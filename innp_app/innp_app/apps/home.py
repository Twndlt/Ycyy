# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-18
import os
from flask import (Flask,request....)
"""
from flask import (Blueprint, render_template, json, request,flash,redirect,url_for)
from ..forms import  RegisterForm
from ..models import User
from ..app import db

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
