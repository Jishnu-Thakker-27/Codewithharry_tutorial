a=int(input("Enter your age: "))

# If elif else ladder
if(a>=18):
    print("Your Age Is above consent")

elif(a<0):
    print("You are entering invalid age")
elif(a==0):
    print("You have enetred 0 which is an invalid age")    
else:
    print("Your age is below consent")