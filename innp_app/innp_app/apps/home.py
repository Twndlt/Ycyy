# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-18
import os
from flask import (Flask,request....)
"""
from flask import (Blueprint, render_template, json, request, flash, redirect, url_for)
from innp_app.forms import (RegisterForm, LoginForm)
from innp_app.models import ()

home = Blueprint('home', __name__, url_prefix="/home")


@home.route("/")
def index():
    """
    主页
    """
    return render_template("index.html")


@home.route("/miniac", methods=["GET"])
def miniac():
    """
    部委
    @author 源哥
    :return:
    """
    pass


@home.route('/hot', methods=["GET"])
def hot():
    """
    热门
    @author hadoop
    :return:
    """
    pass


@home.route('city', methods=["GET"])
def city():
    """
    地方
    @author hadoop
    :return:
    """
    pass


@home.route('/team', methods=["GET"])
def team():
    """
    社会团体
    @author hadoop
    :return:
    """
    pass


@home.route('/base', methods=["GET"])
def base():
    """
    基地
    @author hadoop
    :return:
    """
    pass


@home.route('/column', methods=["GET"])
def column():
    """
    专题专栏
    @author little、seven
    :return:
    """
    pass


@home.route('/news', methods=["GET"])
def news():
    """
    最新政策
    @author lyfy
    :return:
    """
    pass


@home.route('/pas', methods=["GET"])
def pas():
    """
    政策分析
    @author lyfy
    :return:
    """
    pass


@home.route('/active-tracking', methods=["GET"])
def active():
    """
    政策追踪
    @author lyfy
    :return:
    """
    pass


@home.route('/service-dev', methods=["GET"])
def service():
    """
    服务拓展
    @author lyfy
    :return:
    """
    pass
