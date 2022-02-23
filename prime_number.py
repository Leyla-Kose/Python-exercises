def isPrime(x):
  n = 0
  if x > 1:
    for i in range(2, x):
      if x%i == 0:
        n = i
    if n == 0:
      return print(f'{x} is a prime number')
    else:
      return print(f'{x} is not a prime number')
  else:
    return print("Prime numbers can't be less than 1!")
      
isPrime(11)


'''
Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.

The examples of the desired output are as follows :

input →  19 ⇉ output : 19 is a prime number
input →  10 ⇉ output : 10 is not a prime number


'''