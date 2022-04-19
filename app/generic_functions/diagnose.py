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
       cancer =["High_temperature","cold","cough","eye sore"]
       covid =["High_temperature","cold","dry cough","loss of taste","head ache"]
       flu = ["High_temperature","cold"]

       possible = ["cancer","covid","flu"]
       for i in symptoms:
          
           if i not in cancer:
              
                possible.remove("cancer")
              
           if i not in covid:
             
               possible.remove("covid")
           if i not in flu:
             
               possible.remove("flu")

           self.diagnosis = possible
       return possible




       

patient = Diagnose_patient("john", "doe", 27, "male", 27, 27)
diagnose = patient.diagnose(symptoms=["High_temperature","cold","dry cough"])

print(diagnose)
print(patient.diagnosis)