from kanweek import app


@app.route('/')
def index():
    return "Hello"
