# CPSC526-EnrollmentSystem

enroll.py - enrolls the user if the username is not already enrolled and if the password is not relatively simple.

        To compile and run: python enroll.py username password
        key stretching is implemented but key strengthening is not implemented.
        username and password is not case sensitive.
        
authenticate.py - authenticates the user if the username is enrolled and the hashed password matches the password
    stored in the password file (enrolled.json).

        To compile and run: python authenticate.py username password
        username and password is not case sensitive.
        
enrolled.json - the password file consisting of the user's username followed by their hashed password and
        corresponding salt.
