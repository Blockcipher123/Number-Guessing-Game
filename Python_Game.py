
# importing python module
import random


# generating random no to com
c = random.randint(1,5)
print(c)

# welcomeing the use in the game
print('Welcome to this game!')

# some warning for use
print('''
Warning!
Rember :D u will get 2 chance to guess the number 
if u will fail then it will quite automatically 
Thanks, 
Good luck :D
	''')

# taking input to use to guess the no
num = int(input('Guess the number between 1 to 5  : '))

# running the while loop 
while True:
	if c == num: # condition if the user guess the right no or not
		print('''wow! u win cool man ._. :))
			''')
		break
	elif c > num: # if user no is less 
		print('Wrong, Too low')

	else: 
		print('Wrong, Too high') # if user no is big 


	# 1 guess
	n = int(input('Guess again : '))
	if c == n:
		print('''wow! u win cool :D ._. :))''') # if user guess the right no 
		break
	elif c > n:
		print('Wrong, Too low') # if user guess is low 
		print('lol')
		break

	else:
		print('Wrong, Too high') # if user guess is big
		print('lol')
		break


	# if user guess the write no then it'll break the look and exit the game
	if c == num:
		break
	if c == n:
		break


# 
#  			'''''''''''''''__________________________''''''''''''''''
#  			'''''''''''''''__________________________''''''''''''''''
# 
# 				           ````___`````  '''''''___''''''
# 	
# 								   (: Thanks :)
