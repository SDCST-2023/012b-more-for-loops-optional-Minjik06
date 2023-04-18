#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expectedUsername = "systemadmin"
expectedPassword = "master"
a=str(input("Enter the user's name: "))
if a==expectedUsername:
    b=str(input("Enter the user's password: "))
    if b==expectedPassword:
        print("")
