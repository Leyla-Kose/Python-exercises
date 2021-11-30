num = int(input('Enter a number: '))
prime_numbers = []
if num <=1:
  print('Try again!')
else:
  for i in range(2, num+1):
    count = 0
    for j in range(2, (i//2)+1):
      if i%j==0:
        count+=1
        break
    if count==0:
      prime_numbers.append(i)         
      
print(prime_numbers)
