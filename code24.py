def cont():
    print("Continue?")
    n= input()
    if(n=='Yes' or n=='Y' or n=='y'):
        print("True")
        return True
    else:
        print("False")
        return False

cont()
