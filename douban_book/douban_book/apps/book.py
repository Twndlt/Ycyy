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


<<<<<<< HEAD
@book.route('/search/<q>/', methods=["GET"])
def index(q):
=======
@book.route('Login/', methods=["GET","POST"])
def index():
>>>>>>> a7e9100b64cd66bdec092f233369aadbf3bec954
    """
    登录
    author：吴有为
    time：2018-4-26
    :return:
    """
<<<<<<< HEAD
    if q is not None:
        result = DoubanBook.search_by_keywords(q)
        books = BookViewModel.package_data(result, q)
        return render_template("index.html", data=books.get('books'))
=======
    form = Book_Login()
    if form.validate_on_submit():
        pass
    return render_template('login.html', form=form)

@book.route('shuangchuang/', methods=["GET","POST"])
def SC():
    """
    双创
    """
    return render_template('index.html')
>>>>>>> a7e9100b64cd66bdec092f233369aadbf3bec954
