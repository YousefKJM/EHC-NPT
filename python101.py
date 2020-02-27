#!/bin/python3

#Print string
print("Strings and things:")
print('Hello, world!')
print("""Hello, this is
a multi-line string!""")
print("This is"+"a string")

print('\n') #new line

#Maths 
print("Math time:")
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo
print(50 // 6) #number without leftovers

print('\n') #new line

#Variables & Methods
print("Fun with variables and methods:")
quote = "All is fair in love and war"
print(len(quote)) #length
print(quote.upper()) #uppercase
print(quote.lower()) #lower
print(quote.title()) #title

name = "Yousef"
age = 22 #int int(22)
gpa = 3.7 #float float(3.7)

print(int(age))
print(int(22.9)) #dose not round

print("My name is " + name + " and I am " + str(age) + " years old.")

print('\n') #new line

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n') #new line

#Functions
print("How, some functions:")
def who_am_i():
	name = "Yousef"
	age = 22
	print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

#adding in parameters
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

#add in muliple parameters
def add(x,y):
	print(x + y)

add(7,7)
add(305,207)

#Using return
def multiply(x,y):
	return x * y
print(multiply(7,7))

def squre_root(x):
	return x ** .5

print(squre_root(64))

print('\n') #new line

#Boolean expression (True or false)
print("Boolean expression:")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

#Relational and Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7
print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and = (7 > 5) and (6 < 7)
test_or = (7 > 5) or (5 < 7)
test_not = not True
print(test_and, test_or, test_not)

print('\n') #new line

#Conditional Statements
print("Conditional Statements:")
def soda(money):
	if money >= 2:
		return "You've got yourself a soda!"
	else: 
		return "No soda for you!"
print(soda(3))
print(soda(1))

def smoking(age,money):
	if(age >= 21) and (money >= 5):
		return "We're gettin tipsy!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money"
	elif (age < 21) and (money >= 5):
		return "Nice try, kid."
	else:
		return "You're too poor and too young"

print(smoking(21, 5))
print(smoking(21, 4))
print(smoking(20, 5)) 
print(smoking(20, 4))

print('\n') #new line

#Lists
print("Lists have brackets:")
fruit = ["Apple", "Orange", "Blue", "Green"]
print(fruit[0])
print(fruit[0:3])
print(fruit[1:])
print(fruit[:1])
print(fruit[-1])
print(len(fruit))

fruit.append("Yellow")
print(fruit)

fruit.pop()
print(fruit)

fruit.pop(1)
print(fruit)

fruit = ["Apple", "Orange", "Blue", "Green"]
person = ["Yousef", "Jake", "Ahmed", "Khalid"]
combined = zip(fruit, person)
print(list(combined))

fruit = ["Apple", "Orange", "Blue", "Green"]
person = ["Yousef", "Jake", "Ahmed"]
combined = zip(fruit, person)
print(list(combined))

#Tuples
print("Tuples have parentheses and cannot change")
grades = ("A", "B", "C", "D", "F")
print(grades[1])

