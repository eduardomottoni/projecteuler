# THIS CODE IS CHANGED TO NOT GIVE THE ANSWER TO EULER PROJECT QUESTIONS
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 08:51:34 2023

@author: eotoni
"""

from sympy import isprime, primerange
import json
import time

# Record the start time
start_time = time.time()

# Your code goes here
# ...


def is_concatenation_prime(num1, num2):
    concatenated_num = int(str(num1) + str(num2))
    return isprime(concatenated_num)

def verify_if_matches(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            num1, num2 = numbers[i], numbers[j]
            if not (is_concatenation_prime(num1, num2) and is_concatenation_prime(num2, num1)):
                return False
    return True

valid_set = [0] * 3
test_set = [0] * 3
prime_set = list(primerange(1, 200)) 
prime_set.remove(5)
len_prime_set = len(prime_set)
prime_set_last_value = prime_set[len_prime_set-1]
smalest_iterator = 2
second_iterator = minute_iterator = hour_iterator = day_iterator = week_iterator = smalest_iterator
iterator = smalest_iterator
test_set = prime_set[1:4]
restart = False
while verify_if_matches(test_set) == False:
    
    if restart:
        if test_set[1] >= prime_set[len_prime_set-2]:
            week_iterator += 1
            day_iterator = week_iterator
            test_set[0] = prime_set[week_iterator]
        if day_iterator > 164:
            print()
        day_iterator += 1
        test_set[1] = prime_set[day_iterator]
        second_iterator = minute_iterator = hour_iterator = smalest_iterator
        restart = False
    while (verify_if_matches(test_set[:2]) == False ^ restart):
        if test_set[1] == prime_set[len_prime_set-1]:
            week_iterator += 1
            day_iterator = week_iterator
            if test_set[0] != prime_set[len_prime_set-1]:
                test_set[0] = prime_set[week_iterator]
                test_set[1] = prime_set[week_iterator]
                restart = True
                
            else:
                raise SystemExit(0)
        day_iterator += 1
        test_set[1] = prime_set[day_iterator]
        if test_set[1] == prime_set[len_prime_set-1]:
            week_iterator += 1
            day_iterator = week_iterator
            if test_set[0] != prime_set[len_prime_set-1]:
                test_set[0] = prime_set[week_iterator]
                test_set[1] = prime_set[week_iterator]
                restart = True
                
            else:
                raise SystemExit(0)
            
    hour_iterator = day_iterator
    test_set[2] = prime_set[hour_iterator]
    while verify_if_matches(test_set[:3]) == False ^ restart:
        hour_iterator += 1
        test_set[2] = prime_set[hour_iterator]
        if test_set[2] == prime_set[len_prime_set-1]:
            # hour_iterator = smalest_iterator
            # day_iterator += 1
            # test_set[2] = test_set[smalest_iterator]
            if test_set[1] != prime_set[len_prime_set-1]:
                restart = True
                break
            else:
                restart = True
    
    minute_iterator = hour_iterator
    test_set[3] = prime_set[minute_iterator]
    while verify_if_matches(test_set[:4]) == False ^ restart:
        minute_iterator += 1
        test_set[3] = prime_set[minute_iterator]
        if test_set[3] == prime_set[len_prime_set-1]:
            # minute_iterator = smalest_iterator
            # hour_iterator += 1
            # test_set[3] = test_set[smalest_iterator]
            if test_set[2] != prime_set[len_prime_set-1]:
                test_set[2] = prime_set[smalest_iterator]
                restart = True
                break
            else:
                restart = True
    
    second_iterator = minute_iterator
    test_set[4] = prime_set[second_iterator]
    while verify_if_matches(test_set) == False ^ restart:
        second_iterator += 1
        test_set[4] = prime_set[second_iterator]
        if test_set[4] == prime_set[len_prime_set-1]:
            # second_iterator = smalest_iterator
            # minute_iterator += 1
            # test_set[4] = test_set[smalest_iterator]
            if test_set[3] != prime_set[len_prime_set-1]:
                test_set[3] = prime_set[smalest_iterator]
                restart = True
                break
            else:
                restart = True

    
# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(f"The code took {elapsed_time:.4f} seconds to run.")
valid_set = test_set
sum_valid_set = sum(valid_set)