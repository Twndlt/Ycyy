# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-18
import os
from flask import (Flask,request....)
"""
from flask import (Blueprint, render_template, json, request)

home = Blueprint('home',__name__,url_prefix="/home")

@home.route("/")
def index():
    """
    主页
    """
    return render_template("index.html")


@home.route("/login",methods=["POST"])
def login():
    """
    登录功能
    """
    pass


@home.route("/register",methods=["POST"])
def register():
    """
    注册功能
    """
    pass