#swapping of variable without using third variable

def swap(x,y):
    x, y= y, x
    return x, y
    
num1= int(input("Enter the first integer: "))
num2= int(input("Enter the second integer: "))
'''num1, num2= swap(num1, num2)'''
print("Before swapping:-")
print(f"Num1: {num1}")
print(f"Num2: {num2}")
num1, num2= num2, num1
print("After swapping:-")
print(f"Num1: {num1}")
print(f"Num2: {num2}")
