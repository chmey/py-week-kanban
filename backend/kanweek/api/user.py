from .common import bpAPI # noqa
from flask import jsonify, request, url_for
from kanweek.models.user import User, UserSchema
from kanweek.extensions import db # noqa
from datetime import datetime
from mongoengine import errors

siUserSchema = UserSchema()
plUserSchema = UserSchema(many=True)


@bpAPI.route('/api/v1/users/', methods=['GET'])
@bpAPI.route('/api/v1/users/<string:id>', methods=['GET'])
def read_user(id=None):
    if id:
        user = User.objects.get(id=id)
        if user:
            return jsonify({"status": "ok", "data": siUserSchema.dump(user)})
        else:
            return jsonify({"status": "error", "message": "No user found for ID {}.".format(id)}), 404
    else:
        users = User.objects().all()
        return jsonify({"status": "ok", "data": plUserSchema.dump(users)}), 200


@bpAPI.route('/api/v1/users/', methods=['POST'])
def create_user():
    if request.is_json:
        post = request.get_json()['data']
        newUser = User()
        try:
            newUser.email = post['email']
            newUser.set_password_hash(post['password'])
            if 'username' in post:
                try:
                    newUser.username = post['username']
                except Exception:
                    return jsonify({"status": "error", "message": "Bad Request. Could not assign the username."}), 400
            newUser.dateJoined = datetime.now()
        except KeyError:
            return jsonify({"status": "error", "message": "Bad Request. Must supply all required values."}), 400
        try:
            newUser.save()
        except Exception:
            return jsonify({"status": "error", "message": "Failed saving the values to the database."}), 500

        return jsonify({"status": "ok", "data": siUserSchema.dump(newUser)}), 201, {'Location': url_for('api.read_user', id=newUser.id, _external=True)}
    else:
        return jsonify({"status": "error", "message": "Bad Request. Must supply JSON Data."}), 400


@bpAPI.route('/api/v1/users/<string:id>', methods=['PUT'])
def update_user(id=None):
    if id:
        user = User.objects.get(id=id)
        if user:
            if request.is_json:
                try:
                    data = request.get_json()['data']
                    if User.objects.get(email=data['email']).first():
                        return jsonify({"status": "error", "message": "The email is already used."}), 400
                    user.dateModified = datetime.now()
                    user.email = data['email']
                    user.set_password_hash(data['password'])
                    user.save()
                except Exception:
                    raise
            return jsonify({"status": "ok", "data": siUserSchema.dump(user)})
        else:
            return jsonify({"status": "error", "message": "No user found for ID {}.".format(id)}), 404
    else:
        return jsonify({"status": "error", "message": "Missing user ID parameter."}), 400


@bpAPI.route('/api/v1/users/', methods=['DELETE'])
@bpAPI.route('/api/v1/users/<string:id>', methods=['DELETE'])
def delete_user(id=None):
    permanently = request.args.get('permanent', False)
    if id:
        try:
            user = User.objects.get(id=id)
            if permanently:
                user.delete()
            else:
                user.disabled = True
                user.save()
        except errors.DoesNotExist:
            return jsonify({"status": "error", "message": "No user found for ID {}.".format(id)}), 404
        except Exception:
            return jsonify({"status": "error", "message": "Deletion for ID {} failed.".format(id)}), 500
    else:
        try:
            users = User.objects.delete()
            if permanently:
                users.delete()
            else:
                for user in users:
                    user.disabled = True
                    user.save()
            return jsonify({"status": "ok", "data": ''}), 200
        except Exception:
            return jsonify({"status": "error", "message": "Deletion failed."}), 500
