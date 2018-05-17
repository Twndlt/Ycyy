# -*- coding: utf-8 -*-
from datetime import datetime
from contextlib import contextmanager

# import integer as Integer
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
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    imagePaths = db.Column(db.String(50), unique=True, doc="项目图片地址")
    title = db.Column(db.String(50), unique=True, nullable=True, doc="标题")
    insertTime = db.Column(db.DateTime, default=datetime.utcnow, doc="时间")
    pubtime = db.Column(db.DateTime, default=datetime.utcnow, doc="发布时间")
    shortContent = db.Column(db.Text, nullable=True, doc="文章内容")
    source = db.Column(db.String(255), unique=True, nullable=True, doc="文章来源")  # 来源

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

    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    username = db.Column(db.String(40), unique=True, nullable=False, doc="用户名")
    email = db.Column(db.String(40), unique=True, nullable=False, doc="邮箱")
    phone = db.Column(db.Integer, doc="电话号码")
    resume_url = db.String(db.String(255))
    _password = db.Column('password', db.String(256), nullable=False, doc="密码")
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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<Cmember:{}>'.format(self.title)


class Local(Base):
    """
    地方
    @author lyfy
    :return:[<Local:XXX>]
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<Local:{}>'.format(self.title)


class SocioGroup(Base):
    """
    社会团体
    @author lyfy
    :return:[<SocioGroup:xxx>]
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<SocioGroup:{}>'.format(self.title)


class BaseCity(Base):
    """
    基地
    @author lyfy
    :return:[<BaseCity:xxx>]
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<BaseCity:{}>'.format(self.title)


class Panalysis(_Base):
    """"
    政策分析
    @author lyfy
    :return:[<Panalysis:xxx>]
    """
    businessId = db.Column(db.Integer, primary_key=True, doc="id")
    title = db.Column(db.String(50), unique=True, nullable=False, doc="标题")
    type = db.Column(db.Integer, doc="type状态码")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<Panalysis:{}>'.format(self.title)


class Atracking(_Base):
    """"
    活动跟踪
    @author lyfy
    :return:[<Atracking:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(50), unique=True, doc="文章标题")
    category = db.Column(db.String(50), unique=True, doc="cate状态码")
    picPath = db.Column(db.String(50), unique=True, doc="图片地址")
    source = db.Column(db.String(50), unique=True, doc="文章来源")  # 来源
    publishTime = db.Column(db.DateTime, default=datetime.utcnow, doc="发布时间")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<Atracking:{}>'.format(self.title)


class Scolumn(_Base):
    """
    专题专栏
    @author lyfy
    :return:[<Scolumn:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(50), unique=True, doc="文章标题")
    type = db.Column(db.Integer, doc="type状态码")
    category = db.Column(db.Integer, doc="category状态码")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<Scolumn:{}>'.format(self.title)


class Broadcast(_Base):
    """"
    轮播图
    @author lyfy
    :return:[<Broadcast:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(50), unique=True, doc="文章标题")
    imagePaths = db.Column(db.String(200), unique=True, doc="图片地址")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<Broadcast:{}>'.format(self.title)


class Lpolicy(_Base):
    """"
    最新政策
    @author lyfy
    :return:[<Lpolicy:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(50), unique=True, nullable=True, doc="文章标题")
    pubtime = db.Column(db.DateTime, default=datetime.utcnow, doc="发布时间")
    shortContent = db.Column(db.Text, doc="文章正文")
    source = db.Column(db.String(255), doc="文章来源")  # 来源
    issuedno = db.Column(db.String(50))  # 发改运行〔xxx〕xxx号
    issuedtime = db.Column(db.DateTime, default=datetime.utcnow)
    link = db.Column(db.String(255))  # 不知名网址
    type = db.Column(db.Integer, doc="type状态码")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="引用外键")  # 外键

    def __repr__(self):
        return '<Lpolicy:{}>'.format(self.title)


class ServiceExpansion(_Base):
    """
    服务拓展
    @author:lyfy
    :return:
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(50), unique=True, doc="文章标题")
    pubtime = db.Column(db.DateTime, default=datetime.utcnow, doc="发布时间")
    shortContent = db.Column(db.String(255), doc="正文内容")
    source = db.Column(db.String(255), doc="文章来源")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="引用外键")

    def __repr__(self):
        return '<ServiceExpansion:{}>'.format(self.title)


