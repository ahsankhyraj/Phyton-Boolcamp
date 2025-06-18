# print("Hello World")

## Arithmetic operators
# print(10 + 5)
# print(10 - 5)
# print(10 * 5)
# print(10 / 5)
# print(9 // 5)
# print(9 % 5) # modulo
# print(9 ** 2) # Exponent

# print (5 - 2 * 3)

# print ((2+3)*(5+5))

# # Varaibles

# zohair = 5

# x = 3
# y = 5
# z=x+y
# z=z+5
# z+=5
# z-=5
# print(z)

# x = 5
# y = (2*x**2+3*x-1) / (1-x)
# print (y)

# # data types
# 1. integer 5, 10, 200
# 2. strings "abc", helloe world", "a"
# 3. float 5.6 2.3 100.7
# 4. boolean true, false

# a = ""hello"
# print (type(a))

## Sting

# my_var = "Hello"
# my_var2 = 'World'
# my_var3 = 'This is Ahsan's computer'
# my_var4 = "This is Ahsan's computer"
# my_var5 = 'This is Ahsan\'s computer'

## String  Concatenation

# var1 = "Hello"
# var2 = "World"

# print (var1+"  "+var2)


# var1 = "Hello"
# var2 = "World"

# print (var1+"  "+var2)


# var3 = "Number"
# var4 = "4"
# print (var3+var4)

## Type Conversion

# a=4
# print (type(a))
# print (a)
# b= str(a)
# print (type(b))
# print (b)

# var3 = "Number"
# var4 = "4"
# var5 = " + "
# print (var3+var5+var4)

# val_a = 4
# val_b = "4"
# print (val_a+int(val_b))

## Indexing on string:

# my_name = "Zohair"
# print(my_name[0], my_name[-1])
# print(my_name[-1])
# print(my_name[0]+ my_name[-1])
# print(my_name[0]+ my_name[-1])


# Slicing on String:
# a[start:end;Jump]

# 012345
# -6-5-4-3-2-1

# a = "Zohair"

# print(a[1:4]) 

# a = "Zohair"

# print(a[::3]) 

# Basic String Operations:

# - Concatenation: "Hello" + " World" → "Hello World"
# - Repetition: "Hello" * 3 → "HelloHelloHello"
# - Indexing: "Hello"[1] → "e"
# - Slicing: "Hello"[1:4] → "ell"
# Useful String Methods:
# - Changing Case:
# - .upper() → Converts to uppercase
# - .lower() → Converts to lowercase
# - .title() → Converts to title case
# - .swapcase() → Swaps case
# - Finding and Replacing:
# - .find("lo") → Returns index of substring
# - .replace("Hello", "Hi") → Replaces substring
# - Splitting and Joining:
# - "Hello World".split(" ") → ["Hello", "World"]
# - "-".join(["Hello", "World"]) → "Hello-World"
# - Stripping Whitespace:
# - .strip() → Removes leading/trailing spaces
# - .lstrip() → Removes leading spaces
# - .rstrip() → Removes trailing spaces

# a = input("Your First Name: ")
# b = input("Your Last Name: ")
# c = a + " " + b
# print(c)

# x = input("Enter Your Lucky No.")
# print(type(x))  # Output: <class 'int'>

# take 2 numbers as input from user and print the sum of it

# a = input("First no.: ")
# b = input("Second : ")
# c = a + b
# print(c)

# # Taking input from the user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# # Calculating the sum
# sum_result = num1 + num2

# # Printing the result
# print("The sum of", num1, "and", num2, "is:", sum_result)


# take user's name and anage as a input and print in the following way'
# ''
# 'my name is <name> and i am <age> year old'

# # Taking input from the user
# name = input("Enter your name: ")
# age = input("Enter your age: ")

# # Printing the result
# print(f"My name is {name} and I am {age} years old.")

# # Printing the result
# print("My name is",name," and I am ",age," years old.")

# Evaluating


# calculation program in 2 lines
# user_input = input ("enter your expression:")
# print(eval(user_input))

# Collections

# List
# Dictionary
# Tuple
# Set

