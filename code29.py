def palindrome(str1):
    og= str1.upper()
    rev= og[::-1]
    
    if(og==rev):
        return True
    else:
        return False
    
str1= input("Str1: ")
res= palindrome(str1)
if(res):
    print("palindrome")
else:
    print("Not Palindrome")


