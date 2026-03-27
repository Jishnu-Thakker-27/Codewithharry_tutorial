l1=[1, 4, 9, 234,34, 11]
# 
l1.sort()
print(l1)
# 
l1.reverse()
print(l1)
# 
l1.insert(3,355)  
'''first wirte the position of index  which you want to add( remmebr the index valjue starts with 0) then comma and then the number
u want to add #(index: SupportsIndex)'''
print(l1)  #[234, 34, 11, 355, 9, 4, 1]
#
print(l1.pop(2)) #it will print the value at index 2 i.e. 11
l1.pop(2)
print(l1)

# or we can do it in either way
# 
value=l1.pop(2)
print(value) #as string is mutable now the number at index 2 is 9 so 9 will come as output
# 
l1.remove(4) #here we have to add the number we have to remove and not the index value
print(l1)