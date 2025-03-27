# Find the sum of natural numbers upto n numbers using recursion method:

def recursion(n):
    if n<1 :
        return -1
    elif n==1 :
        return n
    else:
        return n + recursion(n-1)

n = int(input("Enter the value of n: "))

sum= recursion(n)
if sum== -1 :
    print("Input a natural number!!")
else:
    print(f"Sum: {sum}")