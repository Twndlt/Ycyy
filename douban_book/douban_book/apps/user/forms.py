# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Regexp, Length

class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(),Length(1, 64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          '用户名必须由字母数、字数、下划线或 . 组成')])
    password = PasswordField('密码', validators=[DataRequired(),EqualTo('password2', message='密码必须一至')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('马上注册')