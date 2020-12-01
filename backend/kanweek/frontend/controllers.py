from .common import bpFrontend
from flask import render_template

@bpFrontend.route('/', methods=['GET'])
def index():
    return render_template('index.html')
