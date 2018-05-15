# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-10
import os
from flask import (Flask,request....)
"""
from flask import request

from innp_app.models import db, User

from innp_app.common.rest import RestView


class IndexView(RestView):

    def get(self):
        """
        后台显示内容
        ---
        tags:
          - 后台页面
        """
        return "1111"

    def post(self):
        with db.auto_commit():
            user = User()
            user.set_attrs(request.form)
            db.session.add(user)
        return "1111", 200