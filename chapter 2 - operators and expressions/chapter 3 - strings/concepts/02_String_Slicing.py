name="Harry" #string length=5

'''If we go from Left To Right
H=0
a=1
b=2
r=3
r=3
y=4'''
'''If we go from Right To left
H=-1
a=-2
b=-3
r=-4
r=-5
y=-6'''

a=name[0:3]#[0:3]means 0 is inlcuded and 3 is not included so it means from 0 to 2   
           #it means select letters from string of name variable from 0 to 2. [0:3]
           # start from index 0 all the way till index 3 (excluding 3) 
     
print(a) #soltuion is Har

b=name[:5] #if nothing written means it is 0 (for first index) i.e.[0:5]
print (b) #Harry

c= name[0:] #if nothing written means it is string length (for last index) i.e.[0:5]
# and as last index is not included in 0:5 it means from 0 to 4 so whole harry will be solution

print(c) #Harry
 
d= name[1]
print(d) # a

e= name[1:4]
print(e) #arr