from app import app
from flask import  render_template, request, abort, flash, url_for, redirect
from . import db
from .models import Users
from flask_login import login_user, login_required, logout_user, current_user

@app.route("/")
def home():
    return render_template('index.html',  title="Home")


@app.route("/login", methods=["GET", "POST"])
def login():
   if request.method == "POST":
      
      email = str(request.form.get('email')).title()
      password = str(request.form.get('password'))
      
    #   check for existence
      check = Users.query.filter_by(email=email, password=password).first()
      if not check:
            # print("==========================>User already exist")
            flash("No user with the given details exist, Please check your email address or password and try again")
            abort(404)
      else:
        #   print("=======================>User saved")
        #   saves user if not found
        login_user(check, remember=True)
        role = current_user.role
        
        return redirect(url_for(str(role).lower()))


   return render_template('login.html')

# route to signup users
@app.route("/signup", methods=["POST", "GET"])
def signup():
   if request.method == "POST":
      firstname = str(request.form.get('firstname')).title()
    #   print(f"===========================> this is {firstname}")
      lastname = str(request.form.get('lastname')).title()
      sex = str(request.form.get('sex')).title()
      address = str(request.form.get('address')).title()
      dob = str(request.form.get('dob')).title()
      email = str(request.form.get('email')).title()
      telephone = str(request.form.get('telephone')).title()
      password = str(request.form.get('password'))
      
    #   check for existence
      check = Users.query.filter_by(email=email).first()
      if check:
            # print("==========================>User already exist")
            flash("An Account has alredy been Registered with this email ")
            abort(500)
      else:
        #   print("=======================>User saved")
        #   saves user if not found
          save_user = Users(firstname=firstname, lastname=lastname, email=email, password=password, telephone=telephone, address=address, sex=sex, dob=dob )
          db.session.add(save_user)
          db.session.commit()
        

          user = Users.query.filter_by(
                email=email, password=password).first()
          if user.role == 'Staff':
                login_user(user, remember=True)
                return redirect(url_for("staff"))




   return render_template('signup.html', title="Sign Up")




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


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

# @app.route("/new3", methods=["POST", "GET"])
# def new3():
#     if request.method == "GET":
#         msg = { "temp": [47, 50, 100, 200], 
#                 "age":20,
#                 "bloodpressure": [100, 50,]
#         }
#     if request.method == "POST":
#         weight = str(request.form.get('weight')).title()
#         print(f"===========================> this is {weight}")
#         temperature = str(request.form.get('temperature')).title()
#         print(f"===========================> this is {temperature}")
#         bloodpressure = str(request.form.get('bloodpressure')).title()
#         print(f"===========================> this is {bloodpressure}")
#         return redirect(url_for("staff"))
#         # return render_template("result.html",msg = msg)
      
#     return render_template('admin_index_form.html', msg = msg)  
