#!/usr/bin/env python3
#Tells user if length of string entered is <10, <10 and >20 or >20
phrase = input("Write something here: ")
if len(phrase) < 10:
	print("Phrase of less than 10 characters")
elif len(phrase) <= 20:
        print("Phrase of 10 to 20 characters")
else:
        print("Phrase of more than 20 characters")
