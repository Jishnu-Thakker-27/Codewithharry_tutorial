a=int(input("Enter your age: "))

# If statement no. 1
if(a%2==0):
    print("a is even")

# End of If Statement no. 1

# If statement no. 2
if(a>=18):
    print("Your Age Is above consent")

elif(a<0):
    print("You are entering invalid age")
elif(a==0):
    print("You have enetred 0 which is an invalid age")    
else:
    print("Your age is below consent")

# End of If Statement no. 2