# ↓↓↓↓↓↓后台表

class omanagement(_Base):
    """
    机构管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Onumber = db.Column(db.String(30), doc="机构编码")
    Nauthority = db.Column(db.String(30), doc="上级机构名称")
    Oname = db.Column(db.String(30), doc="机构名称")
    Iabbreviation = db.Column(db.String(30), doc="机构简称")
    Iaddress = db.Column(db.String(30), doc="机构地址")
    Imailbox = db.Column(db.String(30), doc="机构邮箱")
    OWebsite = db.Column(db.String(30), doc="机构官网")
    Cnumber = db.Column(db.String(30), doc="联系电话")
    Mdescription = db.Column(db.String(100), doc="机构描述")

    def __repr__(self):
        return '<omanagement>:{}'.format(self.title)


class Rmanagement(_Base):
    """
    角色管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Rename = db.Column(db.String(30), doc="角色名称")
    Rdescription = db.Column(db.String(100), doc="角色描述")

    def __repr__(self):
        return '<Rmanagement>:{}'.format(self.title)


class umanagement(_Base):
    """
    用户管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Ainstitutions = db.Column(db.String(30), doc="所属机构")
    Theinstitution = db.Column(db.String(30), doc="所属机构简称")
    Uname = db.Column(db.String(30), doc="用户名")
    Rname = db.Column(db.String(30), doc="真实姓名")
    IDnumber = db.Column(db.String(30), doc="身份证号")
    DBirth = db.Column(db.String(30), doc="出生日期")
    Sex = db.Column(db.String(30), doc="性别")
    Mphone = db.Column(db.String(30), doc="手机")
    Wphone = db.Column(db.String(30), doc="工作电话")
    mailbox = db.Column(db.String(30), doc="邮箱")
    Wlock = db.Column(db.String(20), doc="是否锁定")
    Dregistration = db.Column(db.String(30), doc="注册日期")

    def __repr__(self):
        return '<umanagement>:{}'.format(self.title)


class BPmanagement(_Base):
    """
    banner图片管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Name = db.Column(db.String(50), doc="名称")
    Type = db.Column(db.String(30), doc="类型")
    link = db.Column(db.String(50), doc="链接")
    publisher = db.Column(db.String(30), doc="发布人")
    Rtime = db.Column(db.Date(), doc="发布时间")
    Modifier = db.Column(db.String(30), doc="修改人")
    Mtime = db.Column(db.Date(), doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")
    settop = db.Column(db.String(30), doc="置顶")

    def __repr__(self):
        return '<BPmanagement>:{}'.format(self.title)


class Mgroup(_Base):
    """\
    创业群体维护
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Negroup = db.Column(db.String(30), doc="创业群体名称")
    Aperson = db.Column(db.String(20), doc="添加人")
    Atime = db.Column(db.Date(), doc="添加时间")
    Modifier = db.Column(db.String(30), doc="修改人")
    Mtime = db.Column(db.Date(), doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")
    settop = db.Column(db.String(30), doc="置顶")

    def __repr__(self):
        return '<Mgroup>:{}'.format(self.title)


class Dmanagement(_Base):
    """
    动态管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(30), doc="标题")
    bintroduction = db.Column(db.String(100), doc="简介")
    Runit = db.Column(db.String(30), doc="发布单位")
    Rtime = db.Column(db.Date(), doc="发布时间")
    Ctime = db.Column(db.Date(), doc="创建时间")
    sort = db.Column(db.Integer, doc="排序")
    Rlogo = db.Column(db.String(40), doc="发布标识")
    settop = db.Column(db.String(20), doc="置顶")
    Lmarkers = db.Column(db.String(30), doc="领导标记")

    def __repr__(self):
        return '<Dmanagement>:{}'.format(self.title)


class Promanagement(_Base):
    """
    宣传位管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Name = db.Column(db.String(20), doc="名称")
    link = db.Column(db.String(50), doc="链接")
    describe = db.Column(db.String(100), doc="描述")
    sort = db.Column(db.Integer, doc="排序")
    category = db.Column(db.String(30), doc="类别")
    settop = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<Promanagement>:{}'.format(self.title)


class Fmanagement(_Base):
    """
    金融资讯管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Name = db.Column(db.String(20), doc="名称")
    link = db.Column(db.String(50), doc="链接")
    sort = db.Column(db.Integer, doc="排序")
    category = db.Column(db.String(30), doc="类别")
    settop = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<Fmanagement>:{}'.format(self.title)


