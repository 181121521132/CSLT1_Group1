human_age = int(input('Input human years: '))

if human_age < 0:
	print('Age must be positive')
	
elif human_age <= 2:
	dog_age = human_age * 10.5
else:
	dog_age = (human_age - 2)*4 + 21 #21= 2 năm đầu * 10,5

print('The dog age is', dog_age)