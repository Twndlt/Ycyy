# -*- coding: utf-8 -*-
from flask import Flask
from flask_migrate import Migrate
from flasgger import Swagger
from .config import configs
from .models import db


def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    Swagger(app)


def register_blueprints(app):
    from .apps import home
    app.register_blueprint(home)
    # app.register_blueprint(docs)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_blueprints(app)  # 注册路由
    register_extensions(app)  # 数据库热迁移

    return app
