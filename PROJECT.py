a = -1
b = 0
max_num = 0
min_num = 0
while a != o :
    a = (input("What is the value? (type a to stop) "))
    b = b+a
    if  a > max_num:
        max_num = a
    if a<min_num and a!=0:
        min_num =a


print("Our total value is " + str(b))
print("The Max_num is " + str(max_num))
print("The min_num is " + str(min_num))





