from app import app
from flask import  render_template, request, abort, flash, url_for, redirect
from ... import db
from ...generic_functions.diagnose import Diagnose_patient 
from ...models import Users, Diagnosed_history
from flask_login import login_user, login_required, logout_user, current_user
from datetime import date, datetime

today = date.today()
now = datetime.now()
time = now.strftime("%H:%M:%S")




@app.route("/staff/diagnose", methods=["POST", "GET"])
def diagnose():
 doctor = current_user
 if request.method == "GET":
        msg = { "temp": ["Low", "Average", "High", "Very-high"], 
                "age":range(90),
                "bloodpressure": range(40,200)
        }
 if request.method == "POST":
        fullname = str(request.form.get('fullname')).title() 
        weight = str(request.form.get('weight'))    
        temperature = int(request.form.get('temperature')) 
        bloodpressure = int(request.form.get('bloodpressure'))
        age = int(request.form.get('age')) 
        sex = str(request.form.get('gender')).title() 
        other_symptoms = str(request.form.get('symptoms'))
        firstname = fullname.split(" ")[0]
        lastname = fullname.split(" ")[1]
       #  print(fullname.split(" ")[1], "============>", fullname.split(" "))

       #  symptoms = [other_symptoms.split()] 
        symptoms=[]
       #  ------ end of form---------
       #  ------ blood pressure

#        Children (2–13 years)
        if age > 1 and age < 14:

           if bloodpressure > 120:
               symptoms.append("bloodpressure_High")
           
           if bloodpressure < 80:
               symptoms.append("bloodpressure_low")

        # Adolescent (14–18 years)  
        if age > 13 and age < 19:

           if bloodpressure > 120:
               symptoms.append("bloodpressure_High")
           
           if bloodpressure < 90:
              symptoms.append( "bloodpressure_low")

        # Adult (19–40 years)
        if age > 18 and age < 41:

           if bloodpressure > 135:
               symptoms.append("bloodpressure_High")
           
           if bloodpressure < 95:
               symptoms.append("bloodpressure_low")

         # Adult (41–60 years) 
        if age > 40 and age < 61:

           if bloodpressure > 145:
               symptoms.append("bloodpressure_High")
           
           if bloodpressure < 110:
              symptoms.append( "bloodpressure_low")

        #  Older adult (61 and older)
        if age > 60 :

           if bloodpressure > 145:
              symptoms.append( "bloodpressure_High")
           
           if bloodpressure < 95:
              symptoms.append( "bloodpressure_low")
        




# ------------- Temperature ---------
        if temperature > 100:
               if temperature > 107:
                     symptoms.append( "critical_high_temperature")
               else:
                       symptoms.append("High_temperature")


           
        elif temperature < 97:
               if temperature < 90:
                      symptoms.append("critical_low_temperature")
               else:
                      symptoms.append("low_temperature")






        
       
       #  print(symptoms)
        

        patient = Diagnose_patient(firstname=firstname, lastname=lastname, age=age, sex=sex,bloodpressure=bloodpressure, weight=weight)
        patient.diagnose(symptoms=symptoms)
        if patient.diagnosis:
           save_diagnosis = Diagnosed_history(firstname=firstname, lastname=lastname, diagnosed="".join(map(str, patient.diagnosis)), symptoms="".join(map(str, symptoms))) 
           db.session.add(save_diagnosis)
           db.session.commit()

       #  print(diagnosed_patient, "===================================>")    
        return render_template('staff_index.html',  doctor=doctor, title="Smart Diagnosis", patient=patient, date=today.strftime("%B %d, %Y"), time=time)
       
      
 return render_template('admin_index_form.html', msg = msg, doctor=doctor, title="Smart Diagnosis")  


@app.route("/staff", methods=["POST", "GET"])
def staff():
 doctor = current_user
 if request.method == "GET":
      
         return render_template('staff_index.html',  doctor=doctor, title="Smart Diagnosis", date=today.strftime("%B %d, %Y"), time=time)  
