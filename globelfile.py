''''
l = 10  # Global variable
def function(n):
  #  l = 5 # local variable
    m= 8 # local variable
    global l
    l= l+45
    print(m , l)
    print(n, "I have printed")
function("This is my line")
print(l)
'''
x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
    # print("Before calling rohan()", x)
    rohan()
    print("After calling rohan()", x )
harry()
print(x)