def volumeSphere(R):
    PI= 3.14159
    return 4/3*(PI)*R*R*R

Sphere1= float(input("Radius of first sphere: "))
Sphere2= float(input("Radius of second sphere: "))
Sphere3= float(input("Radius of third sphere: "))

Volume1= volumeSphere(Sphere1)
Volume2= volumeSphere(Sphere2)
Volume3= volumeSphere(Sphere3)

print(f"The volume of 1st sphere: {Volume1:.2f}")
print(f"The volume of 2nd sphere: {Volume2:.2f}")
print(f"The volume of 3nd sphere: {Volume3:.2f}")
