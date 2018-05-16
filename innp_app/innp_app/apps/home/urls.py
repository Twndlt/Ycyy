# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-04
import os
from flask import (Flask,request....)
"""
from flask import Blueprint

from .home import (IndexView, CmemberView, LocalView, SocioGroupView,
                   LpolicyView, BaseCityView, PanalysisView, AtrackingView,
                   ScolumnView, BroadcastView, LpolicyLocalView, AtrackingHitChinaView,
                   ScolumnIndustriesView, DongTaiListOneListView, DongTaiListTwoListView, DongTaiListThreeListView,
                   DongTaiListFourListView, AllNewGaiListView, ZhanXinListView, NewDepartureListView,
                   PolicyAnalysisListView,
                   ActivitytrackingListView, ServiceExpansionListView)

index = Blueprint('/', __name__)
# 主页面路由
index.add_url_rule(
    '/index',
    view_func=IndexView.as_view('index'),
    endpoint="innp_only_index",
)

index.add_url_rule(
    '/cmember',
    view_func=CmemberView.as_view('cmember'),
    endpoint="innp_only_cmember",
    methods=["POST", "GET"]
)

index.add_url_rule(
    '/local',
    view_func=LocalView.as_view('local'),
    endpoint="innp_only_local",
    methods=["GET"]
)

index.add_url_rule(
    '/sociogroup',
    view_func=SocioGroupView.as_view('sociogroup'),
    endpoint="innp_only_sociogroup",
    methods=["GET"]
)

index.add_url_rule(
    '/basecity',
    view_func=BaseCityView.as_view('basecity'),
    endpoint="innp_only_basecity",
    methods=["GET"]
)

index.add_url_rule(
    '/lpolicy',
    view_func=LpolicyView.as_view('lpolicy'),
    endpoint="innp_only_lpolicy",
    methods=["GET"]
)

index.add_url_rule(
    '/lpolicy/local',
    view_func=LpolicyLocalView.as_view('lpolicy/local'),
    endpoint="innp_only_lpolicy/local",
    methods=["GET"]
)

index.add_url_rule(
    '/panalysis',
    view_func=PanalysisView.as_view('panalysis'),
    endpoint="innp_only_panalysis",
    methods=["GET"]
)

index.add_url_rule(
    '/atracking',
    view_func=AtrackingView.as_view('atracking'),
    endpoint="innp_only_atracking",
    methods=["GET"]
)

index.add_url_rule(
    '/atracking/hitchina',
    view_func=AtrackingHitChinaView.as_view('atracking/hitchina'),
    endpoint="innp_only_atracking/hitchina",
    methods=["GET"]
)

index.add_url_rule(
    '/scolumn',
    view_func=ScolumnView.as_view('scolumn'),
    endpoint="innp_only_scolums",
    methods=["GET"]
)

index.add_url_rule(
    '/scolumn/industries',
    view_func=ScolumnIndustriesView.as_view('scolumn/industries'),
    endpoint="innp_only_scolums/industries",
    methods=["GET"]
)

index.add_url_rule(
    '/broadcast',
    view_func=BroadcastView.as_view('broadcast'),
    endpoint="innp_only_broadcast",
    methods=["GET"]
)

index.add_url_rule(
    # 动态列表部委列表页
    # 需传入：pageNum,pageSize
    '/dongTaiOneList',
    view_func=DongTaiListOneListView.as_view('dongTaiOneList'),
    endpoint="innp_only_dongTaiOneList",
    methods=["POST"]
)

index.add_url_rule(
    # 动态列表地方列表页
    # 需传入：pageNum,pageSize
    '/dongTaiTwoList',
    view_func=DongTaiListTwoListView.as_view('dongTaiTwoList'),
    endpoint="innp_only_dongTaiTwoList",
    methods=["POST"]
)

index.add_url_rule(
    # 动态列表基地列表页
    # 需传入：pageNum,pageSize
    '/dongTaiThreeList',
    view_func=DongTaiListThreeListView.as_view('dongTaiThreeList'),
    endpoint="innp_only_dongTaiThreeList",
    methods=["POST"]
)

index.add_url_rule(
    # 动态列表社会团体列表页
    # 需传入：pageNum,pageSize
    '/dongTaiFourList',
    view_func=DongTaiListFourListView.as_view('dongTaiFourList'),
    endpoint="innp_only_dongTaiFourList",
    methods=["POST"]
)

index.add_url_rule(
    # 专题专栏——全面创新改革列表
    # 需传入：pageNum,pageSize,type，category
    # category(1:政策资讯,2:专题动态_中央快讯，3：部委讯息，4：地方报道)
    '/allnewgai',
    view_func=AllNewGaiListView.as_view('allnewgai'),
    endpoint="innp_only_allnewgai",
    methods=["POST"]
)

index.add_url_rule(
    # 专题专栏——战略性新兴产业
    # 需传入：pageNum,pageSize,type，category
    # category(5:政策资讯,6:专题动态_中央快讯，7：部委讯息，8：地方报道)
    '/newIndustry',
    view_func=ZhanXinListView.as_view('newIndustry'),
    endpoint="innp_only_newIndustry",
    methods=["POST"]
)

index.add_url_rule(
    # 最新政策列表
    # 需传入：pageNum,pageSize,type
    '/newdeparture',
    view_func=NewDepartureListView.as_view('newdeparture'),
    endpoint="innp_only_newdeparture",
    methods=["POST"]
)

index.add_url_rule(
    # 政策分析列表
    # 需传入：type
    '/policyanalysis',
    view_func=PolicyAnalysisListView.as_view('policyanalysis'),
    endpoint="innp_only_policyanalysis",
    methods=["POST"]
)

index.add_url_rule(
    # 活动跟踪列表
    # 需传入category
    '/activitytracking',
    view_func=ActivitytrackingListView.as_view('activitytracking'),
    endpoint="innp_only_activitytracking",
    methods=["POST"]
)

index.add_url_rule(
    # 服务拓展列表
    '/serviceexpansion',
    view_func=ServiceExpansionListView.as_view('serviceexpansion'),
    endpoint="innp_only_serviceexpansion",
    methods=["POST"]
)


@index.errorhandler(404)
def get_not_found(error):
    return {'msg': error}, 404
