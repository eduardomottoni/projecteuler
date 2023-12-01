# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:14:52 2023

@author: eotoni
"""

def sum_square(number):
    square = 1
    sum_of_squares = 1
    sum_of_squares_old_method = 0
    for i in range(1, number):
        square = (square + i+i+1)
        sum_of_squares+= square
    return sum_of_squares
    for i in range(1, number+1):
        print(sum_of_squares_old_method)
        sum_of_squares_old_method += i**2
number = 100
squared_sum = sum_square(number)
sum_squared = sum(i for i in range(1,number+1))**2
result = sum_squared - squared_sum
print (result)