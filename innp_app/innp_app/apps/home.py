# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-18
import os
from flask import (Flask,request....)
"""
from flask import (Blueprint, request)
from flask_restplus import Api, Resource, fields

from innp_app.models import (Miniac)
from innp_app.serializers import (IndexSchema)

home = Blueprint('api', __name__, url_prefix='/api')
api = Api(home, doc='/docs', title="主页的API接口", version='0.1')


@api.route('/')
class Index(Resource):

    def get(self):
        """
        Index主页
        """
        return {"msg": "主页"}


@api.route("/miniac")
class MiniacIndexView(Resource):

    def get(self):
        """
        部委数据列表
        @author 源哥
        :return:
        """
        # page = request.args.get('id')
        miniac = Miniac.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        return IndexSchema().dump(miniac, many=True).data

    @api.expect(api.model(
        'miniac', {'title': fields.String('标题'), 'content': fields.String('内容')}
    ))
    def post(self):
        """
        新增部委数据
        :return:
        """
        sechema = IndexSchema(many=True)
        return {"user_data": "rest"}


@api.route('/hot')
class Hot(Resource):
    def get(self):
        """
        热门列表
        @author hadoop
        :return:
        """
        return {"data": "hot"}


@api.route('city')
class City(Resource):

    def city(self):
        """
        地方列表
        @author hadoop
        :return:
        """
        return "1"


@api.route('/team')
class Team(Resource):

    def team(self):
        """
        社会团体
        @author hadoop
        :return:
        """
        pass


@api.route('/base')
class BaseCity(Resource):
    def get(self):
        """
        基地
        @author hadoop
        :return:
        """
        pass


@api.route('/column')
class Column(Resource):

    def get(self):
        """
        专题专栏
        @author little、seven
        :return:
        """
        return {"id": "1", "title": "11111222333"}


@api.route('/news')
class News(Resource):

    def get(self):
        """
        最新政策列表
        @author lyfy
        :return:
        """
        pass


@api.route('/pas')
class Pas(Resource):

    def get(self):
        """
        政策分析
        @author lyfy
        :return:
        """
        pass


@api.route('/active-tracking')
class Active(Resource):

    def get(self):
        """
        政策追踪
        @author lyfy
        :return:
        """
        pass


@api.route('/service-dev')
class Service(Resource):

    def get(self):
        """
        服务拓展
        @author lyfy
        :return:
        """
        pass
