# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-18
import os
from flask import (Flask,request....)
"""
from flask import (Blueprint, render_template, json, request,flash,redirect,url_for)
from innp_app.forms import  (RegisterForm,LoginForm)
from innp_app.models import User
from innp_app import db

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
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash(message=u'该用户名已经注册', category='danger')
            return render_template('index.html', form=form)
        else:
            if form.password.data == form.password2.data:
                user = User(email=form.email.data,
                            username=form.username.data,
                            password=form.password.data, )
                db.session.add(user)
                db.session.commit()
                flash(message=u'注册成功，请登陆', category='success')
                return redirect(url_for('home.login'))
            else:
                flash(message=u'两次密码不一至', category='danger')
                return render_template('index.html', form=form)
    else:
        return render_template('index.html', form=form)
