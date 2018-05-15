# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-04-18
import os
from flask import (Flask,request....)
"""
from innp_app.serializers import *
from innp_app.models import (Cmember, Local, SocioGroup,
                             BaseCity, Panalysis, Atracking, Scolumn, Broadcast, Lpolicy, ServiceExpansion)
from innp_app.common.rest import RestView
from innp_app.view_models.index import IndexModelView
from flask_restplus import Resource
from flask import request


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


class CmemberView(RestView):

    def get(self):
        """
        部委数据列表
        :author lyfy
        :return:{Id ， imagePaths，title，insertTime，pubtime，shortContent，source}
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


class LocalView(RestView):
    def get(self):
        """
        地方列表
        :author lyfy
        :return:{Id，imagePaths，insertTime，pubtime，shortContent,source,title}
        ---
        tags:
          - 前台页面
        """
        local = Local.query.filter_by(deleted=0).paginate(page=1, per_page=2).items
        data = IndexModelView()
        data.fill(local)
        content, errors = LocalSchema().dump(data)
        if errors:
            return errors, 400
        return content


class SocioGroupView(RestView):

    def get(self):
        """
        社会团体列表
        :author lyfy
        :return:{Id，imagePaths，insertTime，pubtime，shortContent,source,title}
        ---
        tags:
          - 前台页面
        """
        sociogroup = SocioGroup.query.filter_by(deleted=0).paginate(page=1, per_page=4).items
        data = IndexModelView()
        data.fill(sociogroup)
        content, errors = SocioGroupSchema().dump(data)
        if errors:
            return errors, 400
        return content


class BaseCityView(RestView):

    def get(self):
        """
        基地列表列表
        :author lyfy
        :return:{Id，imagePaths，insertTime，pubtime，shortContent,source,title}
        ---
        tags:
          - 前台页面
        """
        basecity = BaseCity.query.filter_by(deleted=0).paginate(page=1, per_page=4).items
        data = IndexModelView()
        data.fill(basecity)
        content, errors = BaseCitySchema().dump(data)
        if errors:
            return errors, 400
        return content


class LpolicyView(RestView):
    def get(self):
        """
        最新政策列表
        :author lyfy
        :return:{Id，pubTime，shortContent，source，titile}
        ---
        tags:
          - 前台页面
        """
        lpoicy = Lpolicy.query.filter_by(deleted=0).paginate(page=1, per_page=4).items
        data = IndexModelView()
        data.fill(lpoicy)
        content, errors = LpolicySchema().dump(data)
        if errors:
            return errors, 400
        return content


class LpolicyLocalView(RestView):
    def get(self):
        """
        最新政策——地方列表
        :author lyfy
        :return:{Id，pubTime，shortContent，source，titile}
        ---
        tags:
          - 前台主页
        """
        lpoicy = Lpolicy.query.filter_by(deleted=0, type=1).paginate(page=1, per_page=4).items
        data = IndexModelView()
        data.fill(lpoicy)
        content, errors = LpolicySchema().dump(data)
        if errors:
            return errors, 400
        return content


class PanalysisView(RestView):

    def get(self):
        """
        政策分析列表
        :author lyfy
        :return:{businessId，title}
        ---
        tags:
          - 前台页面
        """
        panalysis = Panalysis.query.filter_by(deleted=0, type=1).paginate(page=1, per_page=4).items
        data = IndexModelView()
        data.fill(panalysis)
        content, errors = PanalysisSchema().dump(data)
        if errors:
            return errors, 400
        return content


class AtrackingView(RestView):

    def get(self):
        """
        活动跟踪列表
        :author lyfy
        :return:{Category，id，picPath，publishTime，source，title}
        ---
        tags:
          - 前台页面
        """
        atracking = Atracking.query.filter_by(deleted=0, category=1).paginate(page=1, per_page=10).items
        data = IndexModelView()
        data.fill(atracking)
        content, errors = AtrackingSchema().dump(data)
        if errors:
            return errors, 400
        return content


