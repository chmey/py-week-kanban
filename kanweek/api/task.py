from .common import bpAPI
from flask import jsonify
from kanweek.models.task import Task


@bpAPI.route('/api/v1/task/', methods=['GET'])
@bpAPI.route('/api/v1/task/<string:id>', methods=['GET'])
def get_task(id=None):
    if id:
        task = Task.query.get(id)
        if task:
            return jsonify({"status": "ok", "data": task})
        else:
            return jsonify({"status": "error", "message": "No task found for ID {}.".format(id)}), 404
    else:
        return jsonify({"status": "error", "message": "Missing task ID parameter."}), 400
