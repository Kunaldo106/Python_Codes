# to make a recursive function to add number upto times:

def sum_recursive(n):
    if(n<1):
        return 0
    else:
        return n+sum_recursive(n-1)
    
n= int(input("Enter the number: "))
sum= sum_recursive(n)

print(sum)