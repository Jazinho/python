import re

print('*** EMAIL VALIDATOR ***')
print('Type in an email you want to check and I will tell you if it is valid.')
while(True):
    email = input('Your email: ')
    if re.match('\S+@[a-z]+\.[a-z]+',email):
        print('Your e-mail is correct!')
    else:
        print('Your e-mail is not correct!')
    end = input('If you want to exit, press \'x\' then \'Enter\'\nIf you want to check another e-mail, type any other key and then \'Enter\'\n')
    if end == 'x':
        break
