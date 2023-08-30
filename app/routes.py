from app import app

@app.route("/")
def home():
    return 'My first app!'

@app.route('/index')
def index():
    return "This is my route index"