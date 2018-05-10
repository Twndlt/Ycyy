# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-18
import os
from flask import (Flask,request....)
"""
from flask import g
from flask_restplus import Resource

from innp_app.serializers import *

from innp_app.models import (Cmember, Local, SocioGroup,
                             BaseCity, Panalysis, Atracking, Scolumn, Broadcast)
from innp_app.common.rest import RestView


class IndexView(RestView):
    method_decorators = ()

    def get(self):
        """
        前端主页显示内容
        ---
        tags:
          - 前台主页
        parameters:
          - name: target_type
            in: path
            description: currently only "candidate" is supported
            required: true
            type: string
            default: candidate
          - name: item_type
            in: path
            description: currently only "openings" is supported
            required: true
            type: string
            default: openings
          - in: body
            name: body
            schema:
              id: rec_query
              required:
                - candidate_id
                - context
              properties:
                candidate_id:
                  type: integer
                  description: Id of the target (candidate / user)
                  default: 123456
                exclude:
                  type: array
                  description: item_ids to exclude from recs
                  default: [12345, 123456]
                  items:
                      type: integer
                context:
                  type: object
                  schema:
                    $ref: '#/definitions/rec_query_context'
        responses:
          200:
            description: A single recommendation item
            schema:
              id: rec_response
              properties:
                opening_id:
                  type: integer
                  description: The id of the opening
                  default: 123456
          204:
             description: No recommendation found
        """
        data = {
            'data': Cmember.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        }
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
          - 前台主页
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
          - 前台主页
        parameters:
          - name: target_type
            in: path
            description: currently only "candidate" is supported
            required: true
            type: string
            default: candidate
          - name: item_type
            in: path
            description: currently only "openings" is supported
            required: true
            type: string
            default: openings
          - in: body
            name: body
            schema:
              id: rec_query
              required:
                - candidate_id
                - context
              properties:
                candidate_id:
                  type: integer
                  description: Id of the target (candidate / user)
                  default: 123456
                exclude:
                  type: array
                  description: item_ids to exclude from recs
                  default: [12345, 123456]
                  items:
                      type: integer
                context:
                  type: object
                  schema:
                    $ref: '#/definitions/rec_query_context'
        responses:
          200:
            description: A single recommendation item
            schema:
              id: rec_response
              properties:
                opening_id:
                  type: integer
                  description: The id of the opening
                  default: 123456
          204:
             description: No recommendation found
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
          - 前台主页
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
          - 前台主页
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
          - 前台主页
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
          - 前台主页
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
          - 前台主页
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
          - 前台主页
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
          - 前台主页
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
          - 前台主页
        """
        data = {
            'code': 200,
            'msg': "数据已成功返回",
            'data': Broadcast.query.filter_by(deleted=0).paginate(page=1, per_page=4).items
        }
        return BroadcastSchema().dump(data)
