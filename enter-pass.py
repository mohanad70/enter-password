print('Who are you ..?')
count=0

while count < 3: 
	username=input('Enter the username:')
	password=input('Enter the password:')
	if username== 'mohanad' and  password=='123456':
		print('Welcome Back Mohanad ..')
		break
	elif count < 2:
		print('Access denied Try again..')
		count+=1
	elif count <3:
		print('you have been blocked')
		break
