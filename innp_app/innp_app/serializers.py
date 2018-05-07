# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-02
import os
from flask import (Flask,request....)
"""
from marshmallow import (Schema, fields, validate, post_load,
                         validates_schema, ValidationError)

class Schema_one(Schema):
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

class Schema_two(Schema):
    """
    继承Schema类，创建Schema2类
    author lyfy
    :return:{Id ，title}
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    code = fields.Integer(requeired=True)
    msg = fields.String(requeired=True)

class CmemberSchema(Schema_one):
    """
    部委
    author:lyfy
    :return:Id ， imagePaths，title，insertTime，pubtime，shortContent，source
    """
    data = fields.Nested('self',only=["id","imagePaths","title","insertTime","pubtime","shortContent","source"],many=True)

class LocalSchema(Schema_one):
    """
    地方
    author:lyfy
    :return:Id，imagePaths，insertTime，pubtime，shortContent,source,title
    """
    data = fields.Nested('self',only=["id","imagePaths","title","insertTime","pubtime","shortContent","source"],many=True)


class SocioGroupSchema(Schema_one):
    """
    社会团体
    author:lyfy
    :return:Id,imagePaths,insertTime,pubtime,shortContent,source,title
    """
    data = fields.Nested('self',only=["id","imagePaths","title","insertTime","pubtime","shortContent","source"],many=True)

class BaseCitySchema(Schema_one):
    """
    基地
    author:lyfy
    :return:Id，imagePaths，insertTime，pubtime，shortContent，source，title
    """
    data = fields.Nested('self',only=["id","imagePaths","title","insertTime","pubtime","shortContent","source"],many=True)

class LpolicySchema(Schema_two):
    """
    最新政策
    author:lyfy
    :return:Id，pubTime，shortContent，source，titile
    """
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)
    data = fields.Nested('self',only=["id","pubtime","shortContent","source","title"],many=True)

class PanalysisSchema(Schema):
    """
    政策分析
    author:lyfy
    :return:businessId，title
    """
    businessId = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    code = fields.Integer(requeired=True)
    msg = fields.String(requeired=True)
    data = fields.Nested('self',only=["businessId","title"],many=True)


class AtrackingSchema(Schema_two):
    """
    活动跟踪
    author:lyfy
    :return:Category，id，picPath，publishTime，source，title
    """
    picPath = fields.String(validate=validate.Length(6, 12), required=True)
    publishTime = fields.DateTime(dump_only=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)
    Category = fields.String(validate=validate.Length(6, 12), required=True)
    data = fields.Nested('self',only=["id","title","picPath","publishTime","source","Category"],many=True)

class ScolumnSchema(Schema_two):
    """
    专题专栏
    author:lyfy
    :return:Id，title
    """
    data = fields.Nested('self',only=["id","title"],many=True)

class BroadcastSchema(Schema_two):
    """"
    轮播图
    author:lyfy
    :return:Id，title，imagepaths
    """
    imagePaths = fields.String(validate=validate.Length(6, 12), required=True)
    data = fields.Nested('self',only=["id","title","imagePaths"],many=True)
