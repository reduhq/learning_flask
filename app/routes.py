from flask import render_template, request, session, redirect, url_for

from app import app

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/create_list", methods=['GET', 'POST'])
def create_list():
    if request.method == 'GET':
        variable = 'reduhq'
        return render_template('create_list.html', var=variable)
    if request.method == 'POST':
        data = request.form
        name = data["nombre"]
        quantity = data["cantidad"]
        session[name] = quantity
        return redirect(url_for('create_list'))

@app.route("/read_list")
def read_list():
    return render_template("read_list.html")

@app.route("/delete_list")
def delete_list():
    session.clear()
    return redirect(url_for('home'))