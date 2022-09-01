# Strings in python are surrounded by either single or double quotation marks . let's  look at string formating and some string methodes

name = 'KAMAL'
age = 26

# Concatenate
print("Hello ,  My Name is "+name+'and i am ' +str(age))
# String Formatig

# Argument by position
print("My name is {name} and i am {age}". format(name=name,age=age))

# F-Strings
print(f' Hello My name is {name} and i am {age}')

# String ,ethodes
s = 'hello worlds'

# Capitalize string
print(s.capitalize())

# Make all Upper
print(s.upper())

# Make all Lower
print(s.lower())

# Swap Case
print(s.swapcase())

# Get Length
print(len(s))

# Replace
print(s.replace('worlds',  'everyone'))

# Count
sub ="h"
print(s.count(sub))

#Starts with
print(s.startswith('hello'))

#End with
print(s.endswith("s"))

# Split into a list
print(s.split())

#Find Position
print(s.find("r"))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabatic
print(s.isalpha())

#Is all numeric
print(s.isnumeric())
