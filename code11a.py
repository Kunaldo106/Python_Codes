n= int(input("Enter the value of n: "))
for i in range(n):
    for j in range(1, i+1):    
        print(" ", end=" ")
    for j in range(1, n-i+1):
        print(j,end=" ")
    print()
    
