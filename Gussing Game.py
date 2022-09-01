'''
What is Python ?
Python is a very popular programming language . It was created by Guido Van Rossum ,and released in 1991.
it is used for:
web development
software development,
mathematics
system scripting

Variables :- Variables are container for storing data values.
Variable Name :- A variable name must start with a letter or the underscore character
                              A variable name can only contain alpha-numeric,
                            characters and underscore (A-z, 0-9, and_)
                            Variable names are case-sensitive(age,Age and AGE are three different variables

Python Casting

Specify a Variable type
The may be times when you want to specify a type on to a variable. This can be done with casting . Python is an
 object-orientated language ,and as such it uses classes t0 define data types , including its primitive type.
 int
 float
 str

 Python String:-
 Strings in Python are surrounded by either single quotation maks , or double quotation marks.

Slicing String:-
You can return a range of characters by using the slice syntax
Specify the start index and the ens index separated by a colon , to return a part of the string.
print(a[1:2:4]


Python Format string:-
As we learned in the python Variables chapter we cannot combine string and numbers like this :
quantity = 3
itemno = 567
price  = 34.33
myorder I want to pay {2} dollars for {0} pieces of items{1};"

print(myorder.format(quantity , itemno, price))


Escape Characters :-
To insert characters that are illegal in a string ,use an escape character.
An escape character is a backslash '' \''
 followed by the character you want to inside
 \, \\, \n, \r, \t, \b, \f , \ooo \xhh






'''

print( "Hello World!" )

print()

if 5>2:
      print("Five is Greater then two")


quantity = 3
itemno = 567
price  = 34.33
my0rder = " I want to pay  {2} dollars for  {0} pieces of items  {1}  ."

print(my0rder.format(quantity , itemno, price))