class AtrackingHitChinaView(RestView):
    def get(self):
        """
        活动跟踪列表__创响中国
        :author lyfy
        :return:{Category，id，picPath，publishTime，source，title}
        ---
        tags:
          - 前台主页
        """
        atracking = Atracking.query.filter_by(deleted=0, category=1).paginate(page=1, per_page=10).items
        data = IndexModelView()
        data.fill(atracking)
        content, errors = AtrackingSchema().dump(data)
        if errors:
            return errors, 400
        return content


class ScolumnView(RestView):

    def get(self):
        """
        政策分析
        :author lyfy
        :return:{Id，title}
        ---
        tags:
          - 前台页面
        """
        scolumn = Scolumn.query.filter_by(deleted=0).paginate(page=1, per_page=10).items
        data = IndexModelView()
        data.fill(scolumn)
        content, errors = ScolumnSchema().dump(data)
        if errors:
            return errors, 400
        return content


class ScolumnIndustriesView(RestView):
    def get(self):
        """
        专题专栏__战略型新兴产业
        :author lyfy
        :return:{Id，title}
        ---
        tags:
          - 前台主页
        """
        scolumn = Scolumn.query.filter_by(deleted=0, category=1).paginate(page=1, per_page=3).items
        data = IndexModelView()
        data.fill(scolumn)
        content, errors = ScolumnSchema().dump(data)
        if errors:
            return errors, 400
        return content


class BroadcastView(RestView):

    def get(self):
        """
        轮播图列表
        ---
        tags:
          - 前台页面
        """
        broadcast = Broadcast.query.filter_by(deleted=0).paginate(page=1, per_page=3).items
        data = IndexModelView()
        data.fill(broadcast)
        content, errors = BroadcastSchema().dump(data)
        if errors:
            return errors, 400
        return content


class DongTaiListOneListView(RestView):
    def post(self):
        """
        动态列表_部委
        ---
        tags:
          - 前台主页
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        data = {
            'allCounts': len(Cmember.query.filter_by(deleted=0).all()),
            'currentPage': 1,
            'list': Cmember.query.filter_by(deleted=0).paginate(page=int(pageNum), per_page=int(pageSize)).items,
            'pageCounts': (len(Cmember.query.filter_by(deleted=0).all()) - 1) // 10 + 1,
            'pageSize': 10
        }
        data1 = IndexModelView()
        data1.fill(data)
        content, errors = DongTaiListSchema().dump(data1)
        if errors:
            return errors, 400
        return content


class DongTaiListTwoListView(RestView):
    def post(self):
        """
        动态列表_地方
        ---
        tags:
          - 前台主页
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        data = {
            'allCounts': len(Local.query.filter_by(deleted=0).all()),
            'currentPage': 1,
            'list': Local.query.filter_by(deleted=0).paginate(page=int(pageNum), per_page=int(pageSize)).items,
            'pageCounts': (len(Local.query.filter_by(deleted=0).all()) - 1) // 10 + 1,
            'pageSize': 10
        }
        data1 = IndexModelView()
        data1.fill(data)
        content, errors = DongTaiListSchema().dump(data1)
        if errors:
            return errors, 400
        return content


class DongTaiListThreeListView(RestView):
    def post(self):
        """
        动态列表_基地
        ---
        tags:
          - 前台主页
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']

        data = {
            'allCounts': len(BaseCity.query.filter_by(deleted=0).all()),
            'currentPage': 1,
            'list': BaseCity.query.filter_by(deleted=0).paginate(page=int(pageNum), per_page=int(pageSize)).items,
            'pageCounts': BaseCity.query.filter_by(deleted=0).paginate.pages,
            'pageSize': 10
        }
        data1 = IndexModelView()
        data1.fill(data)
        content, errors = DongTaiListSchema().dump(data1)
        if errors:
            return errors, 400
        return content


class DongTaiListFourListView(RestView):
    def post(self):
        """
        动态列表_社会团体
        ---
        tags:
          - 前台主页
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        data = {
            'allCounts': len(SocioGroup.query.filter_by(deleted=0).all()),
            'currentPage': 1,
            'list': SocioGroup.query.filter_by(deleted=0).paginate(page=int(pageNum), per_page=int(pageSize)).items,
            'pageCounts': (len(SocioGroup.query.filter_by(deleted=0).all()) - 1) // 10 + 1,
            'pageSize': 10
        }
        data1 = IndexModelView()
        data1.fill(data)
        content, errors = DongTaiListSchema().dump(data1)
        if errors:
            return errors, 400
        return content


