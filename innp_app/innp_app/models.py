# -*- coding: utf-8 -*-
from datetime import datetime
from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = SQLAlchemy()


class _Base(db.Model):
    __abstract__ = True
    deleted = db.Column(db.SmallInteger, default=0)  # 逻辑删除:0表示显示，1表示删除
    active = db.Column(db.SmallInteger, default=0)  # 禁用/启用:0表示显示，1表示删除


class Base(_Base):
    """
    继承_Base类
    :author lyfy
    :return:{Id ， imagePaths，title，insertTime，pubtime，shortContent，source}
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    imagePaths = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(50), unique=True, nullable=True)
    insertTime = db.Column(db.DateTime, default=datetime.utcnow)
    pubtime = db.Column(db.DateTime, default=datetime.utcnow)
    shortContent = db.Column(db.Text, nullable=True)
    source = db.Column(db.String(255), unique=True, nullable=True)  # 来源

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            # hasattr(self,key) # 是否包含key
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)  # 给key赋值value （将value的值赋给key）


class User(_Base):
    """
    用户表
    """
    __tablename__ = "user"
    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
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

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            # hasattr(self,key) # 是否包含key
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)  # 给key赋值value （将value的值赋给key）


class Cmember(Base):
    """
    部委
    author:lyfy
    :return:[<Cmember:XXX>]
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Cmember:{}>'.format(self.title)


class Local(Base):
    """
    地方
    @author lyfy
    :return:[<Local:XXX>]
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Local:{}>'.format(self.title)


class SocioGroup(Base):
    """
    社会团体
    @author lyfy
    :return:[<SocioGroup:xxx>]
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<SocioGroup:{}>'.format(self.title)


class BaseCity(Base):
    """
    基地
    @author lyfy
    :return:[<BaseCity:xxx>]
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<BaseCity:{}>'.format(self.title)


class Panalysis(_Base):
    """"
    政策分析
    @author lyfy
    :return:[<Panalysis:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    businessId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Panalysis:{}>'.format(self.title)


class Atracking(_Base):
    """"
    活动跟踪
    @author lyfy
    :return:[<Atracking:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    Category = db.Column(db.String(50), unique=True)
    picPath = db.Column(db.String(50), unique=True)
    source = db.Column(db.String(50), unique=True)  # 来源
    publishTime = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Atracking:{}>'.format(self.title)


class Scolumn(_Base):
    """
    专题专栏
    @author lyfy
    :return:[<Scolumn:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Scolumn:{}>'.format(self.title)


class Broadcast(_Base):
    """"
    轮播图
    @author lyfy
    :return:[<Broadcast:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True)
    imagePaths = db.Column(db.String(200), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def __repr__(self):
        return '<Broadcast:{}>'.format(self.title)
