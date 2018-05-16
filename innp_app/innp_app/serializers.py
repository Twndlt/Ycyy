# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-02
import os
from flask import (Flask,request....)
"""
from marshmallow import (Schema as _Schema, fields, validate)

__all__ = ['CmemberSchema', 'LocalSchema', 'SocioGroupSchema', 'LpolicySchema','BaseCitySchema',
           'PanalysisSchema', 'AtrackingSchema', 'ScolumnSchema', 'BroadcastSchema','DongTaiListSchema',
           "ScolumnListSchema","NewDepartureListSchema",'PolicyAnalysisListSchema','ActivitytrackingListSchema',
           'ServiceExpansionSchema']


class Schema(_Schema):
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


class Schema_one(_Schema):
    """
    继承Schema类，创建Schema2类
    author lyfy
    :return:{Id ，title}
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    code = fields.Integer(requeired=True)
    msg = fields.String(requeired=True)


class OmanagementSchema(Schema):
    """
    机构管理
    """
    Onumber = fields.String(validate=validate.Length(6,12), required=True)
    Nauthority = fields.String(required=True)
    Oname = fields.String(required=True)
    Iabbreviation = fields.String(required=True)
    Iaddress = fields.String(required=True)
    Imailbox = fields.String(required=True)
    OWebsite = fields.String(required=True)
    Cnumber = fields.String(required=True)
    Mdescription = fields.String(required=True)


class RmanagementSchema(Schema):
    """
    角色管理
    """
    Rename = fields.String(required=True)
    Rdescription = fields.String(required=True)

class UmanagementSchema(Schema):
    """
    用户管理
    """
    Ainstitutions = fields.String(required=True)
    Theinstitution = fields.String(required=True)
    Uname = fields.String(required=True)
    Rname = fields.String(required=True)
    IDnumber = fields.String(required=True)
    DBirth = fields.String(required=True)
    Sex = fields.String(required=True)
    Mphone = fields.String(required=True)
    Wphone = fields.String(required=True)
    mailbox = fields.String(required=True)
    Wlock = fields.String(required=True)
    Dregistration = fields.String(required=True)


class BPmanagementSchema(Schema):
    """
    banner图片管理
    """
    Name = fields.String(required=True)
    Type = fields.String(required=True)
    link = fields.String(required=True)
    publisher = fields.String(required=True)
    Rtime = fields.DateTime(dump_only=True)
    Modifier = fields.String(required=True)
    Mtime = fields.String(required=True)
    sort = fields.Integer(required=True)
    settop = fields.String(required=True)


class MgroupSchema(Schema):
    """
    创业群体维护
    """
    Negroup = fields.String(required=True)
    Aperson = fields.String(required=True)
    Atime = fields.String(required=True)
    Modifier = fields.String(required=True)
    Mtime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    settop = fields.String(required=True)


class DmanagementSchema(Schema):
    """
    动态管理
    """
    title = fields.String(required=True)
    bintroduction = fields.String(required=True)
    Runit = fields.String(required=True)
    Rtime = fields.DateTime(required=True,dump_only=True)
    Ctime = fields.DateTime(dump_only=True)
    sort = fields.Integer(required=True)
    Rlogo = fields.String(required=True)
    settop = fields.String(required=True)
    Lmarkers = fields.String(required=True)


class PromanagementSchema(Schema):
    """
    宣传位管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    describe = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)


class FmanagementSchema(Schema):
    """
    金融资讯管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)


class bmanagementSchema(Schema):
    """
    金融机构管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    Route = fields.String(required=True)
    sort = fields.String(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)

class TmanagementShema(Schema):
    """
    技术资讯管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)

class MinstitutionsSchema(Schema):
    """
    技术机构管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    Route = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)


class TimanagementSchema(Schema):
    """
    人才资讯管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)


class TamanagementSchema(Schema):
    """
    人才机构管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    Route = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)

class SitemanagementSchema(Schema):
    """
    场地资讯管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)

