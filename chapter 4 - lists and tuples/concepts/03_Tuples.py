# note that tuples are immutable

a= ( 12,3,4,5,False, "Rohan")
print(type(a)) #<class 'tuple'>

b=() #This is called empty tuple

c=(1)
print(type(c)) #<class 'int'>
#although i need to make a tuple but it shows as int type
#but if I want to make it a single term tuple, I need to add comma to it

d=(1,)
print(type(d)) #<class 'tuple'>
 
a[0]= 34 #this will not happen as tuples are immutable just like strings