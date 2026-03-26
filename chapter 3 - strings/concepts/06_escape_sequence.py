a="Jishnu is a good boy \n but not a bad boy"  # \n new line ke liye
b="Jishnu is a good boy \n but not a bad\tboy" # \t tab jitni space de deta hai
c="Jishnu is a \"Good\" \n but not a \"bad\" boy" 
'''when i want that some words in 
output should be in "..." form i need to write it in \"...\" in the input so that 
compiler do not get confused in string close " and " for output'''

# if string is written in '..' form then "" can be recognized for ouput but then 
# for '' we need to write \'...\'

d= "Jishnu is \\" #when i want to print \ in the output i need to input \\ 
print(a)
print(b)
print(c)
print(d) #Jishnu is \


# Newline
print("Hello\nWorld")      
# Output:
# Hello
# World

# Tab (adds spaces)
print("Hello\tWorld")      
# Output: Hello    World

# Backslash
print("This is a backslash: \\")  
# Output: This is a backslash: \

# Single quote
print('It\'s Python')      
# Output: It's Python

# Double quote
print("He said: \"Hello\"") 
# Output: He said: "Hello"

# Carriage return (moves cursor to start of line)
print("Hello\rWorld")      
# Output: World

# Backspace (removes one character)
print("Hello\bWorld")      
# Output: HellWorld

# Form feed (rare, moves to next page in printers)
print("Hello\fWorld")      

# Vertical tab (moves cursor vertically down)
print("Hello\vWorld")      

# Unicode escape (character by code point)
print("\u03A9")            # Output: Ω  (Greek Omega)

# Hexadecimal escape
print("\x41")              # Output: A
