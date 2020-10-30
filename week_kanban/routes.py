from week_kanban import app


@app.route('/')
def index():
    return "Hello"