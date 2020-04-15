#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20  
a = int(input("enter a number:"))
b = int(input("enter another number:"))
x = a + b
if x >= 15 and x <= 20:
    print(20)
else:
    print (x)
