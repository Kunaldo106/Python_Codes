#to check whether a number is prime or not:

def check_prime(num):
    flag=0
    for i in range(2, int((num**0.5)+1)):
        if (num%i==0):
            flag+=1
        
    return flag
    
num= int(input("Enter the number: "))
check= check_prime(num)
if(check==0):
    print(f"The number {num} is Prime")
else:
    print(f"The number {num} is not Prime")
