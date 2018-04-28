# -*- coding: utf-8 -*-
# **************************************************************************
# Author: 杨举成
# Email: tyhg@sina.com
# Created: 2018-4-25
# Last Update:星期五 2018-4-25
# Description:
# **************************************************************************

from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

class User(db.Model):
    """"用户"""
    __tablename__ = "info_user"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    nick_name = db.Column(db.String(32), unique=True, nullable=False)  # 用户昵称
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    mobile = db.Column(db.String(11), unique=True, nullable=False)  # 手机号
    avatar_url = db.Column(db.String(256))  # 用户头像路径
    last_login = db.Column(db.DateTime, default=datetime.datetime.now())  # 最后一次登录时间
    is_admin = db.Column(db.Boolean, default=False)
    signature = db.Column(db.String(512))  # 用户签名
    gender = db.Column(db.Enum( "MAN","WOMAN"),default="MAN")