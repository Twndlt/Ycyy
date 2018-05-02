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
    username = fields.String(validate=validate.Length(6, 12), required=True)
    password = fields.String(validate=validate.Length(6, 12), required=True)
    update_by = fields.DateTime(dump_only=True)
    create_by = fields.DateTime(dump_only=True)
