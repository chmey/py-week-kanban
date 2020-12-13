from .common import bpAPI
from flask import jsonify, request
from kanweek.models.user import User
from mongoengine.errors import DoesNotExist


@bpAPI.route('/api/v1/auth/login', methods=['POST'])
def auth_login():
    if request.is_json:
        post = request.get_json()['data']
        if 'email' in post and 'password' in post:
            try:
                user = User.objects.get(email=post['email'])
                if user.verify_password(post['password']) and not user.disabled:
                    return jsonify({"status": "ok", "data": {"isAuthenticated": True}})
            except DoesNotExist:
                pass
            return jsonify({"status": "error", "data": {"isAuthenticated": False}, "message": "Login failed."}), 403
        else:
            return jsonify({"status": "error", "message": "Bad Request. Must supply all required values."}), 400
    else:
        return jsonify({"status": "error", "message": "Bad Request. Must supply JSON Data."}), 400