class bmanagement(_Base):
    """
    金融机构管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Name = db.Column(db.String(20), doc="名称")
    link = db.Column(db.String(50), doc="链接")
    Route = db.Column(db.String(50), doc="路径")
    sort = db.Column(db.Integer, doc="排序")
    category = db.Column(db.String(30), doc="类别")
    settop = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<bmanagement>:{}'.format(self.title)


class Tmanagement(_Base):
    """
    技术资讯管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Name = db.Column(db.String(20), doc="名称")
    link = db.Column(db.String(50), doc="链接")
    sort = db.Column(db.Integer, doc="排序")
    category = db.Column(db.String(30), doc="类别")
    settop = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<Tmanagement>:{}'.format(self.title)


class Minstitutions(_Base):
    """
    技术机构管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Name = db.Column(db.String(20), doc="名称")
    link = db.Column(db.String(50), doc="链接")
    Route = db.Column(db.String(50), doc="路径")
    sort = db.Column(db.Integer, doc="排序")
    category = db.Column(db.String(30), doc="类别")
    settop = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<Minstitutions>:{}'.format(self.title)


class Timanagement(_Base):
    """
    人才资讯管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Name = db.Column(db.String(20), doc="名称")
    link = db.Column(db.String(50), doc="链接")
    sort = db.Column(db.Integer, doc="排序")
    category = db.Column(db.String(30), doc="类别")
    settop = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<Timanagement>:{}'.format(self.title)


class Tamanagement(_Base):
    """
    人才机构管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Name = db.Column(db.String(20), doc="名称")
    link = db.Column(db.String(50), doc="链接")
    Route = db.Column(db.String(50), doc="路径")
    sort = db.Column(db.Integer, doc="排序")
    category = db.Column(db.String(30), doc="类别")
    settop = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<Tamanagement>:{}'.format(self.title)


class Sitemanagement(_Base):
    """
    场地资讯管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Name = db.Column(db.String(20), doc="名称")
    link = db.Column(db.String(50), doc="链接")
    sort = db.Column(db.Integer, doc="排序")
    category = db.Column(db.String(30), doc="类别")
    settop = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<Sitemanagement>:{}'.format(self.title)


class siteinstitutions(_Base):
    """
    场地机构管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Name = db.Column(db.String(20), doc="名称")
    link = db.Column(db.String(50), doc="链接")
    Route = db.Column(db.String(50), doc="路径")
    sort = db.Column(db.Integer, doc="排序")
    category = db.Column(db.String(30), doc="类别")
    settop = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<siteinstitutions>:{}'.format(self.title)


class positionmanagement(_Base):
    """
    宣传位管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    Name = db.Column(db.String(20), doc="名称")
    link = db.Column(db.String(50), doc="链接")
    Route = db.Column(db.String(50), doc="路径")
    Insertuser = db.Column(db.String(30), doc="插入用户")
    Insertiontime = db.Column(db.Date(), doc="插入时间")
    Updateuser = db.Column(db.String(30), doc="更新用户")
    utime = db.Column(db.Date(), doc="更新时间")
    sort = db.Column(db.Integer, doc="排序")
    settop = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<positionmanagement>:{}'.format(self.title)


class Amanagement(_Base):
    """
    成果展示管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(30), doc="标题")
    Rtime = db.Column(db.Date(), doc="发布时间")
    Ctime = db.Column(db.Date(), doc="创建时间")
    sort = db.Column(db.Integer, doc="排序")
    Rlogo = db.Column(db.String(20), doc="发布标识")
    settop = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<Amanagement>:{}'.format(self.title)


class Mediamanage(_Base):
    """
    媒体管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    meidaName = db.Column(db.String(50), doc='媒体名称')
    businessType = db.Column(db.String(30), doc='业务类型')
    mediaType = db.Column(db.String(20), doc='媒体类型')
    href = db.Column(db.String(100), doc="链接")
    top = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<Mediamanage>:{}'.format(self.title)


