def most_frequent_num(numbers_list):
    return max(numbers_list, key=numbers_list.count)
    
most_frequent_num([1, 3, 7, 4, 3, 0, 3, 6, 3])

'''
Task : Find out the most frequent number and its frequency.

Write a program that;
Finds out the most frequent number in the given list.
Calculates its frequency.
Prints out the result such as :
Example
Given list	
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
Desired Output
the most frequent number is 3 and it was 4 times repeatedNote : You can/should use useful/necessary built-in functions and methods of the list operation.
'''