# -*- coding: utf-8 -*-
from datetime import datetime

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted = db.Column(db.Integer, default=0)  # 逻辑删除:0表示显示，1表示删除
    active = db.Column(db.Integer, default=0)  # 禁用/启用:0表示显示，1表示删除


class User(Base):
    """
    用户表
    """
    __tablename__ = 'user'
    pass