class ActivityManage(_Base):
    """
    活动管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    activityTitle = db.Column(db.String(50), doc="活动标题")
    activityType = db.Column(db.String(30), doc="活动种类")
    area = db.Column(db.String(20), doc="所属区域")
    activity = db.Column(db.String(130), doc="活动简介")
    releaseUnit = db.Column(db.String(30), doc="发布单位")
    releasePeople = db.Column(db.String(20), doc="发布人")
    releaseTime = db.Column(db.Date(), doc="发布时间")
    source = db.Column(db.String(30), doc="来源")
    mkdirTime = db.Column(db.Date(), doc="创建时间")
    modifier = db.Column(db.String(20), doc="修改人")
    modifyTime = db.Column(db.Date(), doc="修改时间")

    def __repr__(self):
        return '<ActivityManage>:{}'.format(self.title)


class Mascot(_Base):
    """
    吉祥物管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(50), doc="标题")
    intro = db.Column(db.String(30), doc="简介")
    releasePeople = db.Column(db.String(30), doc="发布人")
    releaseTime = db.Column(db.Date(), doc="发布时间")
    mkdirTime = db.Column(db.Date(), doc="创建时间")
    modifier = db.Column(db.String(30), doc="修改人")
    modifyTime = db.Column(db.Date(), doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")
    top = db.Column(db.String(20), doc="置顶")
    releaseNote = db.Column(db.String(20), doc="发布标识")

    def __repr__(self):
        return '<Mascot>:{}'.format(self.title)


class Guest(_Base):
    """
    嘉宾管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(50), doc="标题")
    activityType = db.Column(db.String(50), doc="活动类别")
    publisher = db.Column(db.String(30), doc="发布人")
    releaseTime = db.Column(db.Date(), doc="发布时间")
    mkdirTime = db.Column(db.Date(), doc="创建时间")
    modifier = db.Column(db.String(20), doc="修改人")
    modifyTime = db.Column(db.Date(), doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")
    top = db.Column(db.String(20), doc="置顶")
    releaseNote = db.Column(db.String(30), doc="发布标识")

    def __repr__(self):
        return '<Guest>:{}'.format(self.title)


class Hall(_Base):
    """
    展厅管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(40), doc="标题")
    intro = db.Column(db.String(100), doc="简介")
    releasePeople = db.Column(db.String(20), doc="发布人")
    releaseTime = db.Column(db.Date(), doc="发布时间")
    mkdirTime = db.Column(db.Date(), doc="创建时间")
    modifier = db.Column(db.String(20), doc="修改人")
    modifyTime = db.Column(db.Date(), doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")
    top = db.Column(db.String(20), doc="置顶")
    releaseNote = db.Column(db.String(20), doc="发布标识")

    def __repr__(self):
        return '<Hall>:{}'.format(self.title)


class ActivityType(_Base):
    """
    活动类别管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    activityTitle = db.Column(db.String(50), doc="活动标题")
    activityType = db.Column(db.String(30), doc="活动类别")
    activityIntro = db.Column(db.String(100), doc="活动简介")
    releasePeople = db.Column(db.String(30), doc="发布人")
    releaseTime = db.Column(db.Date(), doc="发布时间")
    modifier = db.Column(db.String(30), doc="更新人")
    updateTime = db.Column(db.Date(), doc="更新时间")
    status = db.Column(db.String(20), doc="已启用")
    pageView = db.Column(db.Integer, doc="页面浏览量")
    href = db.Column(db.String(100), doc="参与方式跳转链接")

    def __repr__(self):
        return '<ActivityType>:{}'.format(self.title)


class CenterNew(_Base):
    """
    中央快讯
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(50), doc="标题")
    intro = db.Column(db.String(100), doc="简介")
    releaseTime = db.Column(db.Date(), doc="发布时间")
    mkdirTime = db.Column(db.Date(), doc="创建时间")
    modifyTime = db.Column(db.Date(), doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")
    releaseNote = db.Column(db.String(30), doc="发布标识")
    top = db.Column(db.String(30), doc="置顶")
    source = db.Column(db.String(30), doc="来源")

    def __repr__(self):
        return '<CenterNew>:{}'.format(self.title)


class LocalNew(_Base):
    """
    地方报道
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(50), doc="标题")
    intro = db.Column(db.String(100), doc="简介")
    releaseTime = db.Column(db.Date(), doc="发布时间")
    mkdirTime = db.Column(db.Date(), doc="创建时间")
    modifyTime = db.Column(db.Date(), doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")
    releaseNote = db.Column(db.String(30), doc="发布标识")
    top = db.Column(db.String(30), doc="置顶")
    source = db.Column(db.String(30), doc="来源")

    def __repr__(self):
        return '<LocalNew>:{}'.format(self.title)


class Department(_Base):
    """
    部委讯息
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(50), doc="标题")
    intro = db.Column(db.String(100), doc="简介")
    releaseTime = db.Column(db.Date(), doc="发布时间")
    mkdirTime = db.Column(db.Date(), doc="创建时间")
    modifyTime = db.Column(db.Date(), doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")
    releaseNote = db.Column(db.String(30), doc="发布标识")
    top = db.Column(db.String(30), doc="置顶")
    source = db.Column(db.String(30), doc="来源")

    def __repr__(self):
        return '<Department>:{}'.format(self.title)


class policy(_Base):
    """
    政策讯息
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(50), doc="标题")
    intro = db.Column(db.String(100), doc="简介")
    releaseTime = db.Column(db.Date(), doc="发布时间")
    mkdirTime = db.Column(db.Date(), doc="创建时间")
    modifyTime = db.Column(db.Date(), doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")
    releaseNote = db.Column(db.String(30), doc="发布标识")
    top = db.Column(db.String(30), doc="置顶")
    source = db.Column(db.String(30), doc="来源")

    def __repr__(self):
        return '<policy>:{}'.format(self.title)


class LocalReport(_Base):
    """
    地方报道
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(50), doc="标题")
    intro = db.Column(db.String(100), doc="简介")
    releaseTime = db.Column(db.Date(), doc="发布时间")
    sort = db.Column(db.Integer, doc="排序")
    top = db.Column(db.String(30), doc="置顶")
    releaseNote = db.Column(db.String(30), doc="发布标识")

    def __repr__(self):
        return '<LocalReport>:{}'.format(self.title)


