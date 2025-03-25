#To calculate the time of workof three men

def WorkCalculate(x,y,z):
    return (x*y*z)/(x*y+y*z+x*z)
    
per1= int(input("Enter the days taken by person 1: "))
per2= int(input("Enter the days taken by person 2: "))
per3= int(input("Enter the days taken by person 3: "))

total= float(WorkCalculate(per1,per2,per3))
print(f"The Time taken to complete work together is {total:.2f} days.")
