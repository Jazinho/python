print('*** COLOUR CONVERTER ***\n\n')

dict = {0:'0',
        1:'1',
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        7:'7',
        8:'8',
        9:'9',
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F'}
while True:
    dec = input('Type \'x\' to exit. \'c\' to convert colour: ')
    if dec == 'x':
        break
    if not dec == 'c':
        print('I don\'t know what to do...')
        continue
    while True:
        red = input('Enter red value (between 0 and 255): ')
        if int(red) >=0 and int(red) <=255:
            break
        else:
            print('Value of colour must be between 0 and 255!')
    while True:
        blue = input('Enter blue value (between 0 and 255): ')
        if int(blue)>=0 and int(blue) <=255:
            break
        else:
            print('Value of colour must be between 0 and 255!')
    while True:
        green = input('Enter green value (between 0 and 255): ')
        if int(green)>=0 and int(green) <=255:
            break
        else:
            print('Value of colour must be between 0 and 255!')
            
    result = '#'

    for i in [red,blue,green]:
        dig1 = int(i) % 16
        dig2 = (int(i) / 16) % 16
        result = result + dict[int(dig2)]
        result = result + dict[dig1]

    print('Hexadecimal representation of given colour: '+result)
