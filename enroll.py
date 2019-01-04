import argon2
import json
import re
import sys
import random

##########################
##
## 	Program: enroll.py
## 	Name: Shanel Sayson
## 	ID: 10073474
##
##########################

## initialize variables
username = sys.argv[1]
password = sys.argv[2]

## variables for checking the passwords
## [numword] and [wordnum]
numFirst = bool(re.search(r'^\d+', password))
wordLast = re.search(r'[a-z]+$', password)
numLast = bool(re.search(r'\d+$', password))
wordFirst = re.search(r'^[a-z]+', password)

## argument check
if(len(sys.argv) < 3):
	print("rejected.")
	print("usage: python enroll.py username password")
	sys.exit(-1)
if(len(sys.argv) > 3):
	print("rejected.")
	print("usage: python enroll.py username password")
	sys.exit(-1)

# get dictionary words
dictionary = open("words.txt", 'r')
lines = dictionary.read().split("\n")

## check the last word of the password, if it is in the
## dictionary, return True otherwise False
def check_lastword():
	if wordLast is not None:
		if wordLast.group() in lines:
			return True
	else:
		return False

## check the first word of the password, if it is in the
## dictionary, return True otherwise False
def check_firstword():
	if wordFirst is not None:
		if wordFirst.group() in lines:
			return True
	else:
		return False

## check the password
## 	-	if password is all digits, return True
## 	-	if password is a word in the dictionary, return True
## 	-	if password is [numword], return True
## 	-	if password is [wordnum], return True
def check_pwd(password):
		#check all ints
		if(password.isdigit()):
			return True
		if(password in lines):
			return True
		if(numFirst and check_lastword()):
			return True
		if(check_firstword() and numLast):
			return True

## check the username
##  -	if username is already enrolled, return True
def check_user(username):
	try:
		with open("enrolled.json", 'r') as data: #remember to change
			users = json.load(data)
			if username in users:
				return True
	except:
		""
## enroll the user
## 	-	generates a random salt
##  -	hashes the password with that salt
##	-	dumps the updated information into json file
def enroll(username):
	enrolledUsers ={}

	try:
		enrolledUsers = json.load(open('enrolled.json'))
	except:
		""
	salt = generate_salt()

	## key stretching: to be stored in password file
	## the digest
	## keep this digest for authentication and store the hash chain into the password file
	digest = str(argon2.argon2_hash(password, salt))

	## key strengthening
	#strongDigest = str(argon2.argon2_hash(digest, salt, 100))

	## store the digest into the password file and write it
	enrolledUsers[username] = {
		#"PASSWORD": hashedPwd, "SALT": salt
		"PASSWORD": digest, "SALT": salt
	}

	enrolledUsers.update(enrolledUsers)

	with open("enrolled.json", 'w') as out:
		json.dump(enrolledUsers, out)

## generates a random salt
def generate_salt():
	salt = ""
	for i in range(0, 15):
		salt += str(random.randint(0,9))
	return salt

## initialize program
def main():
	# check if username is already enrolled and if the password is simple
	# print rejected if so, otherwise enroll the user
	if(check_pwd(password) or check_user(username)):
		print("rejected.")
		sys.exit(-1)
	else:
		print("accepted.")
		enroll(username)
		sys.exit(0)

if __name__ == "__main__":
	main()