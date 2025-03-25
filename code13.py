
n= int(input("Enter the value of n: "))
sum= 0

for i in range(1,n+1):
    sum= float(sum+(1/(i*i*i)))
    
print(f"Sum of the given series: {sum:.4f}")
