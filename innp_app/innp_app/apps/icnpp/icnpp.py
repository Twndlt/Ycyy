# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-10
import os
from flask import (Flask,request....)
"""

from flask import request, render_template

from innp_app.models import db, User, Mediamanage, ActivityManage, Mascot, Guest, Hall, ActivityType, CenterNew, \
    LocalNew, Department, policy, LocalReport, PolicyRelease

from innp_app.common.rest import RestView

from innp_app.serializers import MediamanageSchema



class IndexView(RestView):

    def get(self):
        """
        后台显示内容
        ---
        tags:
          - 后台页面
        """
        return "1111"

    def post(self):
        with db.auto_commit():
            user = User()
            user.set_attrs(request.form)
            db.session.add(user)
        return "1111", 200




class MediaView(RestView):
    def AddMedia(self):
        """
        媒体管理，新增媒体请求处理并响应
        author:wpc
        :return:
        """
        with db.auto_commit():
            #ms = Mediamanage('10', '样例测试', '医药', '音频', '10', 'www.baidu.com', '已置顶')
            ma = Mediamanage()
            ma.id = 10
            ma.meidaName = "样例测试"
            ma.bussionessType = "医药"
            ma.mediaType = "音频"
            ma.sort = "10"
            ma.href = "www.baidu.com"
            ma.top = "已置顶"
            db.session.add(ma)
            return "1111", 200

    # def DeleteMedia(self):
    #     """
    #     媒体管理。获取复选框的状态值，删除媒体记录
    #     author:wpc
    #     :return:
    #     """
    #     #option = request.values.getlist("option")
    #     with db.auto_commit(self):
    #         record =Mediamanage.query.filter_by(id="10").all()
    #         db.session.delete(record)


    # def AlterMedia(self):
    #     """
    #     媒体管理，修改媒体记录
    #     author:wpc
    #     :return:
    #     """
    #     with db.auto_commit():
    #         media = Mediamanage.query.first()
    #         media.medianame = request.form.get("mname")
    #         media.bussinessType = request.form.get("btype")
    #         media.mediaType = request.form.get("mtype")
    #         media.sort = request.form.get("sort")
    #         media.href = request.form.get("href")


class ActivityManageView(RestView):
    """
    活动管理
    author:wpc
    """
    def addmanage(self):
        """
        添加活动管理
        author:wpc
        :return:
        """
        with db.auto_commit():
            amanage = ActivityManage()
            amanage.id = 9
            amanage.activityTitle = "事业培训"
            amanage.activityType = "教育"
            amanage.area = "北京"
            amanage.activity = "关于加强事业单位人员工作能力"
            amanage.releaseUnit = "教育局"
            amanage.releasePeople = "张三"
            amanage.releaseTime = "2018年5月21日"
            amanage.source = "教育局"
            amanage.mkdirTime = "2018年5月12日"
            amanage.modifer = "张三"
            amanage.modifyTime = "2018年5月13日"
            db.session.add(amanage)
            return "1111", 200

    # def Dcmanage(self):
    #     """
    #     删除活动管理
    #     author:wpc
    #     :return:
    #     """
    #     with db.auto_commit():
    #         media = ActivityManage.query.filter_by(id="9").all()
    #         db.session.delete(media)
    # def alteractivity(self):
    #     """
    #     修改活动管理
    #     author:wpc
    #     :return:
    #     """
    #     with db.auto_commit():
    #         media = ActivityManage.query.filter_by(id="9").all()
    #         media.mediaType = "培训"
    #         media.activityTitle = request.form.get("atname")
    #         media.activityType  = request.form.get("tname")
    #         media.area = request.form.get("area")
    #         media .acativity = request.form.get("activity")
    #         media.relasePerson = request.form.get("rperson")
    #         media.relaseTime = request.form.get("relasetime")

class MascotView(RestView):
    """
    吉祥物管理
    author:wpc
    """
    def addmascot(self):
        """
        新增吉祥物
        :return:
        """
        with db.auto_commit():
            mascot = Mascot()
            mascot.id = 8
            mascot.title = "吉祥物"
            mascot.intro = "奥运福娃"
            mascot.releasePeople = "发布人，张三"
            mascot.releaseTime = '%2018-%4-%23'
            mascot.mkdirTime = '%2018-%4-%21'
            mascot.modifer = "李四"
            mascot.modifyTime = '%2018-%5-%22'
            mascot.sort = 8
            mascot.top = "已置顶"
            mascot.releaseNote = "已标识"
            db.session.add(mascot)
            return "1111", 200

    def deletemascot(self):
        """
        删除吉祥物
        :return:
        """
        with db.auto_commit:
            mascotlist=Mascot.query.filter_by(id="7").all()
            for m in mascotlist:
                m.active =1
        return "1111", 200


class GuestView(RestView):
    """
    嘉宾管理
    author:wpc
    """
    def addguest(self):
        with db.auto_commit():
            guest = Guest()
            guest.id = 20
            guest.title = "嘉宾管理标题"
            guest.activityType = "活动类"
            guest.publisher = "张三"
            guest.releaseTime = '%2018-%5-%23'
            guest.mkdirTime = '%2018-%5-%21'
            guest.modifer = "李四"
            guest.modifyTime = "%2018-%5-%24"
            guest.sort =20
            guest.top = "已置顶"
            guest.releaseNote = "已标识"
            db.session.add(guest)
            return "1111", 200
    def deleteguest(self):
        """
        删除嘉宾管理
        :return:
        """
        with db.auto_commit:
            guestlist= Guest.query.filter_by(id="").all()
            for gu in guestlist:
                gu.active=1
        return "111",200
