#Write a Python program to guess a number between 1 to 9
import random
target_num, pick_num = random.randint(1, 10), 0
while target_num != pick_num:
	pick_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Correct Guess!')
