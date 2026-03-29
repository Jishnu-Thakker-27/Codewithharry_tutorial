d={} #Empty Dictionary
a = { 
    "key": "value",
# left side of colon is called key and right is called value
    "harry": "code",
    "marks": "100", 
    "list": [1, 2, 9],
    "Jishnu": "99"
    }

print(a)
print(a, type(a))
# print(a[0])
#   this will show error because unlike string,tuples,lists its indexing doesnt 
# go as per 0,1,2,3.. it goes as per the key and gives value

print(a["harry"]) #code
print(a["Jishnu"]) #99
