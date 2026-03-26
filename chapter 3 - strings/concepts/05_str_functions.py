name="Jishnu"

print(len(name)) #6
print(name.endswith("rry")) #False
print(name.endswith("shnu")) #True
print(name.startswith("shnu")) #False
print(name.startswith("Jish")) #True
print(name.startswith("ish")) #False
print(name.startswith("jish")) #False (this function is case sensitive)
print(name.replace("Jishnu", "Harsh")) #Harsh

s ="  Hello World 123\n"

# 🔹 Basic String Information
print(len(s))               # 18 (because it also consider \n as whole index)
print(s.count("l"))         # 3  (there are three l in s)
print(s.find("World"))      # 8  (at which position of the word World starts)
print(s.index("Hello"))     # 2  (at which position of the word Hello starts)

'''index and find are the same but  find gives -1 if not found and index gives but
 raises an error if not found.'''
#  for example

print(s.find("Jishnu")) #-1
#print(s.index("Jishnu")) #generates an error

# 🔹 Changing Case
print(s.upper())            # "  HELLO WORLD 123\n" ( every letter in upper case)
print(s.lower())            # "  hello world 123\n" ( every letter in lower case)
print(s.title())            # "  Hello World 123\n" (Capitalizes first letter of each word.)
print(s.capitalize())       # "  hello world 123\n" (Capitalizes first letter of the string.)
'''Here as the first letter of s is a wide space we cannot see h capital'''
print(s.swapcase())         # "  hELLO wORLD 123\n" (Swaps uppercase to lowercase and vice versa.)

print(name.capitalize())

# 🔹 Removing / Stripping
print(s.strip())            # "Hello World 123"
print(s.lstrip())           # "Hello World 123\n"
print(s.rstrip())           # "  Hello World 123"

# 🔹 Checking String Content
print(s.strip().isalpha())  # False
print("Hello".isalpha())    # True
print("123".isdigit())      # True
print("Hello123".isalnum()) # True
print("   ".isspace())      # True
print("HELLO".isupper())    # True
print("hello".islower())    # True
print("Hello World".istitle()) # True

# 🔹 Replacing & Splitting
print(s.replace("World", "Python"))  # "  Hello Python 123\n"
print(s.split())                     # ['Hello', 'World', '123']
print(s.splitlines())                # ['  Hello World 123']
print("-".join(["2025", "09", "28"]))# "2025-09-28"

# 🔹 String Alignment & Formatting
print("Hi".center(10, "*"))   # "***Hi*****"
print("Hi".ljust(10, "-"))    # "Hi--------"
print("Hi".rjust(10, "-"))    # "--------Hi"
print("42".zfill(5))          # "00042"

name = "Jishnu"
age = 20
print("My name is {} and I am {}".format(name, age))
print(f"My name is {name} and I am {age}")   # f-string

# 🔹 Checking Start/End
print(s.startswith("  He"))   # True
print(s.endswith("123\n"))    # True

