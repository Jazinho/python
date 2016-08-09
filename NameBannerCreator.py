import time

name = input("Gimme your name: ")
length = len(name)
first_line = ''
for _ in range(length+4):
    first_line=first_line+'*'
print()
print(first_line)
print('* '+name+' *')
print(first_line)
time.sleep(3)
