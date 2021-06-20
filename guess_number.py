import random
r = random.randint(1 , 100)
count = 0
while True:
	count += 1
	guess = input('enter a number that you guess: ')
	guess = int(guess)
	if guess == r:
		print('you are right!!')
		break
	else:
		print('please try again!')
		if guess > r:
			print('bigger than the answer')
		else:
			print('smaller than the answer')
	print('This is the', count, 'time you guessed')