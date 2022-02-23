import random

def generate_password():
  name = input('Please enter your full name: ').lower().replace(' ', '')
  if name.isalpha():
    s = "".join(random.sample(name, k=3))
    n = "".join([str(random.randint(0, 9)) for i in range(4)])
    return s + n
  else:
    return 'invalid input, try again!'

generate_password()



'''
Coding Challenge - 015: Generate Password
The purpose of this coding challenge is to write a program that creates a random password from a given full name.

Learning Outcomes
At the end of this coding challenge, students will be able to;

Analyze a problem, identify, and apply programming knowledge for an appropriate solution.

Implement conditional statements effectively to solve a problem.

Implement loops to solve a problem.

Execute operations on strings.

Make use of random numbers to solve a problem.

Demonstrate their knowledge of algorithmic design principles by solving the problem effectively.

Problem Statement
Write a Python program that prompts the user to enter his/her full name (without any spaces) and then creates a secret password consisting of three letters (in lowercase) randomly picked up from his/her full name, and a random four-digit number. For example, if the user enters "JackClarusway", a secret password can probably be one of "jcs1578" or "yka8832" or "awu1250".

Expected Output:
Please enter your full name: StephenClarkson
rto8807

Please enter your full name: BillJames
ils6032

Please enter your full name: MarkJackson
jkr7034

Please enter your full name: CarlSmith
iih7800

'''