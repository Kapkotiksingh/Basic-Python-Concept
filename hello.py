# print("How Money Row You want to print")
# one = int(input())
# print("type 1 or 0")
# two = int(input())
# new = bool(two)
# if  new == True  :
#     for i in range(1,one+1):
#              for j in range(1,i+1):
#                   print("*", end = " ")
#              print()
# elif new == False:
# #     for i in range(one,0,-1):
# #         for j in range(1,i+1):
#             print("*" , end=" ")
#         print()


# print("Pattern Printing ")
# num = int(input("Enter num how money rows you want :-  "))
# print("ENTER 1 OR 0")
# bool_val = input("1 for True value or 0 for False:  ")
# if bool_val =="1":
#     for i in range(0,num+1):
#         print("* " * i)
# if  bool_val=="0" :
#     for i in range(num,0,-1):
#         print("*"*i)


# try :
#     n =int(input("Enter No. of Row : "))
#     b = int(input("Enter Patttern (0 or 1) :"))
#     if   b is 0:
#         count = 0
#         while(count<=n):
#             print("*" * count, end="")
#             print("/n", end="")
#             count = count+1
#
#     elif b is 1:
#         count = n
#         while(count!=0):
#             print("*" * count, end=" ")
#             print("/n",end=" ")
#             count= count-1
#
#     else:
#         print("Invlid")


#* statment
for number in range(1,10):
    print("Star",number,number*"*")
 