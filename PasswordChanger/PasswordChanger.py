import re
import os.path
import hashlib
import getpass

pattern = re.compile('[A-Z][a-z]')

print('*****************************************')
print('*********  DATABASE OF USERS  ***********')
print('*****************************************')
print('********  AUTHOR: JAN PAŁUCKI  **********')
print('*****************************************')

while(True):
    decision = input('If you want to add new user, type \'n\'. \nIf you want to change your password, type \'c\'.\nIf you want to exit, type \'x\'\n>>>>')
    if decision == 'x':
        break
    if not decision=='x' and not decision=='n' and not decision=='c':
        print('I don\'t know what to do...')
        continue
    if decision == 'n':
        print('Password must contains uppercase letter, lowercase letter and has at least 8 characters.')

    if os.path.isfile('PasswordBase.txt'):
        f = open('PasswordBase.txt','r+')
        lines = f.readlines()
        f.close()
    else:
        lines=[]
    f = open('PasswordBase.txt','w+')

    found_user = False
    changed = False
    not_valid = False
    bad_retyping = False
    validate_user = False
    
    login = input('Login: ')
    old_pwd = getpass.getpass('Password: ')

    for line in lines:
        if login+','+hashlib.md5(old_pwd.encode('utf-8')).hexdigest()+'\n' == line:
            validate_user = True
            if decision == 'c':
                new_pwd = getpass.getpass('New password: ')
                new_pwd2 = getpass.getpass('Retype new password: ')
                if new_pwd == new_pwd2:
                    if pattern.findall(new_pwd) and len(new_pwd)>7:
                        f.write(login+','+hashlib.md5(new_pwd.encode('utf-8')).hexdigest()+'\n')
                        changed = True
                        continue
                    else:
                        not_valid = True
                else:
                    bad_retyping = True
        if login+',' in line:
            found_user = True
        f.write(line)

    if validate_user and decision=='c':
        if changed:
            print('Correctly changed password!')
        elif bad_retyping:
            print('Retyped password is different to the first one!')
        else:
            print('Your password must contain uppercase letter, lowercase letter and has at least 8 characters!')
    elif found_user and decision=='n':
        print('User already exists!')
    elif found_user and not validate_user and decision=='c':
        print('Wrong password! Access denied!')
    elif not found_user and decision=='c':
        print('Given user doesn\'t exists!')
    elif not found_user and decision=='n':
        if pattern.findall(old_pwd) and len(old_pwd)>7:
            f.write(str(login)+','+hashlib.md5(old_pwd.encode('utf-8')).hexdigest()+'\n')
            print('Succesfully added new user!')
        else:
            print('Adding new user failed. Not valid password!')
    else:
        print('Unhandled condition. Report it to program author :)')
        
    f.close()

    
