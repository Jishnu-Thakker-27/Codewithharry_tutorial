a=int(input("Enter Number 1: "))
b=int(input("Enter Number 2: "))
c=int(input("Enter Number 3: "))
d=int(input("Enter Number 4: "))

if(a>b and a>c and a>d ):
    print(f"The greatest number is {a}")
elif(b>a and b>c and b>d):
    print(f"The greatest number is {b}")
elif(c>a and c>b and c>d):
    print(f"The greatest number is {c}")
elif(d>a and d>b and d>c ):
    print(f"The greatest number is {d}")
else:
    print("Invalid Input")