class AllNewGaiListView(RestView):
    def post(self):
        """
        专题专栏——全面创新改革列表
        ---
        tags:
          - 前台主页
        """
        pageNum = request.form['pageNum']
        category = request.form['category']  # 各个列表种类
        pageSize = request.form['pageSize']
        type = request.form['type']  # 分全面创新改革，战略性新兴产业
        data = {
            'allCounts': len(Scolumn.query.filter_by(deleted=0).all()),
            'currentPage': 1,
            'list': Scolumn.query.filter_by(deleted=0, type=type, category=category).paginate(page=int(pageNum),
                                                                                              per_page=int(
                                                                                                  pageSize)).items,
            'pageCounts': (len(Scolumn.query.filter_by(deleted=0).all()) - 1) // 10 + 1,
            'pageSize': 10
        }
        data1 = IndexModelView()
        data1.fill(data)
        content, errors = ScolumnListSchema().dump(data1)
        if errors:
            return errors, 400
        return content


class ZhanXinListView(RestView):
    def post(self):
        """
        专题专栏——战略性新兴产业
        ---
        tags:
          - 前台主页
        """
        pageNum = request.form['pageNum']
        category = request.form['category']
        pageSize = request.form['pageSize']
        type = request.form['type']
        data = {
            'allCounts': Scolumn.query.count(),
            'currentPage': 1,
            'list': Scolumn.query.filter_by(deleted=0, category=category, type=type).paginate(page=int(pageNum),
                                                                                              per_page=int(
                                                                                                  pageSize)).items,
            'pageCounts': Scolumn.query.filter_by(deleted=0).paginate(page=int(pageNum),per_page=int(pageSize)).pages,
            'pageSize': 10
        }
        data1 = IndexModelView()
        data1.fill(data)
        content, errors = ScolumnListSchema().dump(data1)
        if errors:
            return errors, 400
        return content


class NewDepartureListView(RestView):
    def post(self):
        """
        最新政策列表
        ---
        tags:
          - 前台主页
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        type = request.form['type']
        data = {
            'allCounts': len(Lpolicy.query.filter_by(deleted=0).all()),
            'currentPage': 1,
            'list': Lpolicy.query.filter_by(deleted=0, type=type).paginate(page=int(pageNum),
                                                                           per_page=int(pageSize)).items,
            'pageCounts': (len(Lpolicy.query.filter_by(deleted=0).all()) - 1) // 10 + 1,
            'pageSize': 10
        }
        data1 = IndexModelView()
        data1.fill(data)
        content, errors = NewDepartureListSchema().dump(data1)
        if errors:
            return errors, 400
        return content


class PolicyAnalysisListView(RestView):
    def post(self):
        """
            政策分析列表
            ---
            tags:
              - 前台主页
            """
        type = request.form['type']
        panalysis = Panalysis.query.filter_by(deleted=0, type=type).paginate(page=1, per_page=10).items
        data = IndexModelView()
        data.fill(panalysis)
        content, errors = PolicyAnalysisListSchema().dump(data)
        if errors:
            return errors, 400
        return content


class ActivitytrackingListView(RestView):
    def post(self):
        """
        活动跟踪列表页
        ---
        tags:
          - 前台主页
        """
        category = request.form['category']
        atracking = Atracking.query.filter_by(deleted=0, category=category).paginate(page=1, per_page=10).items
        data = IndexModelView()
        data.fill(atracking)
        content, errors = ActivitytrackingListSchema().dump(data)
        if errors:
            return errors, 400
        return content


class ServiceExpansionListView(RestView):
    def post(self):
        """
        服务拓展列表
        @author:lyfy
        :return:
        ---
        tags:
          - 前台主页
        """
        service = ServiceExpansion.query.filter_by(deleted=0).paginate(page=1, per_page=10).items
        data = IndexModelView()
        data.fill(service)
        content, errors = ServiceExpansionSchema().dump(data)
        if errors:
            return errors, 400
        return content
