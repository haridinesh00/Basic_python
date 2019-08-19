"""
Generate a password of 10 characters with letters symbols and numbers
choose an option to opt out or include caps, symbols, numbers
"""
import random
print("Date a SouthIndian so that it can be a strong password!!!")
usr_inpC = raw_input("Generate with caps? : y/n")
usr_inpSymb = raw_input("Generate pwd with sumbols? : y/n")
user_inpNum = raw_input("Generate pwd with numbers? : y/n")

print (usr_inpC+"\n"+usr_inpSymb+"\n"+user_inpNum)

def allFun():	
	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*?'
	password = ''
	for c in range(10):
		password += random.choice(chars)
	print(password)

def Num():	
	chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
	password = ''
	for c in range(10):
		password += random.choice(chars)
	print(password)

def sym():	
	chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*?'
	password = ''
	for c in range(10):
		password += random.choice(chars)
	print(password)

def letters():	
	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?'
	password = ''
	for c in range(10):
		password +=random.choice(chars)
	print(password)

def capsNum():	
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	password = ''
	for c in range(10):
		password+=random.choice(chars)
	print(password)


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
	



