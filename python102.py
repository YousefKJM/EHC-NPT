#!/bin/python3

#Importing
print("Importing is important:")

import sys #system functions and parameters

from datetime import datetime
print(datetime.now())

from datetime import datetime as dt #importing with an alias
print(dt.now())

def new_line():
	print('\n')

new_line()

#Advanced Strings
print("Advanced strings:")
my_name = "Yousef"
print(my_name[0]) #first initial
print(my_name[-1]) #last letter

sentence = "This is a sentence."

print(sentence[:4]) #first word
print(sentence[-9:-1]) #last word

print(sentence.split()) #split sentence by delimiter (space)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))

quoteception = "I said, 'give me all the money'"
print(quoteception)

quoteception = "I said, \"give me all the money\""
print(quoteception)

print("A" in "Apple") #it is boolean --> return True
letter = "a"
word = "Apple"
print(letter.lower() in word.lower()) #Improved - case insensitive

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower()))

too_much_space = "                  hello                      "
print(too_much_space.strip())

full_name = "yoef Majeed"
print(full_name.replace("yoef","Yousef"))
print(full_name.find("Majeed"))

car = "Mazda"
print("My favourite car is {}.".format(car))

def favourite_book(title, author):
	fav = "My favourite book is \"{}\". which is written by {}".format(title, author)
	return fav

print(favourite_book("The Great Gatsby", "F. Scott Fitz"))
