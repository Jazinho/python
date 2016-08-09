
import random

print('*** BINGO BOARD ***')

numbers = []
new=0
random.seed()
for _ in range(10):
    new = random.randint(1,101)
    while(new in numbers):
        new = random.randint(1,101)
    numbers += [new]
numbers.sort()
cur = 0
for i in range(1,101):
    if i == numbers[cur] and cur<10:
        if i<10:
            print(' '+str(i)+' ', end='')
        else:
            if i % 10 == 1:
                print('\n\n'+str(i)+' ', end='')
            else:
                print(str(i)+' ', end='')
        if cur<9:
            cur=cur+1
    else:
        if i % 10 == 1:
            print('\n\n__ ', end='')
        else:
            print('__ ', end='')

print('\n\nYou\'re welcome! :)\n')
    
