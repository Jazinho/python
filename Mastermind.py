import random
import time

random.seed()
sol=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
sol_flags=[False,False,False,False]
counter = 1
guessed_counter=0
flag=False

print('        ------------ MASTERMIND -------------     ')
print('   Guess the 4 numbers in as few tries as possible')

while(True):
    user_input = input('Try no.'+str(counter)+':')

    if not ' ' in user_input and len(user_input)==4:
        for i in range(4):
            for j in range(4):
                if sol_flags[i]==False and sol[i] == int(user_input[j]):
                    sol_flags[i] = True
                    user_input.replace(user_input[j],'')
                    guessed_counter=guessed_counter+1
                    break
                
#Checking if user guessed all numbers
        if(sol_flags[0]==True and sol_flags[1]==True and sol_flags[2]==True and sol_flags[3]==True):
            break

#Printing how many numbers was guessed correctly
        print("*" * guessed_counter)
        guessed_counter=0
        counter=counter+1
        sol_flags=[False,False,False,False]
    else:
        print('Invalid input! Try again.')
    
print('You won! It took you '+str(counter)+' tries.')
time.sleep(3)
