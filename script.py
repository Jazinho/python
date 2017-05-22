#!/usr/bin/python

import re
import matplotlib.pyplot as plt

f = open('sample4.txt', 'r')

x_list = []
y_list = []
z_list = []

for line in f:
    tab = re.split(';',line)
    x_list.append(eval(tab[0]))
    y_list.append(eval(tab[1]))
    z_list.append(eval(tab[2]))

plt.figure(1)

s1 = plt.subplot(311)
s1.set_title("X coordinate")
plt.plot(x_list)

s2= plt.subplot(312)
s2.set_title("Y coordinate")
plt.plot(y_list)

s3 = plt.subplot(313)
s3.set_title("Z coordinate")
plt.plot(z_list)

#plt.savefig('coords.png')
plt.show()
