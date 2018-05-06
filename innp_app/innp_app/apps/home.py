# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-18
import os
from flask import (Flask,request....)
"""
from flask import jsonify
from flask_restplus import Resource
from innp_app.models import (Cmember, Local, Sgroups,
                             BaseCity,Panalysis, Atracking, Scolumn)
from innp_app.serializers import (CmemberSchema, LocalSchema, SgroupsSchema,LpolicySchema,
                                  BaseCitySchema,PanalysisSchema, AtrackingSchema, ScolumnSchema)


class IndexView(Resource):

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
        return jsonify({'id': 1})


class CmemberListView(Resource):

    def get(self):
        """
        部委数据列表
        :author lyfy
        :return:{Id ， imagePaths，title，insertTime，pubtime，shortContent，source}
        ---
        tags:
          - 前台主页
        """
        # page = request.args.get('id')
        cmember = Cmember.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        return CmemberSchema().dumps(cmember, many=True).data

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


class LocalListView(Resource):
    def get(self):
        """
        地方列表
        :author lyfy
        :return:{Id，imagePaths，insertTime，pubtime，shortContent,source,title}
        ---
        tags:
          - 前台主页
        """
        local = Local.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        return LocalSchema().dumps(local, many=True).data


class SgroupsListView(Resource):

    def get(self):
        """
        社会团体列表
        :author lyfy
        :return:{Id，imagePaths，insertTime，pubtime，shortContent,source,title}
        ---
        tags:
          - 前台主页
        """
        sgroups = Sgroups.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        return ScolumnSchema().dumps(sgroups, many=True).data


class BaseCityListView(Resource):

    def get(self):
        """
        基地列表列表
        :author lyfy
        :return:{Id，imagePaths，insertTime，pubtime，shortContent,source,title}
        ---
        tags:
          - 前台主页
        """
        basecity = BaseCity.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        return BaseCitySchema().dumps(basecity, many=True).data


class LpolicyListView(Resource):
    def get(self):
        """
        最新政策列表
        :author lyfy
        :return:{Id，pubTime，shortContent，source，titile}
        ---
        tags:
          - 前台主页
        """
        lpolicy1 = Cmember.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        lpolicy2 = Local.query.filter_by(deleted=0).all()
        lpolicy = lpolicy1+lpolicy2
        return LpolicySchema().dumps(lpolicy, many=True).data


class PanalysisListView(Resource):

    def get(self):
        """
        政策分析列表
        :author lyfy
        :return:{businessId，title}
        ---
        tags:
          - 前台主页
        """
        panalysis = Panalysis.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        return PanalysisSchema().dumps(panalysis, many=True).data


class AtrackingListView(Resource):

    def get(self):
        """
        活动跟踪列表
        :author lyfy
        :return:{Category，id，picPath，publishTime，source，title}
        ---
        tags:
          - 前台主页
        """
        atracking = Atracking.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        return AtrackingSchema().dumps(atracking, many=True).data


class ScolumnListView(Resource):

    def get(self):
        """
        政策分析
        :author lyfy
        :return:{Id，title}
        ---
        tags:
          - 前台主页
        """
        scolumn = Scolumn.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        return ScolumnSchema().dumps(scolumn, many=True).data