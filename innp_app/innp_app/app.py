# -*- coding: utf-8 -*-
from flask import Flask
from .config import configs
from .models import db


def register_blueprints(app):
    from .apps import home
    app.register_blueprint(home)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprints(app)  # 注册路由

    return app
