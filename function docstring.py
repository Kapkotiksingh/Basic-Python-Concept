# a =  9
# b =  7
# c = sum((a,b)) #bult in Function

def function1(a , b):
    """This is a function which will calculater  average of two number"""
    print("Hello you are in function 1 " ,a+b)
# print(function()) # None
function1(5,6)
print(function1.__doc__)

def function2(a,b):
    average= (a+b)/2
    print(average)
    return average
v= function2(5, 7)
print(v)