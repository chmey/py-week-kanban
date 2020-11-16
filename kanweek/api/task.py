from .common import bpAPI
from flask import jsonify, request
from kanweek.models.task import Task, TaskSchema
from datetime import datetime

siTaskSchema = TaskSchema()
plTaskSchema = TaskSchema(many=True)


@bpAPI.route('/api/v1/task/', methods=['GET'])
@bpAPI.route('/api/v1/task/<string:id>', methods=['GET'])
def read_task(id=None):
    if id:
        task = Task.query.get(id)
        if task:
            return jsonify({"status": "ok", "data": siTaskSchema.dump(task)})
        else:
            return jsonify({"status": "error", "message": "No task found for ID {}.".format(id)}), 404
    else:
        return jsonify({"status": "error", "message": "Missing task ID parameter."}), 400


@bpAPI.route('/api/v1/task/', methods=['POST'])
def create_task():
    if request.is_json:
        post = request.get_json()
        newTask = Task()
        try:
            newTask.title = post['title']
            newTask.description = post['description']
            newTask.created_date = datetime.now()
        except KeyError:
            return jsonify({"status": "error", "message": "Bad Request. Must supply all required values."}), 400
        try:
            newTask.save()
        except Exception:
            return jsonify({"status": "error", "message": "Failed saving the values to the database."}), 500

        return jsonify({"status": "ok", "data": siTaskSchema.dump(newTask)})
    else:
        return jsonify({"status": "error", "message": "Bad Request. Must supply JSON Data."}), 400
