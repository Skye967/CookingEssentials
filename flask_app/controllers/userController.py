from flask import render_template, redirect, request, session, flash, url_for
from flask_app import app
import os
from ..models.User import User
from flask_app.config.my_sequal_connections import connectToMySQL
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/")
def title():
    return render_template("title.html")


@app.route("/index")
def index():
    if 'logged_in' not in session:
        session['logged_in'] = ""
        session['user_id'] = 0
        session['user_name'] = ""
    if session['logged_in'] != "":
        return redirect("/dashboard/display_images")
    return render_template("index.html")


@app.route("/login", methods = ["POST", "GET"])
def login():
    if session['logged_in'] != "":
        return render_template('dashboard.html')
    if not User.user_login(request.form):
        return redirect("/index")
    session['logged_in'] = request.form['login']
    user_info = User.user_login(request.form)
    for user_id in user_info:
        user_id.id
        user_id.fname
        session['user_name'] = user_id.fname
        session['user_id'] = user_id.id
    return redirect("/index")

@app.route("/log_out")
def logout():
    session.clear()
    return redirect("/")


@app.route("/registration", methods = ["POST"])
def enter_email():
    print(request.form)
    if not User.validate_email(request.form):
        return redirect("/index")
    print(request.form)
    pw_hash = bcrypt.generate_password_hash(request.form['p_word'])
    cpw_hash = bcrypt.generate_password_hash(request.form['password_confirmation'])
    data = {
        "firstname": request.form['firstname'],
        "lastname":request.form['lastname'],
        "email_name": request.form['email_name'],
        "p_word" : pw_hash,
        "confirmpassword": cpw_hash
    }
    user_id = User.add_email(data)
    session['user_id'] = user_id
    display = User.display_emails()
    return redirect("/index")

if __name__ == "__main__":
    app.run(debug=True)