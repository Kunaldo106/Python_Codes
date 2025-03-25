def palindromecheck(num):   
    og=num
    rev=0
    while num>0:
        digit= num%10
        rev= rev*10 +digit
        num=num//10
    return rev
    
num= int(input("Enter the interger: "))
rev= palindromecheck(num)
print(rev)
if(num==rev):
    print(f"The number {num} is palindrome.")
else:
    print(f"the number {num} is not palindrome.")
