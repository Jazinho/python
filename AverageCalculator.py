

print('*** AVERAGE CALCULATOR ***\n')
print('Type as many numbers as You wish, separating then with a comma.')
print('I will do the rest and calculate the average of them for You :)\n')
while(True):
    user_input = input('Type your numbers: ')
    numbers = user_input.split(',')
    sum = 0
    for i in numbers:
        sum = sum+int(i)

    result = sum/len(numbers)
    print('The average of given numbers is '+str(result))
    end = input('If you like to exit, press \'x\', then \'Enter\'.\nIf you like to count another average, press any key, then \'Enter\'.\n')
    if end == 'x':
        print('Visit us again! Bye :)')
        break
