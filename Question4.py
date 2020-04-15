#Write a Python program to check the validity of password input by users 
import re
z= input("Set Password ")
x = True
while x: 
    if (len(z)<6 or len(z)>12):
        break
    elif not re.search("[a-z]",z):
        break
    elif not re.search("[0-9]",z):
        break
    elif not re.search("[A-Z]",z):
        break
    elif not re.search("[$#@]",z):
        break
    elif re.search("\s",z):
        break
    else:
        print("valid password")
        x=False
        break
if x:
    print("Not a Valid Password")
