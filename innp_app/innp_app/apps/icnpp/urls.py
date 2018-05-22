# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-10
import os
from flask import (Flask,request....)
"""
from flask import Blueprint

from .icnpp import IndexView, MediaView, ActivityManageView, MascotView, GuestView, HallView, CenterNewView, \
    ActivityTypeView, LocalNewView, DepartmentView, policyView, LocalReportView

icnpp = Blueprint('icnpp', __name__)

icnpp.add_url_rule(
    '/',
    view_func=IndexView.as_view('/'),
    endpoint="innp_only_andminindex",
    methods=["POST", "GET"]
)

icnpp.add_url_rule(
    '/mediaview',
    view_func=MediaView.as_view("/"),
    endpoint="AddMedia",
    methods=["POST"]
)

icnpp.add_url_rule(
    '/addmanage',
    view_func=ActivityManageView.as_view("/"),
    endpoint="addmanage",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/mascot",
    view_func=MascotView.as_view("/"),
    endpoint="addmascot",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/guest",
    view_func=GuestView.as_view("/"),
    endpoint="addguest",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/hall",
    view_func=HallView.as_view("/"),
    endpoint="addhall",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/atype",
    view_func=ActivityTypeView.as_view("/"),
    endpoint="addactivitytype",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/cnew",
    view_func=CenterNewView.as_view("/"),
    endpoint="addcenternew",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/lnew",
    view_func=LocalNewView.as_view("/"),
    endpoint="addlocalnew",
    methods=["POST"]
)
icnpp.add_url_rule(
    "/dp",
    view_func=DepartmentView.as_view("/"),
    endpoint="adddepartment",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/policy",
    view_func=policyView.as_view("/"),
    endpoint="Addpolicy",
    methods=["POST"]
)

icnpp.add_url_rule(
    "lpview",
    view_func=LocalReportView.as_view("/"),
    endpoint="AddLocalReport",
    methods=["POST"]
)