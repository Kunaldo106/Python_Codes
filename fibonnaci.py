# to print the fibonnaci  upto n terms:

def fibonnaci(n):
    n1,n2=0,1
    for i in range(n):
        if(i==n-1):
            print(n1)
        n1,n2=n2, n1+n2
        
n= int(input("Enter the value of n:"))
fibonnaci(n)