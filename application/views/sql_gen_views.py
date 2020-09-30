#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -------------------
# @Time    : 2020/9/30 3:07 PM
# @Version : 1.0
# @Author  : lvzhidong
# @For : 
# -------------------


from flask_admin import BaseView, expose
from flask import request


class SqlGenView(BaseView):
    extra_js = [
        '/static/copy.js',
    ]

    @expose('/', methods=['GET', 'POST'])
    def index(self):
        form = request.form
        print(str(form))
        return self.render('sql_gen.html')
