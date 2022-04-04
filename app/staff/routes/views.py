from app import app
from flask import  render_template, request, abort, flash, url_for, redirect
from ... import db
from ...models import Users
from flask_login import login_user, login_required, logout_user, current_user

@app.route("/staff")
def staff():
    return render_template('staff_index.html',  title="Home")

