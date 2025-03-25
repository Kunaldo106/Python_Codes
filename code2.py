#To find the area of rectangle

def AreaOfRectangle(length, breadth):
    return length*breadth

length = float(input("Enter the first value: "))
breadth = float(input("Enter the second value: "))

area= AreaOfRectangle(length, breadth)
print(f"The area: {area} units")    
