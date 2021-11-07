
age =  input('Are you a cigarette addict older than 75 years old? Yes or No? ').lower()
chronic =  input('Do you have a severe chronic disease? Yes or No? ').lower()
immune = input('Is your immune system too weak? Yes or No? ').lower()

if (age == 'yes') or (chronic == 'yes') or (immune == 'yes'):
  print('You are in risky group.')
elif (age == 'no') and (chronic == 'no') and (immune == 'no'):
  print('You are not in risky group.')
else: 
  print('Try again!')
