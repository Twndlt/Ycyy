# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-02
import os
from flask import (Flask,request....)
"""
from marshmallow import (Schema as _Schema, fields, validate)

__all__ = ['CmemberSchema', 'LocalSchema', 'SocioGroupSchema', 'LpolicySchema','BaseCitySchema',
           'PanalysisSchema', 'AtrackingSchema', 'ScolumnSchema', 'BroadcastSchema','DongTaiListSchema',
           "ScolumnListSchema","NewDepartureListSchema",'PolicyAnalysisListSchema','ActivitytrackingListSchema',
           'ServiceExpansionSchema']


class Schema(_Schema):
    """
    继承Schema类，创建Schema1类
    author lyfy
    :return:{Id ， imagePaths，title，insertTime，pubtime，shortContent，source}
    """
    id = fields.Integer(dump_only=True)
    imagePaths = fields.String(validate=validate.Length(6, 12), required=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    insertTime = fields.DateTime(dump_only=True)
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)
    code = fields.Integer(requeired=True)
    msg = fields.String(requeired=True)


class Schema_one(_Schema):
    """
    继承Schema类，创建Schema2类
    author lyfy
    :return:{Id ，title}
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    code = fields.Integer(requeired=True)
    msg = fields.String(requeired=True)


class CmemberSchema(Schema):
    """
    部委
    author:lyfy
    :return:Id ， imagePaths，title，insertTime，pubtime，shortContent，source
    """
    data = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)


class LocalSchema(Schema):
    """
    地方
    author:lyfy
    :return:Id，imagePaths，insertTime，pubtime，shortContent,source,title
    """
    data = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)


class SocioGroupSchema(Schema):
    """
    社会团体
    author:lyfy
    :return:Id,imagePaths,insertTime,pubtime,shortContent,source,title
    """
    data = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)


class BaseCitySchema(Schema):
    """
    基地
    author:lyfy
    :return:Id，imagePaths，insertTime，pubtime，shortContent，source，title
    """
    data = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)


class LpolicySchema(Schema_one):
    """
    最新政策
    author:lyfy
    :return:Id，pubTime，shortContent，source，titile
    """
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(required=True)
    source = fields.String(required=True)
    issuedtime = fields.DateTime(dump_only=True)
    issuedno = fields.String(required=True)
    type1 = fields.Integer(required=True)
    link= fields.String(required=True)
    data = fields.Nested('self',only=['id','title','pubtime','shortContent','issuedtime','issuedno','type1','link'],many=True)


class PanalysisSchema(_Schema):
    """
    政策分析
    author:lyfy
    :return:businessId，title
    """
    businessId = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    type = fields.Integer(required=True)
    code = fields.Integer(requeired=True)
    msg = fields.String(requeired=True)
    # data = fields.Nested('self', only=["businessId", "title", "type"], many=True)
    data = fields.Nested("self",only=["businessId","title","type"],many=True)


class AtrackingSchema(Schema_one):
    """
    活动跟踪
    author:lyfy
    :return:Category，id，picPath，publishTime，source，title
    """
    # picPath = fields.String(validate=validate.Length(6, 12), required=True)
    # publishTime = fields.DateTime(dump_only=True)
    # source = fields.String(validate=validate.Length(6, 12), required=True)
    # category = fields.String(validate=validate.Length(6, 12), required=True)

    data = fields.Nested('self', only=["id", "title", "picPath", "publishTime", "source","category"],many=True)


class ScolumnSchema(Schema_one):
    """
    专题专栏
    author:lyfy
    :return:Id，title
    """
    type = fields.Integer(required=True)
    category = fields.Integer(required=True)
    pubTime = fields.DateTime(required=True)
    data = fields.Nested('self', only=["id", "title","type","category","pubTime"], many=True)


class BroadcastSchema(Schema_one):
    """"
    轮播图
    author:lyfy
    :return:Id，title，imagepaths
    """
    imagePaths = fields.String(validate=validate.Length(6, 12), required=True)
    data = fields.Nested('self', only=["id", "title", "imagePaths"], many=True)


class DongTaiListDataSchema(_Schema):
    data = fields.String(required=True)
    allCounts = fields.Integer(dump_only=True)
    currentPage = fields.Integer(dump_only=True)
    # list = fields.List(fields.Field())
    list = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)
    pageCounts = fields.Integer(dump_only=True)
    pageSize = fields.Integer(dump_only=True)


class DongTaiListSchema(Schema):
    """
    动态列表
    author:lyfy
    :return:Id ， imagePaths，title，insertTime，pubtime，shortContent，source
    """
    # data = fields.Nested('self',only={"id","imagePaths","title","insertTime","pubtime","shortContent","source"},many=True)
    data = fields.Nested(DongTaiListDataSchema())


class AllNewGaiListDataSchema(Schema_one):
    data = fields.String(required=True)
    allCounts = fields.Integer(dump_only=True)
    currentPage = fields.Integer(dump_only=True)
    # list = fields.List(fields.Field())
    list = fields.Nested('self', only=["id", "title", "category","type"],
                         many=True)
    pageCounts = fields.Integer(dump_only=True)
    pageSize = fields.Integer(dump_only=True)


class ScolumnListSchema(Schema):
    """"
    专题专栏列表
    author:lyfy
    :return:Id，title,category,pubTime
    """
    data = fields.Nested(AllNewGaiListDataSchema())


class NewDepartureListDataSchema(_Schema):
    data = fields.String(required=True)
    allCounts = fields.Integer(dump_only=True)
    currentPage = fields.Integer(dump_only=True)
    list = fields.Nested('self', only=["id", "title",  "pubtime", "shortContent", "source","issuedno","issuedtime","link"],
                         many=True)
    pageCounts = fields.Integer(dump_only=True)
    pageSize = fields.Integer(dump_only=True)


class NewDepartureListSchema(Schema_one):
    """"
    最新政策列表
    author:lyfy
    :return:Id，title,category,pubTime
    """
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)
    data = fields.Nested(NewDepartureListDataSchema())


class PolicyAnalysisListSchema(Schema_one):
    """"
    政策分析列表
    author:lyfy
    :return:Id，title,category,pubTime
    """
    data = fields.Nested('self', only=["businessId", "title"],many=True)


class ActivitytrackingListSchema(Schema_one):
    """"
    政策分析列表
    author:lyfy
    :return:Id，title,category,pubTime
    """
    data = fields.Nested('self', only=["id", "title", "picPath", "publishTime", "source","category"],many=True)


class ServiceExpansionSchema(Schema_one):
    """
    服务拓展列表
    @author:lyfy
    :return:
    """
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)
    data = fields.Nested('self',only=['id','title','pubtime','shortContent','source'],many=True)