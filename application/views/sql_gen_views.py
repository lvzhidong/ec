#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -------------------
# @Time    : 2020/9/30 3:07 PM
# @Version : 1.0
# @Author  : lvzhidong
# @For : 
# -------------------

from datetime import datetime, timedelta
from flask_admin import BaseView, expose
from flask import request


def gen_sql_1(begin_date, end_date, opt_cd):
    """查询某个操作码一段日期内的触发次数"""
    sql = """SELECT dt, count(android_id)
FROM f_evt_sdk_log_101
WHERE opt_cd = '{}' and
dt >='{}' and dt<='{}'
GROUP BY dt
ORDER BY dt ASC""".format(opt_cd, begin_date, end_date)
    return sql


def gen_sql_2(begin_date, end_date, opt_cd):
    """查询某个操作码一段日期内的触发人数"""
    sql = """SELECT dt, count(distinct android_id)
FROM f_evt_sdk_log_101
WHERE opt_cd = '{}' and
dt>='{}' and dt<='{}'
GROUP BY dt
ORDER BY dt ASC""".format(opt_cd, begin_date, end_date)
    return sql


def gen_sql_3(begin_date, end_date, opt_cd, adv_id):
    """某个广告位请求次数统计【可更换展示操作码】"""
    sql = """SELECT dt, count(receive_time) 
FROM f_evt_sdk_log_105 
WHERE adv_id = '{}' 
AND opt_cd = '{}' and 
dt>='{}' and dt<='{}'
GROUP BY dt
ORDER BY dt ASC""".format(adv_id, opt_cd, begin_date, end_date)
    return sql


def gen_sql_4(begin_date, end_date, opt_cd_1, opt_cd_2):
    """2个操作步骤的人数漏斗统计"""
    sql = """SELECT t1.opt_cd, t2.opt_cd, count(distinct t2.android_id) user_num 
FROM f_evt_sdk_log_101 t1 join f_evt_sdk_log_101 t2 on t1.android_id=t2.android_id
where t1.opt_cd in ('{}', '{}')
and t2.opt_cd in ('{}', '{}')
and t1.dt>='{}' and t1.dt<='{}'
and t2.dt>='{}' and t2.dt<='{}'
group by t1.opt_cd, t2.opt_cd order by user_num desc;
""".format(opt_cd_1, opt_cd_2, opt_cd_1, opt_cd_2, begin_date, end_date, begin_date, end_date)
    return sql


def gen_sql_5(begin_date, end_date, opt_cd_1, opt_cd_2, opt_cd_3):
    """3个操作步骤的人数漏斗统计"""
    sql = """select t1.opt_cd, t2.opt_cd, t3.opt_cd, count(distinct t1.android_id) as num 
from f_evt_sdk_log_101 t1 join f_evt_sdk_log_101 t2 on t1.android_id=t2.android_id join f_evt_sdk_log_101 t3 on t2.android_id=t3.android_id
where t1.opt_cd in ('{}', '{}', '{}') 
and t2.opt_cd in ('{}', '{}', '{}') 
and t3.opt_cd in ('{}', '{}', '{}')
and t1.dt>='{}' and t1.dt<='{}'
and t2.dt>='{}' and t2.dt<='{}'
and t3.dt>='{}' and t3.dt<='{}'
group by t1.opt_cd, t2.opt_cd, t3.opt_cd
order by num desc;
""".format(opt_cd_1, opt_cd_2, opt_cd_3, opt_cd_1, opt_cd_2, opt_cd_3, opt_cd_1, opt_cd_2, opt_cd_3,
           begin_date, end_date, begin_date, end_date, begin_date, end_date)
    return sql


def gen_sql_6(target_date, other_opt_cd):
    """6. 某天打开次日留存 【不含外广】【具体操作码具体修改】"""
    d_target_date = datetime.strptime(target_date, '%Y-%m-%d')
    d_next_day = d_target_date + timedelta(days=1)
    next_day = d_next_day.strftime('%Y-%m-%d')
    sql = """(select count(distinct android_id) from f_evt_sdk_log_101 where dt='{}' and opt_cd='t000_open_app')  
union all
select count(*) from 
    (select android_id, count(opt_cd) as num1 from f_evt_sdk_log_101 where dt='{}' and opt_cd='t000_open_app' 
        and android_id in 
            (select distinct android_id from f_evt_sdk_log_101 where dt='{}' and opt_cd='t000_open_app')  
     group by android_id) t1 
 left join
    (select android_id, count(opt_cd) as num2 from f_evt_sdk_log_101 where dt='{}' and opt_cd='{}' group by android_id) t2 
    on t1.android_id=t2.android_id
    
where t1.num1>t2.num2 or t2.android_id is null
""".format(target_date, next_day, target_date, next_day, other_opt_cd)
    return sql


class SqlGenView(BaseView):
    # extra_js = [
    #     '/static/copy.js',
    # ]

    @expose('/', methods=['GET', 'POST'])
    def index(self):
        form = request.form
        sql = ''
        sql_id = form.get('sql_id')
        # print(dict(form))
        # return self.render('test.html')
        if sql_id == 'sql_1':
            sql = gen_sql_1(form['begin_date'], form['end_date'], form['opt_cd'])
        elif sql_id == 'sql_2':
            sql = gen_sql_2(form['begin_date'], form['end_date'], form['opt_cd'])
        elif sql_id == 'sql_3':
            sql = gen_sql_3(form['begin_date'], form['end_date'], form['opt_cd'], form['adv_id'])
        elif sql_id == 'sql_4':
            sql = gen_sql_4(form['begin_date'], form['end_date'], form['opt_cd_1'], form['opt_cd_2'])
        elif sql_id == 'sql_5':
            sql = gen_sql_5(form['begin_date'], form['end_date'], form['opt_cd_1'], form['opt_cd_2'], form['opt_cd_3'])
        elif sql_id == 'sql_6':
            sql = gen_sql_6(form['target_date'], form['other_opt_cd'])

        return self.render('sql_gen.html', sql=sql)
