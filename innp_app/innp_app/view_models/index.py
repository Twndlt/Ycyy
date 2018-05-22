# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-12
import os
from flask import (Flask,request....)
"""


class IndexModelView:

    def __init__(self):
        self.code = 400
        self.msg = '无正确数据!'
        self.data = []

    def fill(self, items_data=None):
        if items_data:
            self.data = items_data
            self.code = 200
            self.msg = "数据已取出!"

