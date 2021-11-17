def isPrime(x):
  n = 0
  if x > 1:
    for i in range(2, x):
      if x%i == 0:
        n = i
    if n == 0:
      print(f'{x} is a prime number')
    else:
      print(f'{x} is not a prime number')
  else:
    print("Prime numbers can't be less than 1!")
      
isPrime(11)
