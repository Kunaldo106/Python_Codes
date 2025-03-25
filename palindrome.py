#to check a number is palindrome or not:

def is_palindrome(num):
    rev= 0
    
    while(num!=0):
        rem= num%10
        rev= (rev*10)+rem
        num=num//10
        
    return rev

num= int(input("Enter the numbers: "))
check=is_palindrome(num)
if(check==num):
    print(f"The number {num} is palindrome")
else:
    print(f"The number {num} is not palindrome")