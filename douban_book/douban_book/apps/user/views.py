# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for,request,flash
from . import user
from .forms import  RegistrationForm
from .models import User
from ...app import db

@user.route('/register', methods=["GET",'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash(message=u'该用户名已经注册', category='danger')
            return render_template('register.html', form=form)
        else:
            if form.password.data == form.password2.data:
                user = User(username=form.username.data,
                            password=form.password.data,)
                db.session.add(user)
                db.session.commit()
                flash(message=u'注册成功，请登陆', category='success')
                return redirect(url_for('user.login'))
            else:
                flash(message=u'两次密码不一至', category='danger')
                print('两次密码不一至')
                return render_template('register.html', form=form)
    else:
        return render_template('register.html', form=form)



@user.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('index.html',title=u'登录')
