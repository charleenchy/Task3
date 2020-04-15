# Task3

#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
for k in range(1500,2701):
  if(k%7==0 and k%5==0):
     print(k)

#Write a Python program to convert temperatures to and from celsius, fahrenheit 
ans=int(input("1 for cel to Fah, 2 for Fah to cel"))
If ans == 1:
	cel = int(input("enter a temp in cel"))
	fah = (cel - 9/5) + 32
	print('%.2f Celsius is: %.2f Fahrenheit' %(cel, fah))
else:
	fah = int(input("yourtemp in Fah"))
	cel = (fah - 32) * 5/9
	print('%.2f Fahrenheit is: %.2f Celsius' %(fah, cel))

#Write a Python program to guess a number between 1 to 9
import random
target_num, pick_num = random.randint(1, 10), 0
while target_num != pick_num:
	pick_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Correct Guess!')

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

#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20  
a = int(input("enter a number:"))
b = int(input("enter another number:"))
x = a + b
if x >= 15 and x <= 20:
    print(20)
else:
    print (x)
