# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-10
import os
from flask import (Flask,request....)
"""
from flask import Blueprint

from .icnpp import IndexView

icnpp = Blueprint('icnpp', __name__, url_prefix='/admin')

icnpp.add_url_rule(
    '/',
    view_func=IndexView.as_view('/'),
    endpoint="innp_only_andminindex",
    methods=["POST", "GET"]
)
