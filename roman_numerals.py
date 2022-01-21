
roman_numerals = {0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IV', 10:'X',
 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC', 100:'C', 200:'CC', 300:'CCC', 
 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM', 1000:'M', 2000:'MM', 3000:'MMM'}
while True:
    entry = input('Enter a number: ')
    if entry.lower() == 'exit':
      print('Exiting the program... Good Bye')
      break
    if not entry.isdigit():
        print("Not a valid input!!!")
        continue
    number = int(entry)
    if number < 1 or number > 3999:
        print("Not a valid input!!!")
        continue
    n = len(str(number))
    if n == 1:
        print(roman_numerals[number])
    elif n == 2:
        print(roman_numerals[int(str(number)[0])*10] + roman_numerals[number%10])
    elif n == 3:
        print(roman_numerals[int(str(number)[0])*100] + roman_numerals[int(str(number)[1])*10] + roman_numerals[number%10])
    elif n == 4:
        print(roman_numerals[int(str(number)[0])*1000] + roman_numerals[int(str(number)[1])*100] + roman_numerals[int(str(number)[2])*10] + roman_numerals[number%10])

