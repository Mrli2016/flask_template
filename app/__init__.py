# -*- coding: utf-8 -*-
"""
@Author: 李子
@Email: mrli2016@126.com
@Date: 2019-12-25 22:46:25
@LastEditTime: 2020-04-17 10:46:25
@Description:
"""
from flask import Flask
import pymongo
# import redis


app = Flask(__name__)
app.config.from_object("config")

# Redis = redis.Redis(host='111.229.218.119', port=6378, password="test123")
mongo = pymongo.MongoClient(app.config["MONGO_URI"])


def register_blueprints(flask_app):
    from app.api.base import base

    flask_app.register_blueprint(base, url_prefix='/')


def init_app():
    """  系统初始化   """
    # 注册蓝图
    register_blueprints(app)

    return app