class PolicyRelease(_Base):
    """
    政策发布
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(50), unique=True, doc="文章标题")
    number = db.Column(db.String(50), primary_key=True, unique=True, doc="文号")
    organization = db.Column(db.String(30), doc="发布机构")
    publisher = db.Column(db.String(30), doc="发布人")
    releaseTime = db.Column(db.Date(), doc="发布时间")
    modifyTime = db.Column(db.Date(), doc="修改时间")
    policyTheme = db.Column(db.String(30), doc="政策主题")
    animalKeyword = db.Column(db.String(30), doc="生态圈关键字")
    timerShaft = db.Column(db.String(30), doc="时间轴阶段")
    policyBelong = db.Column(db.String(30), doc="政策隶属")
    area = db.Column(db.String(30), doc="区域")
    businessPeople = db.Column(db.String(50), doc="创业人群")
    businessService = db.Column(db.String(50), doc="创业服务")
    profession = db.Column(db.String(30), doc="行业")
    policySort = db.Column(db.Integer, doc="政策排序")
    policyTop = db.Column(db.String(20), doc="政策置顶")
    releaseFlag = db.Column(db.String(20), doc="发布标识")

    def __repr__(self):
        return '<PolicyRelease>:{}'.format(self.title)


class ecosphere(_Base):
    """
    生态圈维护
    """
    id = db.Column(db.Integer, primary_key=True, doc="生态圈id")
    ecosphereName = db.Column(db.String(30), doc="生态圈名称")

    def __repr__(self):
        return '<ecosphere>:{}'.format(self.title)


class TimerShaft(_Base):
    """
    时间轴维护
    """
    id = db.Column(db.Integer, primary_key=True, doc="时间轴id")
    timerShaftName = db.Column(db.String(30), doc="时间轴名称")

    def __repr__(self):
        return '<TimerShaft>:{}'.format(self.title)


class BusinessService(_Base):
    """
    行业数据维护
    """
    id = db.Column(db.Integer, primary_key=True, doc="行业id")
    businessName = db.Column(db.String(30), doc="行业名称")

    def __repr__(self):
        return '<BusinessService>:{}'.format(self.title)


class AreaService(_Base):
    """
    区域数据维护
    """
    id = db.Column(db.Integer, primary_key=True, doc="区域id")
    areaName = db.Column(db.String(30), doc="区域名称")

    def __repr__(self):
        return '<AreaService>:{}'.format(self.title)


class SubjectClassification(_Base):
    """
    主题分类
    """
    id = db.Column(db.Integer, primary_key=True, doc="主题分类id")
    SubjectName = db.Column(db.String(30), doc="主题分类名称")

    def __repr__(self):
        return '<SubjectClassification>:{}'.format(self.title)


class PolicyClassify(_Base):
    """
    政策分类
    """
    id = db.Column(db.Integer, primary_key=True, doc="政策分类Id")
    policyName = db.Column(db.String(30), doc="政策分类名称")

    def __repr__(self):
        return '<PolicyClassify>:{}'.format(self.title)


class IndustrialPark(_Base):
    """
    产业园推荐
    """
    id = db.Column(db.Integer, primary_key=True, doc="产业园区id")
    industrialName = db.Column(db.String(30), doc="名称")
    href = db.Column(db.String(70), doc="链接")
    sort = db.Column(db.Integer, doc="排序")
    top = db.Column(db.String(30), doc="置顶")

    def __repr__(self):
        return '<PolicyClassify>:{}'.format(self.title)


class BaseManage(_Base):
    """
    示范基地管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    baseName = db.Column(db.String(50), unique=True, doc="基地名称")
    baseStyle = db.Column(db.String(30), doc="基地类型")
    baseBatc = db.Column(db.String(20), doc="基地批次")
    area = db.Column(db.String(20), doc="区域")
    policyUnit = db.Column(db.String(30), doc="发布单位")
    creator = db.Column(db.String(20), doc="创建人")
    createTime = db.Column(db.Date(), doc="创建时间")
    modifier = db.Column(db.String(30), doc="修改人")
    modifyTime = db.Column(db.Date(), doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")
    top = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<BaseManage>:{}'.format(self.title)


class UserBrowsingMessage(_Base):
    """
    用户浏览信息
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    userIp = db.Column(db.String(30), unique=True, doc="用户ip")
    bussinessType = db.Column(db.String(20), doc="业务类型")
    userType = db.Column(db.String(30), doc="用户类型")
    systemEnvironment = db.Column(db.String(30), doc="系统环境")
    customerPremise = db.Column(db.String(20), doc="用户所在地")
    userSystem = db.Column(db.String(20), doc="用户使用系统")
    userMachineCode = db.Column(db.String(20), doc="用户机器码")
    userBrowsingTime = db.Column(db.Date(), doc="用户浏览时长")
    userInformationClassification = db.Column(db.String(20), doc="用户信息分类")

    def __repr__(self):
        return '<UserBrowsingMessage>:{}'.format(self.title)


class UserSearchInfo(_Base):
    """
    用户搜索信息
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    userIp = db.Column(db.String(50), doc="用户Ip")
    userLocation = db.Column(db.String(70), doc="用户所在地")
    userSystem = db.Column(db.String(30), doc="用户使用系统")
    userMachineCode = db.Column(db.String(50), doc="用户机器码")
    userSearchContent = db.Column(db.String(50), doc="用户查询内容")
    userSearchMethod = db.Column(db.String(30), doc="用户查询方式")
    userSearchCondition = db.Column(db.String(50), doc="用户查询条件")
    searchPageClassify = db.Column(db.String(50), doc="搜索页面分类")
    userType = db.Column(db.String(30), doc="用户类型")

    def __repr__(self):
        return '<UserSearchInfo>:{}'.format(self.title)


class PilotManagement(_Base):
    """
    试验区管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    pilotName = db.Column(db.String(30), unique=True, doc="试验区名称")
    creator = db.Column(db.String(30), doc="创建人")
    createTime = db.Column(db.Date(), doc="创建时间")
    modifier = db.Column(db.String(30), doc="修改人")
    modifyTime = db.Column(db.Date(), doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")
    top = db.Column(db.String(20), doc="置顶")

    def __repr__(self):
        return '<PilotManagement>:{}'.format(self.title)


class PolicyStatistics(_Base):
    """
    政策统计
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(255), doc="政策标题")
    issuednumber = db.Column(db.String(255), doc="发文字号")
    company = db.Column(db.String(255), doc="颁布单位")
    time = db.Column(db.String(255), doc="颁布时间")
    policyaccess = db.Column(db.String(255), doc="政策访问量")

    def __repr__(self):
        return '<PolicyStatistics:{}>'.format(self.title)


