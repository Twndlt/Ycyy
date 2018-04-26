from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import (DataRequired,length)
# from douban_book.models import User
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class Book_Login(FlaskForm):
    """
    用户登录
    """
    username = StringField(
        label=u"用户名",
        validators=[
            DataRequired(u"用户名不存在"),
            length(1,20)
        ]
    )
    _password = PasswordField(
        lable=u"密码",
        validators=[
            DataRequired(u"密码错误"),
            length(1,20)
        ]
    )
    remember_me = BooleanField(
        label='记住我'
    )
    submit = SubmitField('登录')

# # 创建对象的基类:
# Base = declarative_base()
# # 定义User对象:
# class User(Base):
#     # 表的名字:
#     __tablename__ = 'demo'
#
#     # 表的结构:
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     password = Column(String(20))
#
#     def validate(self,name,password):
#         """
#         验证账户密码
#         :param name:
#         :param password:
#         :return:
#         """
#         # 初始化数据库连接:
#         engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/industrydatas_ccc?charset=utf8mb4")
#         # 创建DBSession类型:
#         DBSession = sessionmaker(bind=engine)
#         session = DBSession()
#         zt1=1
#         zt2=1
#         # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
#         try:
#             name = session.query(User).filter(User.name==name).one()
#             zt1=0
#         except:
#             zt1 =1
#         try:
#             password = session.query(User).filter(User.password==password).one()
#             if password==password:
#                 zt2 = 0
#         except:
#             zt2 =1
#         if zt1 and zt2:
#             raise ValidationError('用户名或密码错误')
