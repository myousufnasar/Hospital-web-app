from app import app
from flask import  render_template



@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/services")
def services():
    return render_template('services.html')


@app.route("/contacts")
def contacts():
    return render_template('contacts.html')


@app.route("/departments")
def departments():
    return render_template('departments.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route("/appointments")
def appointments():
    return render_template('appointments.html')