class JournalSystem(_Base):
    """
    日志管理-系统日志管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    modulename = db.Column(db.String(255), doc="模块名称")
    operationtype = db.Column(db.String(255), doc="操作类型")
    describe = db.Column(db.String(255), doc="描述")
    result = db.Column(db.String(255), doc="结果")
    operator = db.Column(db.String(255), doc="操作人")
    ip = db.Column(db.String(255), doc="IP")
    operationdate = db.Column(db.String(255), doc="操作日期")
    creationtime = db.Column(db.DateTime, default=datetime.utcnow, doc="创建时间")

    def __repr__(self):
        return '<JournalSystem:{}>'.format(self.title)


class JournalPolicy(_Base):
    """
    日志管理-政策日志管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    visiting = db.Column(db.String(255), unique=True, doc="受访政策")
    visitorip = db.Column(db.String(255), doc="访问者ip")
    country = db.Column(db.String(255), doc="访问者国家")
    area = db.Column(db.String(255), doc="访问者地区")
    province = db.Column(db.String(255), doc="访问者省份")
    city = db.Column(db.String(255), doc="访问者市")
    district = db.Column(db.String(255), doc="访问者县/区")
    operator = db.Column(db.String(255), doc="运营商")
    type = db.Column(db.String(255), doc="终端类型")
    describe = db.Column(db.String(255), doc="操作描述")
    time = db.Column(db.DateTime, default=datetime.utcnow, doc="记录时间")

    def __repr__(self):
        return '<JournalPolicy:{}>'.format(self.title)


