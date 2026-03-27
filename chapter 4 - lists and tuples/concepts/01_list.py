friends= ["apple","Jishnu",234,32.04,False]

print(friends[0])

friends[0]="Grapes" #unlike strings, lists are mutable

print(friends[0])

print(friends)  #['Grapes', 'Jishnu', 234, 32.04, False]
print(friends[1:4])
print(friends[1:])
print(friends[2:4])     #list indexing is just same as string slicing
print(friends[:])     
# 
friends.append("Harry")  #meaning of append is to add it at the last of the list
print(friends)
