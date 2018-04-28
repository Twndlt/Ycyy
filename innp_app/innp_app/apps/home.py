# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-18
import os
from flask import (Flask,request....)
"""
from flask import (Blueprint, render_template, json, request)
from innp_app.forms import LoginForm
from innp_app.models import User

home = Blueprint('home',__name__,url_prefix="/home")

@home.route("/")
def index():
    """
    主页
    """
    return render_template("index.html")


@home.route("/login",methods=["POST","GET"])
def login():
    form = LoginForm()
    """
    登录功能
    """
    if form.validate_on_submit():  ###表格中填入了数据，执行下面操作
        print("111"+form.username.data)
        print("222"+form.password.data)
        user = None
        try:
            user = User.query.filter_by(username=form.username.data).first()
            print(user.password)
            print(user.username)
        except Exception as e:
            user = None
            print("出错了，原因是%s"%e)
        print(user)

        if user is not None and user.password == form.password.data:
            return render_template("index.html")
    return render_template("login.html",form=form)


@home.route("/register",methods=["POST"])
def register():
    """
    注册功能
    """
    pass