class AboutUs(_Base):
    """
    关于我们
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    firsttitle = db.Column(db.String(255), doc="第一标题")
    firstcontent = db.Column(db.String(255), doc="第一内容")
    secondtitle = db.Column(db.String(255), doc="第二标题")
    secondcontent = db.Column(db.String(255), doc="第二内容")

    def __repr__(self):
        return '<AboutUs:{}>'.format(self.title)


class MovePresentation(_Base):
    """
    移动端功能管理-报告管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(255), unique=True, doc="服务标题")
    description = db.Column(db.String(255), doc="简介")
    company = db.Column(db.String(255), doc="发布单位")
    publisher = db.Column(db.String(255), doc="发布人")
    publishtime = db.Column(db.DateTime, default=datetime.utcnow, doc="发布时间")
    creationtime = db.Column(db.DateTime, default=datetime.utcnow, doc="创建时间")
    modifier = db.Column(db.DateTime, default=datetime.utcnow, doc="修改人")
    mtime = db.Column(db.DateTime, default=datetime.utcnow, doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")
    releaselogo = db.Column(db.String(255), doc="发布标识")

    def __repr__(self):
        return '<MovePresentation:{}>'.format(self.title)


class MoveService(_Base):
    """
    移动端功能管理-服务管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(255), unique=True, doc="服务标题")
    description = db.Column(db.String(255), doc="简介")
    founder = db.Column(db.String(255), doc="创建人")
    creationtime = db.Column(db.DateTime, default=datetime.utcnow, doc="创建时间")
    modifier = db.Column(db.DateTime, default=datetime.utcnow, doc="修改人")
    mtime = db.Column(db.DateTime, default=datetime.utcnow, doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")

    def __repr__(self):
        return '<MoveService:{}>'.format(self.title)


class MoveHomePage(_Base):
    """
    移动端功能管理-活动首页管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(255), unique=True, doc="标题")
    description = db.Column(db.String(255), doc="简介")
    founder = db.Column(db.String(255), doc="创建人")
    creationtime = db.Column(db.DateTime, default=datetime.utcnow, doc="创建时间")
    modifier = db.Column(db.DateTime, default=datetime.utcnow, doc="修改人")
    mtime = db.Column(db.DateTime, default=datetime.utcnow, doc="修改时间")
    sort = db.Column(db.Integer, doc="排序")

    def __repr__(self):
        return '<MoveHomePage:{}>'.format(self.title)


