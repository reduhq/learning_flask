from app import app

@app.route("/")
def home():
    return 'Home'

@app.route("/create_list")
def create_list():
    return "Create List"

@app.route("/read_list")
def read_list():
    return "Read List"

@app.route("/delete_list")
def delete_list():
    return "Delete List"