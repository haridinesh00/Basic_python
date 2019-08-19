"""
Generate a password of 10 characters with letters symbols and numbers
choose an option to opt out or include caps, symbols, numbers
"""
import random
import string

def allFun():
	chars = string.ascii_uppercase + string.ascii_lowercase + '!@#$%^&*?'
	password = ''
	for c in range(10):
		password += random.choice(chars)
	print(password)

def Num():
	chars = string.ascii_lowercase + '1234567890'
	password = ''
	for c in range(10):
		password += random.choice(chars)
	print(password)

def sym():
	chars = string.ascii_lowercase + '!@#$%^&*?'
	password = ''
	for c in range(10):
		password += random.choice(chars)
	print(password)

def letters():
	chars = string.ascii_lowercase + string.ascii_uppercase
	password = ''
	for c in range(10):
		password += random.choice(chars)
	print(password)

def numSymb():
	chars = '1234567890!@#$%^&*?'
	password = ''
	for c in range(10):
		password+=random.choice(chars)
	print(password)


def capsSymb():
	chars = string.ascii_uppercase + '!@#$%^&*?'
	password = ''
	for c in range(10):
		password +=random.choice(chars)
	print(password)

def capsNum():
	chars = string.ascii_uppercase + '1234567890'
	password = ''
	for c in range(10):
		password+=random.choice(chars)
	print(password)

def generate():
	usr_inpC = input("Generate with caps? (y/n): ")
	usr_inpSymb = input("Generate pwd with sumbols? (y/n): ")
	user_inpNum = input("Generate pwd with numbers? (y/n): ")	

	if (usr_inpC == "y" and usr_inpSymb == "y" and user_inpNum == "y"):
		allFun()
	elif (usr_inpC == "y" and usr_inpSymb == "y" and user_inpNum == "n"):
		capsSymb()
	elif (usr_inpC == "y" and user_inpNum == "y" and usr_inpSymb == "n"):
		capsNum()
	elif (usr_inpC == "n" and usr_inpSymb == "y" and user_inpNum == "y"):
	  numSymb()
	else:
	   print("please enter the combination of any two option")
