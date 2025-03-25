#WAP to check whether a number is armstrong or not:

def is_armstrong(num):
    sum=0
    ln= len(str(num))
    while(num!=0):
        rem= num%10
        sum= sum+ (rem**ln)
        num=num//10
    return sum

num= int(input("Enter the number: "))
check= is_armstrong(num)
if(check==num):
    print(f"The number {num} is Armstrong")
else:
    print(f"The number {num} is not Armstrong")