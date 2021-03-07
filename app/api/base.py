'''
@Author: 李子
@Email: mrli2016@126.com
@Date: 2019-12-25 22:46:25
@LastEditTime : 2020-01-08 14:45:32
@Description: 
'''
# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
from app import mongo
from time import time

base = Blueprint('base', __name__)

token_db = mongo.ext.token


@base.route('/demo/')
def index():
    return 'hello flask'
