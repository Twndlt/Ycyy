# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-10
import os
from flask import (Flask,request....)
"""


class RestError(Exception):
    """异常基类
    """

    def __init__(self, code, message):
        """初始化异常
        Aargs:
            code (int): http 状态码
            message (str): 错误信息
        """
        self.code = code
        self.message = message
        super(RestError, self).__init__()
