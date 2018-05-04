# -*- coding: utf-8 -*-
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

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
    __tablename__ = "user"
    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    email = db.Column(db.String(40), unique=True)
    phone = db.Column(db.Integer)
    resume_url = db.String(db.String(255))
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    miniac = db.relationship('Miniac', uselist=False)  # 主键

    def __repr__(self):
        return '<Admin:{}>'.format(self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY

    @property
    def is_active(self):
        if self.active == 0:
            return "禁用"
        else:
            return "启用"

    @classmethod
    def get_alluser(self):
        return User.query.filter_by(deleted=0).all()


class Miniac(Base):
    """
    部委
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    content = db.Column(db.Text(50), unique=True)
    source = db.Column(db.String(255), unique=True)  # 来源
    images = db.Column(db.String(50), unique=True)
    dec = db.Column(db.String(100), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Miniac:{}>'.format(self.title)


class Pas(Base):
    """
    政策分析
    @author lyfy
    :return:[<Pas:XXX>]
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    source = db.Column(db.String(50), unique=True)  # 来源
    images = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Pas:{}>'.format(self.title)


class Active(Base):
    """
    政策追踪
    @author lyfy
    :return:[<Active:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    source = db.Column(db.String(50), unique=True)  # 来源
    images = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Active:{}>'.format(self.title)


class Service(Base):
    """
    服务拓展
    @author lyfy
    :return:[<Service:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    source = db.Column(db.String(50), unique=True)  # 来源
    images = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Service:{}>'.format(self.title)


class City(Base):
    """"
    地方列表
    @author hadoop
    :return:[<city:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    source = db.Column(db.String(50), unique=True)  # 来源
    images = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<City:{}>'.format(self.title)


class Hot(Base):
    """"
    热门列表
    @author hadoop
    :return:[<Hot:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    source = db.Column(db.String(50), unique=True)  # 来源
    images = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return '<Hot:{}>'.format(self.title)


class Team(Base):
    """"
    社会团体
    @author hadoop
    :return:[<Team:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    source = db.Column(db.String(50), unique=True)  # 来源
    images = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return '<Team:{}>'.format(self.title)


class BaseCity(Base):
    """"
    基地
    @author hadoop
    :return:[<BaseCity:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    source = db.Column(db.String(50), unique=True)  # 来源
    images = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return '<BaseCity:{}>'.format(self.title)
