# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-28
import os
from flask import (Flask,request....)
"""
import pymysql


class BaseConfig:
    USER_PER_PAGE = 10


class DevelopmentsConfig(BaseConfig):
    """
    开发环境
    """
    DEBUG = True
    SECRET_KEY = '7d58afd5-5fdb-48b0-9c99-3466c2838745'
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymyaql://test:test@192.168.10.114:3306/inapp_app?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig:
    pass


class ProConfig:
    pass


configs = {
    'developments': DevelopmentsConfig,
    'testing': TestingConfig
}
