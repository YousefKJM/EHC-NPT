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

