#to find the average of n numbers

n= int(input("Enter the no. of integer: "))
total= 0
    
for i in range(1,n+1):
    num= int(input(f"Enter the integer {i}: "))
    total= total+num

average= total/n
print(f"The average of {n} integers: {average}")


