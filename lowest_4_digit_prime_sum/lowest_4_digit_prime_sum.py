# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 23:29:26 2023

@author: eotoni
"""

#the code finds the right answer as much fast as closer to the bigest number of the series

from sympy import isprime, primerange
import json

def is_concatenation_prime(num1, num2):
    concatenated_num = int(str(num1) + str(num2))
    return isprime(concatenated_num)

def verify_if_matches(valid_set, number):
    numbers = valid_set.copy()  # Make a copy to avoid modifying the original set
    numbers.append(number)
    if len(numbers) < 2:
        return False
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
        
            num1, num2 = numbers[i], numbers[j]
            if not (is_concatenation_prime(num1, num2) and is_concatenation_prime(num2, num1)):
                return False
    valid_set.append(num2)
    return True

set_primes = [3]
iterator_start = 1
iterator = 1
find_next_prime = False
list_of_sums = {}
temp_set = []
dark_list = []
limit_range = 50000
prime_set = list(primerange(1, limit_range))  # Convert the generator to a list

while (len(set_primes) < 5):
    len_stop = (len(prime_set) - iterator_start)
    if iterator > len_stop:     
        iterator_start += 1
        iterator = iterator_start
        min_value = min(prime_set)
        if len(set_primes) != 0:
            set_primes.pop(0)
# =============================================================================
#         elif (any(len(value) <= 3 for value in list_of_sums.values())):
#             limit_range += 1000
#             prime_set = list(primerange(1, limit_range))
#             iterator = iterator_start = 1
#             set_primes = [3]
#             print("limit range adjusted")
#             continue
# =============================================================================
        else:
            break
    temp_set = set_primes.copy()
    temp_set.append(prime_set[iterator])
    temp_set = set(temp_set)
    if len(temp_set) == 1 and next(iter(temp_set)) == prime_set[iterator]:
        iterator += 1
        continue
    print(f"iteration number {iterator} and {len_stop-iterator} left, {len_stop} cicles left")
    if temp_set in dark_list:
        print(f"set_primes {temp_set} is in dark_dict.")
        iterator += 1
    elif verify_if_matches(set_primes, prime_set[iterator]):
        list_of_sums[(sum(set_primes))] = set_primes.copy()
        print(f"Found the lowest sum: {sum(set_primes)}")
    else:
        dark_list.append(set(temp_set))
    iterator += 1
file_path = 'result.txt'

# Write the dictionary to the file in JSON format
with open(file_path, 'w') as file:
    json.dump(list_of_sums, file)