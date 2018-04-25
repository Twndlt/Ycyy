# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-17
import os
from flask import (Flask,request....)
"""
from flask import (Blueprint, render_template, jsonify, json)
from douban_book.helper import DoubanBook,BookViewModel

book = Blueprint('book', __name__, url_prefix='/book')


@book.route('/search/<q>/', methods=["GET"])
def index(q):
    """
    图书主页
    需要序列化 serializers
    :return:
    """
    if q is not None:
        result = DoubanBook.search_by_keywords(q)
        books = BookViewModel.package_data(result, q)
        return render_template("index.html", data=books.get('books'))
