# Question 16(a)
# Name and School: Alex Palframan, Athlone Community College
import random

def inputDetails():
    s_name=input("Enter your surname:     ")    
    f_name=input("Enter your first name:      ")
    age=int(input("Enter your age:      "))
    eircode = input("Enter your Eircode:	")
   
    
    print("Hello", f_name, s_name , "you are", age , "years old and your eircode is" , eircode)
    vaccinetrial = input("Do you wish to partake in a secret vaccine trial? Type YES or NO:	")
    vaccinechoices = ['A','B','C']
    if vaccinetrial == "YES":
        print(random.choice(vaccinechoices))
    else:
        pass
    ldoe = eircode[-1]
    ldoe = int(ldoe)
    if (ldoe%2==0):
        print("You must attend Eastwood for your vaccine")
    else:
        print("You must attend Northfield for your vaccine")

    if age < 50:
        print(f_name , "you will recieve the MRNA vaccine.")
    else:
        print(f_name , "you will recieve the ADENO vaccine.")

inputDetails()


choice = input("If you have finished entering peoples details type END, otherwise press RETURN:	")

if choice=="END":
    pass
else:
    inputDetails()
