num1 = int(input ("enter a first number:- "))
num2 = int(input("enter a second umber :- "))
condition = input("enter a condition  (+, -, *, / , %, **)  :- ")
if condition ==  "+":
    print( num1 + num2)
elif condition == "-":
    print(num1 - num2)
elif condition == '*':
    print(num1 * num2)
elif condition == "%":
    print(num1 % num2)
elif condition == "**":
    print(num1 ** num2)

else:
    print("please condition fill in the blank")

