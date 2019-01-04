import sys
import json
import argon2

##########################
##
## 	Program: authenticate.py
## 	Name: Shanel Sayson
## 	ID: 10073474
##
##########################

# initialize variables
username = sys.argv[1]
password = sys.argv[2]

## argument check
if(len(sys.argv) < 3):
	print("rejected.")
	print("usage: python authenticate.py username password")
	sys.exit(-1)
if(len(sys.argv) > 3):
	print("rejected.")
	print("usage: python authenticate.py username password")
	sys.exit(-1)

## check the username
##  -   if username is already enrolled, return True
def check_user(username):
    try:
        with open('enrolled.json') as data:
            users = json.load(data)

            if username in users:
                return True
            else:
                return False
    except:
        ""

## log the user in
##  -   check the users hased password with their password
##  -   if equal, grant access
##  -   else, deny access
def user_login(username, password):
    try:
        with open('enrolled.json') as data:
            users = json.load(data)
            userSalt = users[username]['SALT']
            userPwd = users[username]['PASSWORD']
            hashedPwd = str(argon2.argon2_hash(password, userSalt))

            if(hashedPwd == userPwd):
                print("access granted.")
            else:
                print("access denied.")

    except:
        ""
## initialize program
## if username is not in users, deny access
## otherwise, grant access

if(check_user(username) == False):
    print("access denied.")
else:
    user_login(username, password)
