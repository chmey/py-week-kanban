from .common import bpAPI
from flask import jsonify, request
from kanweek.models.task import Task, TaskSchema
from datetime import datetime
from mongoengine import errors

siTaskSchema = TaskSchema()
plTaskSchema = TaskSchema(many=True)


@bpAPI.route('/api/v1/tasks/', methods=['GET'])
@bpAPI.route('/api/v1/tasks/<string:id>', methods=['GET'])
def read_task(id=None):
    if id:
        task = Task.objects.get(id=id)
        if task:
            return jsonify({"status": "ok", "data": siTaskSchema.dump(task)})
        else:
            return jsonify({"status": "error", "message": "No task found for ID {}.".format(id)}), 404
    else:
        tasks = Task.objects(archived=False).all()
        return jsonify({"status": "ok", "data": plTaskSchema.dump(tasks)}), 200


@bpAPI.route('/api/v1/tasks/', methods=['POST'])
def create_task():
    if request.is_json:
        post = request.get_json()['data']
        print(post)
        newTask = Task()
        try:
            newTask.title = post['title']
            newTask.description = post['description']
            newTask.weekday = post['weekday']
            if post['dateDue']:
                try:
                    newTask.dateDue = datetime.fromisoformat(post['dateDue'])
                except Exception:
                    return jsonify({"status": "error", "message": "Bad Request. Could not parse the due date."}), 400
            newTask.dateCreated = datetime.now()
        except KeyError:
            return jsonify({"status": "error", "message": "Bad Request. Must supply all required values."}), 400
        try:
            newTask.save()
        except Exception:
            raise
            return jsonify({"status": "error", "message": "Failed saving the values to the database."}), 500

        return jsonify({"status": "ok", "data": siTaskSchema.dump(newTask)}), 201
    else:
        return jsonify({"status": "error", "message": "Bad Request. Must supply JSON Data."}), 400


@bpAPI.route('/api/v1/tasks/<string:id>', methods=['PUT'])
def update_task(id=None):
    if id:
        task = Task.objects.get(id=id)
        if task:
            if request.is_json:
                try:
                    data = request.get_json()['data']
                    data['dateModified'] = datetime.now()
                    data['dateCreated'] = task.dateCreated
                    data['id'] = task.id
                    task.update(**data)
                    task = Task.objects.get(id=id)
                except Exception:
                    raise
            return jsonify({"status": "ok", "data": siTaskSchema.dump(task)})
        else:
            return jsonify({"status": "error", "message": "No task found for ID {}.".format(id)}), 404
    else:
        return jsonify({"status": "error", "message": "Missing task ID parameter."}), 400


@bpAPI.route('/api/v1/tasks/', methods=['DELETE'])
@bpAPI.route('/api/v1/tasks/<string:id>', methods=['DELETE'])
def delete_task(id=None):
    permanently = request.args.get('permanent', False)
    if id:
        try:
            task = Task.objects.get(id=id)
            if permanently:
                task.delete()
            else:
                task.archived = True
                task.save()
        except errors.DoesNotExist:
            return jsonify({"status": "error", "message": "No task found for ID {}.".format(id)}), 404
        except Exception:
            return jsonify({"status": "error", "message": "Deletion for ID {} failed.".format(id)}), 500
    else:
        try:
            tasks = Task.objects.delete()
            if permanently:
                tasks.delete()
            else:
                for task in tasks:
                    task.archived = True
                    task.save()
            return jsonify({"status": "ok", "data": ''}), 200
        except Exception:
            return jsonify({"status": "error", "message": "Deletion failed."}), 500
