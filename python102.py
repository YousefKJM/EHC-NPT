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


