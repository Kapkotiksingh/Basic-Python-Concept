# A list is a callection which is ordered  and changeable . Allows Duplicate members.

#Creat list
numbers =[1, 2, 3, 4, 5]
fruits =['Apple', 'Orange','Grapes', 'Pears']

#Use a constructor
nmbers2 =list((1, 2, 3, 4, 5 ))
print(numbers,nmbers2)

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mango')
print(fruits)

# Remove for lit
fruits.remove('Pears')
print(fruits)

# Insert into Position
fruits.insert(2,'Strawbarries')
print(fruits)

# Change the Values
fruits[0] = 'Blueberries'

#Remove with pop
fruits.pop(4)
print(fruits)

#Reverse  list
fruits.reverse()
print(fruits)

# short list
fruits.sort(reverse=True)
print(fruits)

