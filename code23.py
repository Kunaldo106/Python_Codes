
def compoundInterest(P,r,n,t):
    A=P*(1+r/n)**(n*t)
    CI= A-P
    return A, CI

P=float(input("Principle Amount: "))
r=float(input("Interest rate(%): "))/100
n=float(input("No. of times the interest is compounded: "))
t=float(input("No.of years: "))

FinalAmount, CI=compoundInterest(P,r,n,t)

print(f"Final Amount: {FinalAmount:.2f}")
print(f"Compound Interest: {CI:.2f}")
