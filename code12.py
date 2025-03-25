
def digitSum(num):
    digit=0
    while num>0:
        digit= digit+num%10
        num= num//10
    return digit
    
num= int(input("Enter the integer: "))
sum= int(digitSum(num))
print(sum)
