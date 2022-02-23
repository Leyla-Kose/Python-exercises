def is_at_risk():
  age =  input('Are you a cigarette addict older than 75 years old? Yes or No?: ').lower()
  chronic =  input('Do you have a severe chronic disease? Yes or No?: ').lower()
  immune = input('Is your immune system too weak? Yes or No?: ').lower()

  if (age == 'yes') or (chronic == 'yes') or (immune == 'yes'):
    return 'You are in risky group.'
  elif (age == 'no') and (chronic == 'no') and (immune == 'no'):
    return 'You are not in risky group.'
  else: 
    return 'Try again!'

is_at_risk()

'''
Problem :
Task : Estimating the risk of death from coronavirus.
Consider the following questions in terms of True/False regarding anyone else.
Are you a cigarette addict older than 75 years old? Variable → age
Do you have a severe chronic disease? Variable → chronic
Is your immune system too weak? Variable → immune
Set a logical algorithm using boolean logic operators (and/or) and the given variables in order to give us True (there is a risk of death) or False (there is not a risk of death) as a result.

'''
