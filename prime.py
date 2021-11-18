def isPrime(num):
  if num > 1:
    n = 0
    for i in range(2, (num//2)+1):
      if num % i == 0:
        n = i
        break
    if n == 0:
      print(f'{num} is a prime number')
    else:
      print(f'{num} is not a prime number')
  else:
    print('Numbers less then 2 are not prime numbers!')    


isPrime(37)

