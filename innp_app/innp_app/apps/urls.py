# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-04
import os
from flask import (Flask,request....)
"""
from flask import Blueprint
from .home import (IndexView, MiniacListView,
                   BaseCityIndex)

index = Blueprint('/', __name__)
# 主页面路由
index.add_url_rule(
    '/index',
    view_func=IndexView.as_view('index'),
    endpoint="innp_only_index",
)

index.add_url_rule(
    '/miniac',
    view_func=MiniacListView.as_view('miniac'),
    endpoint="innp_only_miniac",
    methods=["POST", "GET"]
)

index.add_url_rule(
    '/basecity',
    view_func=BaseCityIndex.as_view('basecity'),
    endpoint="innp_only_basecity",
    methods=["GET"]
)
