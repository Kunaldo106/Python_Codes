num= list(map(int,input("Enter the intergers in the list: ").split()))

l= list(sorted(num))
print("Second Min:",l[1])
print("Second Max:",l[-2])
