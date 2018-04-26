# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-17
import os
from flask import (Flask,request....)
"""
from flask import (Blueprint, render_template, jsonify, json)
# from douban_book.helper import DoubanBook,BookViewModel
from douban_book.forms import Book_Login

book = Blueprint('book', __name__, url_prefix='/')


@book.route('Login/', methods=["GET","POST"])
def index():
    """
    登录
    :return:
    """
    form = Book_Login()
    if form.validate_on_submit():
        pass
    return render_template('login.html', form=form)
