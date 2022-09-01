# A Variable is a container for a value , which can be of various types

''' 
This is a 
multiline comment
or docstring (used a define a function purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
 - Variable names are case sensitive (name and Name are diffrent variables)
 - Must start with a letter or an underscore
 - Can have numbers but can not start with one 
"""

from operator import is_


x = 1          # int
y = 2.5        # float
name= "john"   # str
is_cool = True # bool

# Multiple assigement

x,y,name,is_cool = (1,2.5,"john",True)

# Basic Math
a= x * y

# Casting
x = str(x)
y = int(y)
z = float(y)

print(type(x))
print(type(y))
print(type(z))
