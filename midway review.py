# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 08:19:17 2021

@author: CS_Knit_tinK_SC
"""

# review simplicities from 'Coding for Kids - Python' book

print("Hi Python!")

food = "cake"

#%%

print("Hello Again, World!")
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

h = a != e

#%%

print("basket" + "ball")

#%%

first_name = "meryl"

last_name = "streep"

print(first_name + " " + last_name)

#%%

print(3*"cookies")

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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

i = 0

while(i < len(numbers)):
    if (numbers[i] + 2) < 20:
        print (f'the numbers under 20 are {numbers[i] + 2}')
    else:
        print(f' the other numbers <before adding 2> are {numbers[i]}')           
    i += 1    
#%%

print("Hi! My name is Juie. My favorite dessert is jelly beans")

#%%

i = 0

#%%

# First try, didn't work, not sure why..
# error message is 'list indices must be integers or slices, not str
# sigh

# people = ['Mario', 'Peach', 'Luigi', 'Daisy', 'Toad', 'Yoshi']

# desserts = ['Star Pudding', 'Peach Pie', 'Popsicles', 'Honey Cake', 'Cookies', 'Jelly Beans']

# for i in people:
#    print (f' Hi! My name is {people[i]} and my fav dessert is {desserts[i]}')
    
    

people = ['Mario', 'Peach', 'Luigi', 'Daisy', 'Toad', 'Yoshi']

desserts = ['Star Pudding', 'Peach Pie', 'Popsicles', 'Honey Cake', 'Cookies', 'Jelly Beans']

for i in range(len(people)):
    name = people[i]
    food = desserts[i]
    print (f' Hi! My name is {name} and my fav dessert is {food}')
    
#%%

nachos_friends = ['athletic', 'not athletic', 'older', 'athletic', 'younger', 'athletic', 'not athletic', 'older', 'athletic', 'older', 'athletic']

hula_hoops_by_swings = 0
hula_hoops_by_basketball_court = 0

for i in range(len(nachos_friends)):
    if nachos_friends[i] == 'athletic':
        hula_hoops_by_swings += 1
    if nachos_friends[i] == 'younger':
        hula_hoops_by_swings += 1
    if nachos_friends[i] == 'not athletic':
        hula_hoops_by_basketball_court += 1
    if nachos_friends[i] == 'older':
        hula_hoops_by_basketball_court += 1

#%%


has_zero_legs = 0
has_two_legs = 0
has_four_legs = 0
#%%

no_id_animals = [4, 0, 2, 4, 2, 0, 2, 4, 4, 2, 0, 2, 4]


#%%
for i in range(len(no_id_animals)):
    if no_id_animals[i] == 0:
        has_zero_legs += 1
    if no_id_animals[i] == 2:
        has_two_legs += 1
    if no_id_animals[i] == 4:
        has_four_legs += 1
        
# This works:      
print(f'Animals with no legs: {has_zero_legs}')
print(f'Animals with two legs: {has_two_legs}')
print(f'Animals with four legs: {has_four_legs}')

#%%

# but this is even better!
animal_summary = f'''       
Animals with no legs: {has_zero_legs}
Animals with two legs: {has_two_legs}
Animals with four legs: {has_four_legs}
'''

print(animal_summary)


#%%

birds_nest_ground = 0
birds_nest_tree = 0
birds_nest_other = 0
#%%

# nest ground = 1, nest tree = 10, nest other = 5

birds = [0, 10, 5, 5, 10, 0, 0, 10, 0, 10]

#%%

for i in range(len(birds)):
    if birds[i] == 0:
        birds_nest_ground += 1
    if birds[i] == 10:
        birds_nest_tree += 1
    if birds[i] == 5:
        birds_nest_other += 1
        
#%%

# but this is even better!
bird_summary = f'''       
survey of birds who build their nests on the ground: {birds_nest_ground}
survey of birds who build their nests in trees: {birds_nest_tree}
survey of birds who build their nests somewhere else: {birds_nest_other}
'''

print(bird_summary)