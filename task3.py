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
    if a in users:
        b=str(input("Enter the user's password: "))
        if b in passwords:
            if users.index(a)==passwords.index(b):
                print(f"{a}'s password is {b}")
                break
            else:
                print(f"{a}'s password is not {b}")
        else:
            print(f"{b} is invalid password")
    else:
        print("Denied Users")


"""for i in range(3):
    a=str(input("Enter the user's name: "))
    if a in users and b in passwords:
        b=str(input("Enter the user's password: "))
        if users.index(a)==passwords.index(b):
            print(f"{a}'s password is {b}")
            break
        else:
            print(f"{a}'s password is not {b}")
    else:
        print("Denied Users")"""
