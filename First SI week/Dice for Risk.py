# Write a python script, that generates 5 numbers between 1 and 6 and prints them in a meaningful # way for the game. Sort the results for the attacker and for the defender, so make roll pairs, 
# like in this image:

# In a dice pair, there are the following rules:

# When the attacker's die value is larger: Attacker wins (1 defender unit dies)
# When the 2 dice value is tie: Defender wins (1 attacker unit dies)
# When the defender's die value is larger: Defender wins (1 attacker unit dies)

import random

attack = int(input('How many units attack(max 3): '))
while not((attack == 1) or (attack == 2) or (attack == 3)):
    attack = int(input('How many units attack(max 3): '))
    
defend = int(input('How many units defend(max 2): '))
while not((defend == 1) or (defend == 2)):
    defend = int(input('How many units defend(max 2): '))

i = 0
j = 0
list1 = []
list2 = []
while i < 3:
    x = random.randint(1,6)
    list1.append(x)
    i += 1
list1 = sorted(list1)
list1.reverse()

while j < 2:
    x = random.randint(1,6)
    list2.append(x)
    j += 1
list2 = sorted(list2)
list2.reverse()

if attack == 3 and defend == 2:
    print('Dice:')
    print('   Attacker: ' + str(list1[0]) + '-' + str(list1[1]) + '-' + str(list1[2]))
    print('   Defender: ' + str(list2[0]) + '-' + str(list2[1]))
    print('Outcome: ')

    if list1[0] <= list2[0] and list1[1] <= list2[1]:
        print('     Attacker: Lost 2 units')
        print('     Defender: Lost 0 units')
    else:
        if list1[0] <= list2[0]:
            print('     Attacker: Lost 1 unit')
        if list1[1] <= list2[0]:
            print('     Attacker: Lost 1 unit')

    if list1[0] > list2[0] and list1[1] > list2[0]:
        print('     Attacker: Lost 0 units')
        print('     Defender: Lost 2 units')
    else:
        if list1[0] > list2[0]:
            print('     Defender: Lost 1 unit')
        if list1[1] > list2[1]:
            print('     Defender: Lost 1 unit')

if attack == 3 and defend == 1:
    print('Dice:')
    print('   Attacker: ' + str(list1[0]) + '-' + str(list1[1]) + '-' + str(list1[2]))
    print('   Defender: ' + str(list2[0]))
    print('Outcome: ')

    if list1[0] <= list2[0]:
        print('     Attacker: Lost 1 unit')
        print('     Defender: Lost 0 unit')
    if list1[0] > list2[0]:
        print('     Attacker: Lost 0 unit')
        print('     Defender: Lost 1 unit')

if attack == 2 and defend == 2:
    print('Dice:')
    print('   Attacker: ' + str(list1[0]) + '-' + str(list1[1]))
    print('   Defender: ' + str(list2[0]) + '-' + str(list2[1]))
    print('Outcome: ')

    if list1[0] <= list2[0] and list1[1] <= list2[1]:
        print('     Attacker: Lost 2 units')
        print('     Defender: Lost 0 units')
    else:
        if list1[0] <= list2[0]:
            print('     Attacker: Lost 1 unit')
        if list1[1] <= list2[1]:
            print('     Attacker: Lost 1 unit')

    if list1[0] > list2[0] and list1[1] > list2[1]:
        print('     Attacker: Lost 0 units')
        print('     Defender: Lost 2 units')
    else:
        if list1[0] > list2[0]:
            print('     Defender: Lost 1 unit')
        if list1[1] > list2[1]:
            print('     Defender: Lost 1 unit')

if attack == 2 and defend == 1:
    print('Dice:')
    print('   Attacker: ' + str(list1[0]) + '-' + str(list1[1]))
    print('   Defender: ' + str(list2[0]))
    print('Outcome: ')

    if list1[0] <= list2[0] :
        print('     Attacker: Lost 1 unit')
        print('     Defender: Lost 0 units')

    if list1[0] > list2[0]:
        print('     Attacker: Lost 0 units')
        print('     Defender: Lost 1 unit')

if attack == 1 and defend == 1:
    print('Dice:')
    print('   Attacker: ' + str(list1[0]))
    print('   Defender: ' + str(list2[0]))
    print('Outcome: ')

    if list1[0] <= list2[0] :
        print('     Attacker: Lost 1 unit')
        print('     Defender: Lost 0 units')

    if list1[0] > list2[0]:
        print('     Attacker: Lost 0 units')
        print('     Defender: Lost 1 unit')
    
