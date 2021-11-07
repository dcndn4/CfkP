# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 08:19:17 2021

@author: CS_Knit_tinK_SC
"""

# review simplicities from 'Coding for Kids - Python' book

print("Hi Python!")

food = "cake"

#%%

food = "beets"

hobby = "knitting"

print(f"I like {food} and {hobby}")

#%%

a = 29

b = 58

c = a*b

d = a**b

e = a % b

f = a == b

g = a == 'b'

h = a != ejjj

#%%

print("basket" + "ball")

#%%

first_name = "meryl"

last_name = "streep"

print(first_name + " " + last_name)

#%%

print(3 + "cookies")

#%%

print(5*"balloons")

#%%

citrus_fruits = ['Orange', 'Lemon', 'Grapefruit', 'Pomelo', 'Lime']

print(citrus_fruits[2])

print(f'my two favorite fruits are {citrus_fruits[2]} and {citrus_fruits[0]}')

#%%

ages = 5, 10, 25, 43, 101

print(f'my two favorite ages are {ages[0]} and {ages[4]}')

#%%

print(f' today I ate {citrus_fruits[0:2]}')

#%%

fav_fruits = citrus_fruits[0:2]

print(f' today I ate {fav_fruits}')

#%%

ages = (5, 10, 25, 43, 150)

times = [5, 10, 25, 43, 150]

ages = []

times += [40, 2000]

ages += [7, 21, 14, 28, 35]

citrus_fruits += ['banana', 'cucumber']

#%%

print('cucumber' in citrus_fruits)

print(21 in ages)

print(22 in ages)

#%%

print(40 not in ages)

print('chocolate' not in citrus_fruits)

#%%

ages.remove(21)

#%%

del ages[2]

#%%

for fruit in citrus_fruits:
    print(f' we are eating {fruit}')
    
#%%

citrus_fruits[6]='Cucumber'

#%%

citrus_fruits[5]='Banana'

#%%

citrus_fruits[4:4]=['Cherries']

for fruit in citrus_fruits:
    print(f' we are eating {fruit}')
    
#%%

for raisin in citrus_fruits:
    print(f' we are eating {raisin}')
    
#%%

numbers = [1, 2, 3, 4, 5]

#%%

# this adds 2 to each element in the list, prints that sum (but doesn't change list contents)

for unicorn in numbers:
    unicorn += 2
    print(unicorn)
    
#%%

# this prints each element in the list, adds 2 to that number 
# in the list (changing the list contents), and prints sum (new list value)



for unicorn in numbers:
    print(unicorn)
    numbers[unicorn-1]+=2
    print(numbers[unicorn-1])
    
# I tried something like this multiple times in homework etc.. but always was forgetting to 
# make the indice of the list be one list than the iteration number. Finally cleared that stumbling block away!

#%%