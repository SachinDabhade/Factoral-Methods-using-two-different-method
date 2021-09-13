# *********************** Factorial Number by two different methods *************************8

# Importing Library
from datetime import datetime

# Function to find factorial using for loop method
def factorial_1(number):
    """ This will find the factorial number of the input"""
    factor = 1
    initial_time = datetime.now()
    for i in range(1, number + 1):
        factor = factor * i
    print('Factorial: ',factor)
    final_time = datetime.now()
    difference_1 = final_time - initial_time
    print('\n1st Method requires ',difference_1, ' time to find factorial')
    return difference_1, factor

# Second method of finding factorial from recursion method
def factorial_2(number):
    """ This will find the factorial number of the input"""
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial_2(number=number - 1)

if __name__ == '__main__':
    
    number = int(input("Enter any positive number: "))
    difference_1, factor = factorial_1(number)
    initial_time = datetime.now()
    factorial_2(number)
    final_time = datetime.now()
    difference_2 = final_time - initial_time
    print('2nd Method requires ',difference_2, ' time to find factorial')

    Maximum = max([difference_1, difference_2])
    Minimum = min([difference_1, difference_2])
    print("Difference between timing: ",Maximum-Minimum)
