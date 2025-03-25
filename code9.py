#to calculate the  

import datetime
x= datetime.datetime.now()
year= x.year

def ageHundred(age):
    birth= year- age
    return birth+100
    

name= input("Enter your name: ")
age= int(input("Enter your age: "))
finalage= ageHundred(age)

print(f"{name}, you are going to be 100 at the year {finalage}")

