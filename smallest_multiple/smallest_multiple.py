# THIS CODE IS CHANGED TO NOT GIVE THE ANSWER TO EULER PROJECT QUESTIONS
# # -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:48:29 2023

@author: eotoni
"""

# =============================================================================
# Smallest Multiple
# <p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
# <p>What is the smallest positive number that is <strong class="tooltip">evenly divisible<span class="tooltiptext">divisible with no remainder</span></strong> by all of the numbers from $1$ to $20$?</p>
# 
# =============================================================================

find_num = False
contador = 1
while True:
    for i in range(1, 5):
        if contador % i != 0:
            break
    else:
        # Este bloco é executado se o loop for concluído sem interrupção
        print(contador)
        break

    contador += 1
    
