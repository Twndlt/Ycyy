# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-02
import os
from flask import (Flask,request....)
"""
from marshmallow import (Schema, fields, validate, post_load,
                         validates_schema, ValidationError)


class IndexSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    content = fields.String(validate=validate.Length(6, 12), required=True)
    updated_at = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

class Indexpas(Schema):
    title = fields.String(dump_only=True)
    source = fields.String(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

class Indexactive(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(dump_only=True)
    source = fields.String(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

class Indexservice(Schema):
    title = fields.String(dump_only=True)
    source = fields.String(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

class Indexcity(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(dump_only=True)
    image = fields.String(dump_only=True)
    source = fields.String(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

class Indexnews(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(dump_only=True)
    image = fields.String(dump_only=True)
    source = fields.String(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

class Indexhot(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(dump_only=True)
    image = fields.String(dump_only=True)
    source = fields.String(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

class Indexteam(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(dump_only=True)
    image = fields.String(dump_only=True)
    source = fields.String(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

class Indexbasecity(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(dump_only=True)
    image = fields.String(dump_only=True)
    source = fields.String(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
