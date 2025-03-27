# Multiple two numbers without using multiplication operator:

def multiple(a,b):
    sum=0
    if a==0 or b==0:
        return 0
    else:
        for i in range(1,b+1):
            sum=sum+a
    return sum       

a= int(input("Enter the value: "))
b= int(input("Enter the value: "))
mul= multiple(a,b)

print(f"Multiple: {mul}")