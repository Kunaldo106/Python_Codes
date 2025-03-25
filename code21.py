
def checkDivisibility(num):
    if(num%8==0):
        return True
    else:
        return False
num=int(input("Enter the integer: "))
if checkDivisibility(num):
    print(f"The integer {num} is divisible by 8")
else:
    print(f"The integer {num} is not divisible by 8")
