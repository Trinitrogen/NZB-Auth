from nzb_auth import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"