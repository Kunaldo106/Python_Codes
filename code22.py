

name= input("Enter Name:")
gender= input("Enter Gender(M/F): ")

if(gender=='M'):
    newName= "Mr "+ name
if(gender=='F'):
    newName= "Ms "+ name
print(f"Name: {newName}")
