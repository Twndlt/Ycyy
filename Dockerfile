# 引入自己构建的基础镜像
FROM hub.c.163.com/jandand/py3-flask:v0.1

MAINTAINER littleseven <https://www.soo9s.com>

ADD innp_app/ /home/innp_app

# supervisor 和 Nginx 配置
COPY docker-dev/supervisor.conf /usr/supervisord.conf
COPY docker-dev/innp /etc/nginx/conf.d/default.conf

WORKDIR /home/innp_app/

# 安装项目所需的第三方
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  -r requirements.txt \
    && python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple \
    gunicorn