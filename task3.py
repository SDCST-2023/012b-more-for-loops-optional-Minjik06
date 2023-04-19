#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]

for i in range(3):
    a=str(input("Enter the user's name: "))
    if a==users[i]:
        b=str(input("Enter the user's password: "))
        if b==users[i]:
            print(f"{users[i]}'s password is {passwords[i]}")
            break
        else:
            print("Password is not a match!")
    else:
        print("Denied Users")
