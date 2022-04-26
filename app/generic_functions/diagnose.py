class Diagnose_patient:
   def __init__(self, firstname, lastname, age, sex, weight, bloodpressure, symptoms=[None] ):
       self.firstname = firstname
       self.lastname = lastname
       self.age = age
       self.sex = sex
       self.diagnosis = None
       self.symptoms = symptoms
       self.weight = weight
       self.bloodpressure = bloodpressure
       
   
   def diagnose(self, symptoms=[]):
       cancer =["High_temperature","low_temperature","cold","cough","eye sore"]
       covid =["High_temperature","critical_high_temperature","cold","dry cough","loss of taste","head ache"]
       flu = ["High_temperature","cold"]
       stroke = ["bloodpressure_High","bloodpressure_low","head ache"]
       possible = ["cancer","covid","flu","stroke"]



       for i in symptoms:

           if i == "critical_high_temperature":
               possible.append("This Patient has a very HIGH Temperature this could be as a result of an Infection, Advice Reduce patients temperature")

           if i == "critical_low_temperature":
               possible.append("This Patient has a very LOW Temperature patient could be lossing blood")

           if i == "bloodpressure_High":
               possible.append("This Patient has a very High Blood pressure Advise administer relaxatives, Stroke Risk is High")

           if i == "bloodpressure_low":
               possible.append("This Patient has a very LOW blood presure patient could be or have lost a lot of blood, check heart rate and ensure blood flow to the brain")
           
        #    print(possible,"========================================================>>>>>")
        #    print({i},"========================================================>>>>>")
           if i not in cancer:
               print(i,"=========================> not found in cancer ")
               if "cancer" in possible:
                print(f"Removing cancer {i} not found")
               
                possible.remove("cancer")
              
           if i not in covid:
             if "covid" in possible:
               print(f"Removing covid {i} not found") 
               possible.remove("covid")

           if i not in flu:
             if "flu" in possible:
               print(f"Removing flu {i} not found")  
               possible.remove("flu")

           if i not in stroke:
             if "stroke" in possible:
               print(f"Removing stroke {i} not found")  
               possible.remove("stroke")
        #    print(possible," FINAL========================================================>>>>>")
           self.diagnosis = possible
       return possible




       

# patient = Diagnose_patient("john", "doe", 27, "male", 27, 27)
# diagnosed = patient.diagnose(symptoms=["High_temperature","cold","dry cough"])

# print(diagnose)
# print(patient.diagnosis)