class MoveVersion(_Base):
    """
    移动端功能管理-版本管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    number = db.Column(db.String(255), unique=True, doc="版本号")
    information = db.Column(db.String(255), unique=True, doc="版本信息")
    classification = db.Column(db.String(255), unique=True, doc="分类")
    compulsoryrenewal = db.Column(db.String(255), unique=True, doc="强制更新")
    founder = db.Column(db.String(255), doc="创建人")
    creationtime = db.Column(db.DateTime, default=datetime.utcnow, doc="创建时间")
    modifier = db.Column(db.DateTime, default=datetime.utcnow, doc="修改人")
    mtime = db.Column(db.DateTime, default=datetime.utcnow, doc="修改时间")

    def __repr__(self):
        return '<MoveVersion:{}>'.format(self.title)


class MoveUser(_Base):
    """
    移动端功能管理-用户管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    phone = db.Column(db.Integer, doc="手机号")
    user = db.Column(db.String(255), unique=True, doc="用户名")
    model = db.Column(db.String(255), unique=True, doc="机型")
    time = db.Column(db.DateTime, default=datetime.utcnow, doc="注册时间")
    logintime = db.Column(db.DateTime, default=datetime.utcnow, doc="最近登录时间")

    def __repr__(self):
        return '<MoveUser:{}>'.format(self.title)


class MoveBriefing(_Base):
    """
    移动端功能管理-简报管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(255), unique=True, doc="标题")
    time = db.Column(db.DateTime, default=datetime.utcnow, doc="维护时间")
    releaselogo = db.Column(db.String(255), doc="发布标识")

    def __repr__(self):
        return '<MoveBriefing:{}>'.format(self.title)


class GuideToAffairs(_Base):
    """
    服务拓展--办事指南管理
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(255), unique=True, doc="标题")
    description = db.Column(db.String(255), doc="简介")
    source = db.Column(db.String(255), doc="来源")
    publishtime = db.Column(db.DateTime, default=datetime.utcnow, doc="发布时间")
    creationtime = db.Column(db.DateTime, default=datetime.utcnow, doc="创建时间")
    founder = db.Column(db.String(255), doc="创建人")
    renewing = db.Column(db.String(255), doc="更新人")
    updatatime = db.Column(db.DateTime, doc="更新时间")
    releaselogo = db.Column(db.String(255), doc="发布标识")

    def __repr__(self):
        return '<GuideToAffairs:{}>'.format(self.title)


class GovernmentFunds(_Base):
    """
    服务拓展--政府性基金和行政事业型收费
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(255), unique=True, doc="文章标题")
    costcategory = db.Column(db.String(255), doc="费用类别")
    publisher = db.Column(db.String(255), doc="发布人")
    publishtime = db.Column(db.DateTime, default=datetime.utcnow, doc="发布时间")
    renewing = db.Column(db.String(255), doc="更新人")
    updatatime = db.Column(db.DateTime, doc="更新时间")
    releaselogo = db.Column(db.String(255), doc="发布标识")

    def __repr__(self):
        return '<GovernmentFunds:{}>'.format(self.title)


class FavouredPolicy(_Base):
    """
    服务拓展--双创税收优惠政策查询
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(255), unique=True, doc="税收标题")
    taxstage = db.Column(db.String(255), doc="税收阶段")
    taxcategory = db.Column(db.String(255), doc="税收类别")
    publisher = db.Column(db.String(255), doc="发布人")
    publishtime = db.Column(db.DateTime, default=datetime.utcnow, doc="发布时间")
    renewing = db.Column(db.String(255), doc="更新人")
    updatatime = db.Column(db.DateTime, doc="更新时间")
    releaselogo = db.Column(db.String(255), doc="发布标识")

    def __repr__(self):
        return '<FavouredPolicy:{}>'.format(self.title)


class CancellationAndDecentralization(_Base):
    """
    服务拓展--取消和下放的行政事项
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    name = db.Column(db.String(255), unique=True, doc="项目名称")
    itemtype = db.Column(db.String(255), doc="事项类型")
    department = db.Column(db.String(255), doc="部门")
    publisher = db.Column(db.String(255), doc="发布人")
    publishtime = db.Column(db.DateTime, default=datetime.utcnow, doc="发布时间")
    renewing = db.Column(db.String(255), doc="更新人")
    updatatime = db.Column(db.DateTime, doc="更新时间")
    releaselogo = db.Column(db.String(255), doc="发布标识")

    def __repr__(self):
        return '<CancellationAndDecentralization:{}>'.format(self.title)
