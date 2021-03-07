"""
@Author: 李子
@Email: mrli2016@126.com
@Date: 2020-01-08 23:36:02
@LastEditTime : 2020-01-09 12:41:03
@Description:
"""
from flask import has_request_context, g
from functools import wraps
from app import mongo
from bson import ObjectId
from werkzeug.local import LocalProxy

user_db = mongo.dianqun.user

# jwt_user = LocalProxy(lambda: _get_user())

# def _get_user():
#   if has_request_context() and not hasattr(g, 'user'):
#     pass


def jwt_login_required(func):
    """
    jwt登录权限装饰器
    """
    from flask import request, jsonify
    import jwt

    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('token')
        try:
            jwt_info = jwt.decode(
                token, 'zifeiyu', issuer='mrlizi', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'code': 514, 'msg': '登录状态已过期'})
        except jwt.InvalidTokenError:
            return jsonify({'code': 508, 'msg': '登录状态无效'})
        jwt_user = user_db.find_one(
            {'_id': ObjectId(jwt_info['data'].get('uid'))})
        if jwt_user:
            return func(*args, **kwargs, jwt_user=jwt_user)
        else:
            return jsonify({'code': 502, 'msg': '登录状态无效'})

    return decorated_function


def jwt_admin_required(func):
    """
    jwt登录权限装饰器
    """
    from flask import request, jsonify
    import jwt

    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('token')
        try:
            jwt_info = jwt.decode(
                token, 'zifeiyu', issuer='mrlizi', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'code': 514, 'msg': '登录状态已过期'})
        except jwt.InvalidTokenError:
            return jsonify({'code': 508, 'msg': '登录状态无效'})
        jwt_user = user_db.find_one(
            {'_id': ObjectId(jwt_info['data'].get('uid'))})
        if jwt_user:
            if jwt_user.get('role') > 90:
              return func(*args, **kwargs, jwt_user=jwt_user)
            else:
              return jsonify({'code': 403, 'msg': '权限不足'})
        else:
            return jsonify({'code': 502, 'msg': '登录状态无效'})

    return decorated_function
