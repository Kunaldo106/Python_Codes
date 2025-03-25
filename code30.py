# WAP to design a FLAME game

name1= input("Enter the name: ")
name2= input("Enter the name: ")

num= len(name1)
num2= len(name2)
length= num+num2
count=0

for i in name1:
    if(i in name2):
        count+=1

res= count*2

fcount=length-res

rcount= (fcount%5)-1

string="FLAME"
print(string[rcount])
    