n = input('Enter a number: ')
sum = 0

if not n.isdigit():
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
  for i in n:
    sum += int(i)**len(n)
  
  if int(n) == sum:
   print(f'{n} is an Armstrong number!')
  else:
    print(f'{n} is not an Armstrong number!')

