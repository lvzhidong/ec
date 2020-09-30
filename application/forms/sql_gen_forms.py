#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -------------------
# @Time    : 2020/9/30 3:21 PM
# @Version : 1.0
# @Author  : lvzhidong
# @For : 
# -------------------

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import DateField


class SqlGenForm(FlaskForm):
    begin_date = DateField('开始日期')

