# 引入自己构建的基础镜像
FROM hub.c.163.com/jandand/py3-flask:v0.1

MAINTAINER littleseven <https://www.soo9s.com>

RUN mkdir /home/innp_app

# supervisor 和 Nginx 配置
COPY docker-dev/requirements.txt /home/innp_app
COPY docker-dev/supervisor.conf /usr/supervisord.conf
COPY docker-dev/innp /etc/nginx/conf.d/default.conf

WORKDIR /home/innp_app/

# 安装项目所需的第三方
RUN python3 -m pip install -i https://pypi.douban.com/simple  -r requirements.txt \
    && python3 -m pip install -i https://pypi.douban.com/simple \
    gunicorn \