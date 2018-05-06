# -*- coding: utf-8 -*-
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
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
    cmember = db.relationship('Cmember', uselist=False)  # 主键

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


class Cmember(Base):
    """
    部委
    author:lyfy
    :return:[<Cmember:XXX>]
    """
    id = db.Column(db.Integer, primary_key=True)
    imagePaths = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(50), unique=True)
    insertTime = db.Column(db.DateTime, default=datetime.utcnow)
    pubtime = db.Column(db.DateTime, default=datetime.utcnow)
    shortContent = db.Column(db.Text)
    source = db.Column(db.String(255), unique=True)  # 来源
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Cmember:{}>'.format(self.title)


class Local(Base):
    """
    地方
    @author lyfy
    :return:[<Local:XXX>]
    """
    id = db.Column(db.Integer, primary_key=True)
    imagePaths = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(50), unique=True)
    insertTime = db.Column(db.DateTime, default=datetime.utcnow)
    pubtime = db.Column(db.DateTime, default=datetime.utcnow)
    shortContent = db.Column(db.Text)
    source = db.Column(db.String(255), unique=True)  # 来源
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Local:{}>'.format(self.title)


class Sgroups(Base):
    """
    社会团体
    @author lyfy
    :return:[<Sgroups:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    imagePaths = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(50), unique=True)
    insertTime = db.Column(db.DateTime, default=datetime.utcnow)
    pubtime = db.Column(db.DateTime, default=datetime.utcnow)
    shortContent = db.Column(db.Text)
    source = db.Column(db.String(255), unique=True)  # 来源
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Sgroups:{}>'.format(self.title)


class BaseCity(Base):
    """
    基地
    @author lyfy
    :return:[<BaseCity:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    imagePaths = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(50), unique=True)
    insertTime = db.Column(db.DateTime, default=datetime.utcnow)
    pubtime = db.Column(db.DateTime, default=datetime.utcnow)
    shortContent = db.Column(db.Text)
    source = db.Column(db.String(255), unique=True)  # 来源
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<BaseCity:{}>'.format(self.title)


class Panalysis(Base):
    """"
    政策分析
    @author lyfy
    :return:[<Panalysis:xxx>]
    """
    businessId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Panalysis:{}>'.format(self.title)


class Atracking(Base):
    """"
    活动跟踪
    @author lyfy
    :return:[<Atracking:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    Category = db.Column(db.String(50), unique=True)
    picPath = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(50), unique=True)
    source = db.Column(db.String(50), unique=True)  # 来源
    publishTime = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Atracking:{}>'.format(self.title)


class Scolumn(Base):
    """"
    专题专栏
    @author lyfy
    :return:[<Scolumn:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键
    def __repr__(self):
        return '<Scolumn:{}>'.format(self.title)