# List
# - Any Data Type
# - Can Be Change
# - any number of values

# my_first_list = [1,2,3,4,5]
# my_second_list = ["one","Two","Three"]
# my_forth_list = [True,False,True,False,]
# my_fifth_list = [2.0,3.5,4.0,5.0]
# my_six_list = [1, "one",2,"Two",3,"Three"]
# nested_list = [[1,2,3,4,5], ["True","False"],[True,False,]]
# nested_list2 = [my_first_list,my_second_list, my_forth_list,my_fifth_list,my_six_list,]
# print (nested_list2)

# indexing on list
# make a list of fruits and print the second
# and second last fruit

# # List of fruits
# fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# # Print the second fruit (index 1) and second last fruit (index -2)
# print(fruits)
# print("Second fruit:", fruits[1])
# print("Second last fruit:", fruits[-2])

# slicing on list
# make a list of fruits and print the first 3
# and last 3 fruits

# List of fruits
# fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# Print the first 3 fruits
# print(fruits)
# print("First 3 fruits:", fruits[:3])

# # Print the last 3 fruits
# print("Last 3 fruits:", fruits[-3:])


# Methods on list

# Here’s a quick tour of some common and handy list methods in Python, using a fruit basket as our example:
fruits = ['apple', 'banana', 'cherry']

# 1. append()
# Adds an item at the end.
# fruits.append('date')  # ['apple', 'banana', 'cherry', 'date']
# print(fruits)

# 2. insert()
# Inserts an item at a given position.
# fruits.insert(1, 'blueberry')  # ['apple', 'blueberry', 'banana', 'cherry']
# print(fruits)

# 3. remove()
# Removes the first matching value.
# fruits.remove('banana')  # ['apple', 'cherry']
# print(fruits)


# 4. pop()
# Removes and returns an item by index (default is last).
# fruits.pop()  # Removes 'cherry'
# print(fruits)

# 5. sort()
# Sorts the list in place.
# fruits.sort()  # Alphabetical order
# print(fruits)

# 6. reverse()
# Reverses the list in place.
# fruits.reverse()
# print(fruits)

# 7. index()
# Returns the index of the first occurrence of a value.
# position = fruits.index('apple')
# print(position)

# 8. count()
# Counts how many times a value appears.
# count = fruits.count('apple')
# print(count)

# 9. clear()
# Removes all items from the list.
# fruits.clear()  # []
# print(fruits)

# Want to play around with some examples or see how these behave with different inputs? I’ve got code and snacks ready 🍎💻. Let's keep going!

# nest = [1, 2, 3, [4, 5, ["target"]]]
# print(nest[3][2][0])

fruits = ["apple", "banana", "cherry", "mango"]

# Print all fruits
# for fruit in fruits:
# print('banana in fruits:', 'banana' in fruits)
# print('bananas in fruits:', 'bananas' in fruits)
# chars = 'abcdefghikklmnopqrstuvxy'
# print ('a in chars:','a' in chars)
# print ('z in chars:','z' in chars)

# Dictionary
# 1- Mutable
# 2- Unordered
# 3- Indexed

# my_dict  = {'name':'John Doe',
#             'age':30,
#             'city':'New York'}

# print(my_dict['name'],my_dict['age'],my_dict['city'],sep="\n")

# names = ['John Doe', 'Jane Doe', 'John doy']
# cities = ['NY', 'LA', 'CA']
# ages = [30, 29, 40]

# # Print the second person’s data (index 1)
# index = 1
# print(f"{names[index]} lives in {cities[index]} and is {ages[index]} years old.")

# names = ['John Doe', 'Jane Doe', 'John doy']
# cities = ['NY', 'LA', 'CA']
# ages = [30, 29, 40]

# # Ask the user which record they want to see
# index = int(input("Enter a number from 0 to 2 to see a person's info: "))

# # Display the selected person's information
# if 0 <= index < len(names):
#     print(f"{names[index]} lives in {cities[index]} and is {ages[index]} years old.")
# else:
#     print("Invalid index. Please enter a number between 0 and 2.")