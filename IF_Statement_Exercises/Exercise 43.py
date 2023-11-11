a = int(input('Please enter the value of an US dollar note:'))

b = ""

if a == 1:
	b = 'George Washington'
elif a == 2:
	b = 'Thomas Jefferson'
elif a == 5:
	b = 'Abraham Lincoln'
elif a == 10:
	b = 'Alexander Hamilton'
elif a == 20:
	b = 'Andrew Jackson'
elif a == 50:
	b = 'Ulysses S. Grant'
elif a == 100:
	b = 'Benjamin Franklin'
 
if b == '':
	print('Sorry that is not a valid US dollar note.')
else:
	print('On that note you will find:',(b))