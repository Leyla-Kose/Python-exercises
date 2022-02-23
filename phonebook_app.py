def phonebook():
  print('Welcome to the phonebook application')
  phonebook = {}
  
  while True:
    phonebook_menu = '1. Find phone number \n2. Insert a phone number \n3. Delete a person from the phonebook \n4. Terminate'
    print(phonebook_menu)
    selection = input('Select operation on Phonebook App (1/2/3): ')
    
    if selection == '4':
      print('Exiting Phonebook')
      break

    elif selection == '1':
      find_name = input('Find the phone number of :')
      if find_name in phonebook:
        print(phonebook[find_name], '\n')     
      else:
        print(f'Couldn\'t find phone number of {find_name}\n')

    elif selection == '2':
      add_name = input('Insert name of the person: ')
      phone = input('Insert phone number of the person: ')
      if phone.isdigit():
        phonebook[add_name] = phone
        print(f'Phone number of {add_name} is inserted into the phonebook\n')
      else:
        print('Invalid input format, cancelling operation ...\n')

    elif selection == '3':
      delete_name = input('Whom to delete from phonebook: ')
      if delete_name in phonebook:
        del phonebook[delete_name]
        print(f'{delete_name} is deleted from the phonebook.\n')
      else: 
         print(f'{delete_name} doesn\'t exist!\n')

    else:
      print('Invalid operation selection, try again!\n')
      continue

phonebook()





'''
Problem Statement
Write a program that creates a phonebook, adds requested contacts to the phonebook, finds them, and removes them.

There should be 4 options available to the user and from the options, users should be able to add, find, delete contacts, or terminate the program as shown below.

Phonebook has users and their corresponding phone numbers.

At the beginning of the program the phonebook will be empty and user can choose to add new contacts to the phonebook.

Program should ask user for the input, after giving information text shown as below.

Welcome to the phonebook application
1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) :
Application should be case sensitive and run until the user types 4.

Example for user inputs and respective outputs

Welcome to the phonebook application
1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 2
Insert name of the person : John
Insert phone number of the person: ten
Invalid input format, cancelling operation ...

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 2
Insert name of the person : Alex
Insert phone number of the person: 1234
Phone number of Alex is inserted into the phonebook

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 1
Find the phone number of : Alex
1234

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 3
Whom to delete from phonebook : Alex
Alex is deleted from the phonebook

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 1
Find the phone number of : Alex
Couldn't find phone number of Alex

1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : 4
Exiting Phonebook
© 2022 GitHub, Inc.
Terms


'''