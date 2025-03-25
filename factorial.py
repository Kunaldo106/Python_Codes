# find factorial of a number using recursive function:

def fact(num):
    if(num==0 or  num==1):
        return 1
    else:
        return num*fact(num-1)
    
num= int(input("Input: "))
res= fact(num)
print(res)