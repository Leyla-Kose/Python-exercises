def prime_numbers():
  num = int(input('Enter a number: '))
  prime_numbers = []
  if num <=1:
    return print('Try again!')
  else:
    for i in range(2, num+1):
      count = 0
      for j in range(2, (i//2)+1):
        if i%j==0:
          count+=1
          break
      if count==0:
        prime_numbers.append(i)             
  return prime_numbers

prime_numbers()

'''
Task : Print the prime numbers which are between 1 to entered limit number (n).

You can use a nested for loop.
Collect all these numbers into a list
The desired output for n=100 :

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
61, 67, 71, 73, 79, 83, 89, 97]


'''