class positionmanagementSchema(Schema):
    """
    宣传位管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    Route = fields.String(required=True)
    Insertuser = fields.String(required=True)
    Insertiontime = fields.DateTime(dump_only=True)
    Updateuser = fields.String(required=True)
    utime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    settop = fields.String(required=True)

class AmanagementSchema(Schema):
    """
    成果展示管理
    """
    title = fields.String(required=True)
    Rtime = fields.DateTime(required=True)
    Ctime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    Rlogo = fields.String(required=True)
    settop = fields.String(required=True)

class MediamanageSchema(Schema):
    """
    媒体管理
    """
    meidaName = fields.String(required=True)
    businessType = fields.String(required=True)
    mediaType = fields.String(required=True)
    href = fields.String(required=True)
    top = fields.String(required=True)

class ActivityManageSchema(Schema):
    """
    活动管理
    """
    activityTitle = fields.String(required=True)
    activityType = fields.String(required=True)
    area = fields.String(required=True)
    activity = fields.String(required=True)
    releaseUnit = fields.String(required=True)
    releasePeople = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    source = fields.String(required=True)
    mkdirTime = fields.DateTime(required=True)
    modifier = fields.String(required=True)
    modifyTime = fields.DateTime(required=True)

class MascotSchema(Schema):
    """
    吉祥物管理
    """
    title = fields.String(required=True)
    intro = fields.String(required=True)
    releasePeople = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    mkdirTime = fields.DateTime(required=True)
    modifier = fields.String(required=True)
    modifyTime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    top = fields.String(required=True)
    releaseNote = fields.String(required=True)

class GuestSchema(Schema):
    """
    嘉宾管理
    """
    title = fields.String(required=True)
    activityType = fields.String(required=True)
    publisher = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    mkdirTime = fields.DateTime(required=True)
    modifier = fields.String(required=True)
    modifyTime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    top = fields.String(required=True)
    releaseNote = fields.String(required=True)

class HallSchema(Schema):
    """
    展厅管理
    """
    title = fields.String(required=True)
    intro = fields.String(required=True)
    releasePeople = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    mkdirTime = fields.DateTime(required=True)
    modifier = fields.String(required=True)
    modifyTime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    top = fields.String(required=True)
    releaseNote = fields.String(required=True)

class ActivityTypeSchema(Schema):
    """
    活动类别管理
    """
    activityTitle = fields.String(required=True)
    activityType = fields.String(required=True)
    activityIntro = fields.String(required=True)
    releasePeople = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    modifier = fields.String(required=True)
    updateTime = fields.DateTime(required=True)
    status = fields.String(required=True)
    pageView = fields.Integer(required=True)
    href = fields.String(required=True)



class CmemberSchema(Schema):
    """
    部委
    author:lyfy
    :return:Id ， imagePaths，title，insertTime，pubtime，shortContent，source
    """
    data = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)


class LocalSchema(Schema):
    """
    地方
    author:lyfy
    :return:Id，imagePaths，insertTime，pubtime，shortContent,source,title
    """
    data = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)


class SocioGroupSchema(Schema):
    """
    社会团体
    author:lyfy
    :return:Id,imagePaths,insertTime,pubtime,shortContent,source,title
    """
    data = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)


class BaseCitySchema(Schema):
    """
    基地
    author:lyfy
    :return:Id，imagePaths，insertTime，pubtime，shortContent，source，title
    """
    data = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)


class LpolicySchema(Schema_one):
    """
    最新政策
    author:lyfy
    :return:Id，pubTime，shortContent，source，titile
    """
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(required=True)
    source = fields.String(required=True)
    issuedtime = fields.DateTime(dump_only=True)
    issuedno = fields.String(required=True)
    type1 = fields.Integer(required=True)
    link= fields.String(required=True)
    data = fields.Nested('self',only=['id','title','pubtime','shortContent','issuedtime','issuedno','type1','link'],many=True)


class PanalysisSchema(_Schema):
    """
    政策分析
    author:lyfy
    :return:businessId，title
    """
    businessId = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    type = fields.Integer(required=True)
    code = fields.Integer(requeired=True)
    msg = fields.String(requeired=True)
    # data = fields.Nested('self', only=["businessId", "title", "type"], many=True)
    data = fields.Nested("self",only=["businessId","title","type"],many=True)


class AtrackingSchema(Schema_one):
    """
    活动跟踪
    author:lyfy
    :return:Category，id，picPath，publishTime，source，title
    """
    # picPath = fields.String(validate=validate.Length(6, 12), required=True)
    # publishTime = fields.DateTime(dump_only=True)
    # source = fields.String(validate=validate.Length(6, 12), required=True)
    # category = fields.String(validate=validate.Length(6, 12), required=True)

    data = fields.Nested('self', only=["id", "title", "picPath", "publishTime", "source","category"],many=True)


class ScolumnSchema(Schema_one):
    """
    专题专栏
    author:lyfy
    :return:Id，title
    """
    type = fields.Integer(required=True)
    category = fields.Integer(required=True)
    data = fields.Nested('self', only=["id", "title","type","category"], many=True)


class BroadcastSchema(Schema_one):
    """"
    轮播图
    author:lyfy
    :return:Id，title，imagepaths
    """
    imagePaths = fields.String(validate=validate.Length(6, 12), required=True)
    data = fields.Nested('self', only=["id", "title", "imagePaths"], many=True)


class DongTaiListDataSchema(_Schema):
    data = fields.String(required=True)
    allCounts = fields.Integer(dump_only=True)
    currentPage = fields.Integer(dump_only=True)
    # list = fields.List(fields.Field())
    list = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)
    pageCounts = fields.Integer(dump_only=True)
    pageSize = fields.Integer(dump_only=True)


class DongTaiListSchema(Schema):
    """
    动态列表
    author:lyfy
    :return:Id ， imagePaths，title，insertTime，pubtime，shortContent，source
    """
    # data = fields.Nested('self',only={"id","imagePaths","title","insertTime","pubtime","shortContent","source"},many=True)
    data = fields.Nested(DongTaiListDataSchema())


class AllNewGaiListDataSchema(Schema_one):
    data = fields.String(required=True)
    allCounts = fields.Integer(dump_only=True)
    currentPage = fields.Integer(dump_only=True)
    # list = fields.List(fields.Field())
    list = fields.Nested('self', only=["id", "title", "category","type"],
                         many=True)
    pageCounts = fields.Integer(dump_only=True)
    pageSize = fields.Integer(dump_only=True)


class ScolumnListSchema(Schema):
    """"
    专题专栏列表
    author:lyfy
    :return:Id，title,category,pubTime
    """
    data = fields.Nested(AllNewGaiListDataSchema())


class NewDepartureListDataSchema(_Schema):
    data = fields.String(required=True)
    allCounts = fields.Integer(dump_only=True)
    currentPage = fields.Integer(dump_only=True)
    list = fields.Nested('self', only=["id", "title",  "pubtime", "shortContent", "source","issuedno","issuedtime","link"],
                         many=True)
    pageCounts = fields.Integer(dump_only=True)
    pageSize = fields.Integer(dump_only=True)


class NewDepartureListSchema(Schema_one):
    """"
    最新政策列表
    author:lyfy
    :return:Id，title,category,pubTime
    """
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)
    data = fields.Nested(NewDepartureListDataSchema())


class PolicyAnalysisListSchema(Schema_one):
    """"
    政策分析列表
    author:lyfy
    :return:Id，title,category,pubTime
    """
    data = fields.Nested('self', only=["businessId", "title"],many=True)


class ActivitytrackingListSchema(Schema_one):
    """"
    政策分析列表
    author:lyfy
    :return:Id，title,category,pubTime
    """
    data = fields.Nested('self', only=["id", "title", "picPath", "publishTime", "source","category"],many=True)


class ServiceExpansionSchema(Schema_one):
    """
    服务拓展列表
    @author:lyfy
    :return:
    """
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)
    data = fields.Nested('self',only=['id','title','pubtime','shortContent','source'],many=True)