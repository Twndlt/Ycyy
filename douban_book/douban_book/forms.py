from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import (DataRequired,length)
# from douban_book.models import User
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class Book_Login(FlaskForm):
    """
    用户登录
    author：吴有为
    time：2018-4-26
    """
    username = StringField(
        label=u"用户名",
        validators=[
            DataRequired(u"用户名不存在"),
            length(1,20)
        ]
    )
    _password = PasswordField(
        lable=u"密码",
        validators=[
            DataRequired(u"密码错误"),
            length(1,20)
        ]
    )
    remember_me = BooleanField(
        label='记住我'
    )
    submit = SubmitField('登录')
