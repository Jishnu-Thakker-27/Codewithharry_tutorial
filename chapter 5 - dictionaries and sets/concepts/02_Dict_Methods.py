a = { 
    "key": "value",
# left side of colon is called key and right is called value
    "harry": "code",
    "marks": "100", 
    "list": [1, 2, 9],
    "Jishnu": "99"
    }

print(a.items())
print(a.keys())
print(a.values())

a.update({"harry": "99"})   #dictionaries are mutable
print(a)   

# also we can add keys and values through update command
a.update({"harsh":"56"})
print(a) 

# i can add a new key and its value and also change  the value of existing key in same update command
a.update({"harsh":"78", "Manisha":"33"})
print(a)

print(a.get("harry"))
print(a["harry"])

# both way we can find value of key but....

print(a.get("harry2")) #give none as output if no such key is present
print(a["harry2"]) #error will occur and no output given if no such key is present

