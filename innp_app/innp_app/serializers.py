# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-02
import os
from flask import (Flask,request....)
"""
from marshmallow import (Schema, fields, validate, post_load,
                         validates_schema, ValidationError)


class CmemberSchema(Schema):
    """
    部委
    author:lyfy
    :return:Id ， imagePaths，title，insertTime，pubtime，shortContent，source
    """
    id = fields.Integer(dump_only=True)
    imagePaths = fields.String(validate=validate.Length(6, 12), required=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    insertTime = fields.DateTime(dump_only=True)
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)

class LocalSchema(Schema):
    """
    地方
    author:lyfy
    :return:Id，imagePaths，insertTime，pubtime，shortContent,source,title
    """
    id = fields.Integer(dump_only=True)
    imagePaths = fields.String(validate=validate.Length(6, 12), required=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    insertTime = fields.DateTime(dump_only=True)
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)

class SgroupsSchema(Schema):
    """
    社会团体
    author:lyfy
    :return:Id,imagePaths,insertTime,pubtime,shortContent,source,title
    """
    id = fields.Integer(dump_only=True)
    imagePaths = fields.String(validate=validate.Length(6, 12), required=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    insertTime = fields.DateTime(dump_only=True)
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)

class BaseCitySchema(Schema):
    """
    基地
    author:lyfy
    :return:Id，imagePaths，insertTime，pubtime，shortContent，source，title
    """
    id = fields.Integer(dump_only=True)
    imagePaths = fields.String(validate=validate.Length(6, 12), required=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    insertTime = fields.DateTime(dump_only=True)
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)

class LpolicySchema(Schema):
    """
    最新政策
    author:lyfy
    :return:Id，pubTime，shortContent，source，titile
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)

class PanalysisSchema(Schema):
    """
    政策分析
    author:lyfy
    :return:businessId，title
    """
    businessId = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)


class AtrackingSchema(Schema):
    """
    活动跟踪
    author:lyfy
    :return:Category，id，picPath，publishTime，source，title
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    picPath = fields.String(validate=validate.Length(6, 12), required=True)
    publishTime = fields.DateTime(dump_only=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)
    Category = fields.String(validate=validate.Length(6, 12), required=True)

class ScolumnSchema(Schema):
    """
    专题专栏
    author:lyfy
    :return:Id，title
    """
    id = fields.String(validate=validate.Length(6, 12), required=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)