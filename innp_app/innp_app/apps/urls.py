# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-04
import os
from flask import (Flask,request....)
"""
from flask import Blueprint
from .home import (IndexView, CmemberListView, LocalListView, SocioGroupListView,LpolicyListView,
                   BaseCityListView,PanalysisListView, AtrackingListView, ScolumnListView,BroadcastListView)

index = Blueprint('/', __name__)
# 主页面路由
index.add_url_rule(
    '/index',
    view_func=IndexView.as_view('index'),
    endpoint="innp_only_index",
)

index.add_url_rule(
    '/cmember',
    view_func=CmemberListView.as_view('cmember'),
    endpoint="innp_only_cmember",
    methods=["POST", "GET"]
)

index.add_url_rule(
    '/local',
    view_func=LocalListView.as_view('local'),
    endpoint="innp_only_local",
    methods=["GET"]
)

index.add_url_rule(
    '/sociogroup',
    view_func=SocioGroupListView.as_view('sociogroup'),
    endpoint="innp_only_sociogroup",
    methods=["GET"]
)

index.add_url_rule(
    '/basecity',
    view_func=BaseCityListView.as_view('basecity'),
    endpoint="innp_only_basecity",
    methods=["GET"]
)

index.add_url_rule(
    '/lpolicy',
    view_func=LpolicyListView.as_view('lpolicy'),
    endpoint="innp_only_lpolicy",
    methods=["GET"]
)

index.add_url_rule(
    '/panalysis',
    view_func=PanalysisListView.as_view('panalysis'),
    endpoint="innp_only_panalysis",
    methods=["GET"]
)

index.add_url_rule(
    '/atracking',
    view_func=AtrackingListView.as_view('atracking'),
    endpoint="innp_only_atracking",
    methods=["GET"]
)

index.add_url_rule(
    '/scolumn',
    view_func=ScolumnListView.as_view('scolumn'),
    endpoint="innp_only_scolums",
    methods=["GET"]
)

index.add_url_rule(
    '/broadcast',
    view_func=BroadcastListView.as_view('broadcast'),
    endpoint="innp_only_broadcast",
    methods=["GET"]
)