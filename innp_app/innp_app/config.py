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
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:test@192.168.10.114:3306/innp_app?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SWAGGER_UI_JSONEDITOR = True

    SWAGGER = {
        "swagger_version": "2.0",
        "title": "Innp项目",
        "headers": [
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
            ('Access-Control-Allow-Credentials', "true"),
        ],
        "specs": [
            {
                "version": "0.1",
                "title": "主页API接口列表",
                "description": 'This is the version 0.1 of Innp_app API',
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        # "static_folder": "static",  # must be set by user
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }


class TestingConfig:
    pass


class ProConfig:
    pass


configs = {
    'developments': DevelopmentsConfig,
    'testing': TestingConfig
}
