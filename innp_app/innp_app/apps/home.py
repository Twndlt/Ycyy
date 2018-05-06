# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-18
import os
from flask import (Flask,request....)
"""
from flask import jsonify
from flask_restplus import Resource
from innp_app.models import (Miniac, Pas, Active,
                             Service, City, Hot, Team, BaseCity)
from innp_app.serializers import (IndexSchema, Indexpas, Indexactive,
                                  Indexservice, Indexcity, Indexnews, Indexhot,
                                  Indexteam, Indexbasecity)


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


class MiniacListView(Resource):

    def get(self):
        """
        部委数据列表
        ---
        tags:
          - 前台主页
        """
        # page = request.args.get('id')
        miniac = Miniac.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        return IndexSchema().dump(miniac, many=True).data

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
        sechema = IndexSchema(many=True)
        return {"user_data": "rest"}


class HotIndex(Resource):
    def get(self):
        """
        热门列表
        :author hadoop
        :return:{id,updated_at,title,created_at,source}
        """
        hot = Hot.query.filter_by(deleted=0).all()  # 这里取数据库的数据
        return Indexhot().dump(hot, many=True).data


class CityIndex(Resource):

    def get(self):
        """
        地方列表
        :author hadoop
        :return:{id,updated_at,title,created_at,source}
        """
        city = City.query.filter_by(deleted=0).all()
        return Indexcity().dump(city, many=True).data


class TeamIndex(Resource):

    def get(self):
        """
        社会团体
        :author hadoop
        :return:{id,updated_at,title,created_at,source}
        """
        team = Team.query.filter_by(deleted=0).all()  # 这里应该取数据库的数据
        return Indexteam().dump(team, many=True).data


class BaseCityIndex(Resource):
    def get(self):
        """
        基地
        ---
        tags:
          - 前台主页
        """
        basecity = BaseCity.query.filter_by(deleted=0).all()  # 这里应该取数据库的数据
        return IndexSchema().dumps(basecity, many=True).data


class Column(Resource):

    def get(self):
        """
        专题专栏
        :author little、seven
        :return:
        """
        return {"id": "1", "title": "11111222333"}


class News(Resource):

    def get(self):
        """
        最新政策列表
        :author lyfy
        :return:{id,updated_at,title,created_at,source}
        """
        new1 = Miniac.query.filter_by(deleted=0).all()  # 这里应该取数据库的数据
        new2 = City.query.filter_by(deleted=0).all()
        news = new1 + new2
        return Indexnews().dump(news, many=True).data


class PasIndex(Resource):

    def get(self):
        """
        政策分析
        :author lyfy
        :return:{updated_at,title,created_at,source}
        """
        pas = Pas.query.filter_by(deleted=0).all()  # 这里应该取数据库的数据
        return Indexpas().dump(pas, many=True).data


class ActiveIndex(Resource):

    def get(self):
        """
        政策追踪
        :author lyfy
        :return:{id,updated_at,title,created_at,source}
        """
        active = Active.query.filter_by(deleted=0).all()  # 这里应该取数据库的数据
        return Indexactive().dump(active, many=True).data


class ServiceIndex(Resource):

    def get(self):
        """
        服务拓展
        :author lyfy
        :return:{updated_at,title,created_at,source}
        """
        service = Service.query.filter_by(deleted=0).all()  # 这里应该取数据库的数据
        return Indexservice().dump(service, many=True).data
