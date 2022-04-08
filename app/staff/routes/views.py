from app import app
from flask import  render_template, request, abort, flash, url_for, redirect
from ... import db
from ...models import Users
from flask_login import login_user, login_required, logout_user, current_user

@app.route("/staff/diagnose", methods=["POST", "GET"])
def diagnose():
 doctor = current_user
 if request.method == "GET":
        msg = { "temp": ["Low", "Average", "High", "Very-high"], 
                "age":range(90),
                "bloodpressure": range(40,200)
        }
 if request.method == "POST":
        weight = str(request.form.get('weight')).title()       
        temperature = str(request.form.get('temperature')).title()      
        bloodpressure = str(request.form.get('bloodpressure')).title() 
               
        return redirect(url_for("staff"))
       
      
 return render_template('admin_index_form.html', msg = msg, doctor=doctor, title="Smart Diagnosis")  


@app.route("/staff", methods=["POST", "GET"])
def staff():
 doctor = current_user
 if request.method == "GET":
      
         return render_template('staff_index.html',  doctor=doctor, title="Smart Diagnosis")  
