import random

num= random.randint(1,10)

while(1):
    guess= int(input("Enter your guess(1-10): "))
    if(num==guess):
        print("waaaw!!!!,Your are correct!")
        exit()
    elif(num>guess):
        print("Oooops!!!,Too low")
    else:
        print("Oooops!!!,Too high")
