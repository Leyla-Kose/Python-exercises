def largest_number():
  try:
    numbers = []
    num = int(input("Enter the 1st of 5 numbers: "))
    numbers.append(num)
    for i in range(4):
      number = int(input("Enter another number: "))
      if number > numbers[0]:
        numbers.insert(0, number)
      else:
        numbers.append(number)
    return numbers[0]
  except: 
    print("Invalid input, try again!")

largest_number()
