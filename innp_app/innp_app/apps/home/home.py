# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-18
import os
from flask import (Flask,request....)
"""
from innp_app.serializers import *

from innp_app.models import (Cmember, Local, SocioGroup,
                             BaseCity, Panalysis, Atracking, Scolumn, Broadcast)
from innp_app.common.rest import RestView

from innp_app.view_models.index import IndexModelView


class IndexView(RestView):

    def get(self):
        """
        前端主页显示内容
        ---
        tags:
          - 前台页面
        """
        cmember = Cmember.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        data = IndexModelView()
        data.fill(cmember)
        content, errors = CmemberSchema().dump(data)
        if errors:
            return errors, 400
        return content


class CmemberListView(RestView):

    def get(self):
        """
        部委数据列表
        :author lyfy
        :return:{Id ， imagePaths，title，insertTime，pubtime，shortContent，source}
        ---
        tags:
          - 前台页面
        """
        data = {
            'data': Cmember.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        }
        content, errors = CmemberSchema().dump(data)
        if errors:
            return errors, 400
        return content

    def post(self):
        """
        新增部委数据
        ---
        tags:
          - 前台页面
        """
        sechema = CmemberSchema(many=True)
        return {"user_data": "rest"}


class LocalListView(RestView):
    def get(self):
        """
        地方列表
        :author lyfy
        :return:{Id，imagePaths，insertTime，pubtime，shortContent,source,title}
        ---
        tags:
          - 前台页面
        """
        data = {
            'code': 200,
            'msg': "数据已成功返回",
            'data': Local.query.filter_by(deleted=0).paginate(page=1, per_page=4).items
        }
        print(data)
        return LocalSchema().dump(data)


class SocioGroupListView(RestView):

    def get(self):
        """
        社会团体列表
        :author lyfy
        :return:{Id，imagePaths，insertTime，pubtime，shortContent,source,title}
        ---
        tags:
          - 前台页面
        """
        data = {
            'code': 200,
            'msg': "数据已成功返回",
            'data': SocioGroup.query.filter_by(deleted=0).paginate(page=1, per_page=4).items
        }
        return SocioGroupSchema().dump(data)


class BaseCityListView(RestView):

    def get(self):
        """
        基地列表列表
        :author lyfy
        :return:{Id，imagePaths，insertTime，pubtime，shortContent,source,title}
        ---
        tags:
          - 前台页面
        """
        data = {
            'code': 200,
            'msg': "数据已成功返回",
            'data': BaseCity.query.filter_by(deleted=0).paginate(page=1, per_page=4).items
        }
        return BaseCitySchema().dump(data)


class LpolicyListView(RestView):
    def get(self):
        """
        最新政策列表
        :author lyfy
        :return:{Id，pubTime，shortContent，source，titile}
        ---
        tags:
          - 前台页面
        """
        data = {
            'code': 200,
            'msg': "数据已成功返回",
            'data': Cmember.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        }
        return LpolicySchema().dump(data)


class PanalysisListView(RestView):

    def get(self):
        """
        政策分析列表
        :author lyfy
        :return:{businessId，title}
        ---
        tags:
          - 前台页面
        """
        data = {
            'code': 200,
            'msg': "数据已成功返回",
            'data': Panalysis.query.filter_by(deleted=0).paginate(page=1, per_page=5).items
        }
        return PanalysisSchema().dump(data)


class AtrackingListView(RestView):

    def get(self):
        """
        活动跟踪列表
        :author lyfy
        :return:{Category，id，picPath，publishTime，source，title}
        ---
        tags:
          - 前台页面
        """
        data = {
            'code': 200,
            'msg': "数据已成功返回",
            'data': Atracking.query.filter_by(deleted=0).paginate(page=1, per_page=5).items
        }
        return AtrackingSchema().dump(data)


class ScolumnListView(RestView):

    def get(self):
        """
        政策分析
        :author lyfy
        :return:{Id，title}
        ---
        tags:
          - 前台页面
        """
        data = {
            'code': 200,
            'msg': "数据已成功返回",
            'data': Scolumn.query.filter_by(deleted=0).paginate(page=1, per_page=3).items
        }
        return ScolumnSchema().dump(data)


class BroadcastListView(RestView):

    def get(self):
        """
        轮播图列表
        ---
        tags:
          - 前台页面
        """
        data = {
            'code': 200,
            'msg': "数据已成功返回",
            'data': Broadcast.query.filter_by(deleted=0).paginate(page=1, per_page=4).items
        }
        return BroadcastSchema().dump(data)