class HallView(RestView):
    """
    展厅管理
    author:wpc
    """
    def addhall(self):
        """
        添加展厅管理
        author:wpc
        :return:
        """
        with db.auto_commit():
            hall = Hall()
            hall.id = 23
            hall.title = "添加展厅"
            hall.intro ="添加展厅活动相关信息"
            hall.releasePeople = "张三"
            hall.releaseTime = "%2018-%5-%21"
            hall.mkdirTime = "%2018-%5-%21"
            hall.modifier = "李四"
            hall.modifyTime = "%2018-%5-%21"
            hall.sort = 23
            hall.top = "已置顶"
            hall.releaseNote = "已标识"
            db.session.add(hall)
            return "1111", 200
    def deletehall(self):
        """
        删除展厅管理
        :return:
        """
        with db.auto_commit():
            halllist = Hall.query.filter_by(id=data[id]).all()
            for hall in halllist:
                hall.active=1
            return "1111", 200

class ActivityTypeView(RestView):
    def addactivitytype(self):
        """
        活动类别管理
        author:wpc
        :return:
        """
        with db.auto_commit():
            atype = ActivityType()
            atype.id = 24
            atype.activityTitle = "活动类别管理标题"
            atype.activityType = "活动类别类型"
            atype.activityIntro = "活动简介"
            atype.releasePeople = "张三"
            atype.releaseTime = "%2018-%5-%21"
            atype.modifier = "李四"
            atype.updateTime = "%2018-%5-%21"
            atype.status = "已启用"
            atype.pageView = 300
            atype.href = "www.baidu.com"
            db.session.add(atype)
            return "1111", 200

    def deleteactivity(self):
        with db.auto_commit():
            """
            活动类别删除
            """
            alist = ActivityType.query.filter_by(id="").all()
            for a in alist:
                a.active=1
            return "1111",200



# class CenterNewView(RestView):
#     """
#     中央快讯
#     author:wpc
#     """
#     def addcenternew(self):
#         """
#         添加中央快讯
#         author:wpc
#         :return:
#         """
#         with db.auto_commit():
#             cnew = CenterNew()
#             cnew.id = 25
#             cnew.title = "中央快讯信息"
#             cnew.intro = "中央快讯简介"
#             cnew.releaseTime = "%2018-%5-%21"
#             cnew.mkdirTime = "%2018-%5-%21"
#             cnew.modifyTime = "%2018-%5-%21"
#             cnew.sort = 25
#             cnew.releaseNote = "已标识"
#             cnew.top = "已置顶"
#             cnew.source = "中央"
#             db.session.add(cnew)
#             return "1111", 200
#     def deletecnew(self):
#         with db.auto_commit():
#             cnewlist = CenterNew.query.filter_by(id="").all()
#             for cnew in cnewlist:
#                 cnew.active=1
#         return "1111", 200


# class LocalNewView(RestView):
#     """
#     地方报道
#     author:wpc
#     """
#     def addlocalnew(self):
#         """
#         发布地方报道
#         author:wpc
#         :return:
#         """
#         with db.auto_commit():
#             lnew = LocalNew()
#             lnew.id = 26
#             lnew.title = "地方报道消息"
#             lnew.intro = "地方报道简介"
#             lnew.releaseTime = "%2018-%5-%21"
#             lnew.mkdirTime = "%2018-%5-%21"
#             lnew.modifyTime = "%2018-%5-%21"
#             lnew.sort = 26
#             lnew.releaseNote = "已标识"
#             lnew.top = "已置顶"
#             lnew.source = "来源"
#             db.session.add(lnew)
#             return "1111", 200

# class DepartmentView(RestView):
#     """
#     部委讯息
#     author:wpc
#     """
#     def adddepartment(self):
#         """
#         发布部委讯息
#         author:wpc
#         :return:
#         """
#         with db.auto_commit():
#             d = Department()
#             d.id = 27
#             d.title = "部委讯息"
#             d.intro = "部委讯息简介"
#             d.releaseTime = "%2018-%5-%21"
#             d.mkdirTime = "%2018-%5-%21"
#             d.modifyTime = "%2018-%5-%21"
#             d.sort = 27
#             d.releaseNote = "已标识"
#             d.top = "已置顶"
#             d.source = "资料来源"
#             db.session.add(d)
#             return "1111", 200

# class policyView(RestView):
#     """
#     政策讯息
#     author:wpc
#     """
#     def Addpolicy(self):
#         """
#         发布政策讯息
#         author:wpc
#         :return:
#         """
#         with db.auto_commit():
#             p = policy()
#             p.id = 28
#             p.title = "政策讯息"
#             p.intro = "政策讯息简介"
#             p.releaseTime = "%2018-%5-%21"
#             p.mkdirTime = "%2018-%5-%21"
#             p.modifyTime = "%2018-%5-%21"
#             p.sort = 28
#             p.releaseNote = "已标识"
#             p.top = "已置顶"
#             p.source = "资料来源"
#             db.session.add(p)
#             return "1111", 200

# class LocalReportView(RestView):
#     """
#     地方报道
#     author:wpc
#     """
    # def AddLocalReport(self):
    #     """
    #     发布地方报道
    #     author:wpc
    #     :return:
    #     """
    #     with db.auto_commit():
    #         lreport = LocalReport()
    #         lreport.id = 28
    #         lreport.title = "测试"
    #         lreport.intro = "简介"
    #         lreport.releaseTime = "%2018-%5-%21"
    #         lreport.sort = 28
    #         lreport.top = "已置顶"
    #         lreport.releaseNote = "已标识"
    #         db.session.add(lreport)
    #         return "1111", 200
    # def deletelocalreport(self):
    #     with db.auto_commit():
    #         lreportlist = LocalReport.query.filter_by(id="").all()
    #         for lreport in lreportlist:
    #             lreport.active=1
    #     return "1111", 200























