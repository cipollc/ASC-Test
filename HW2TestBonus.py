#!/usr/bin/pyhton

from sys import argv

script, name, age, birthmonth = argv

file = open("customer.txt", "w")

line1 = "Your name is %s" % name + "\n"
line2 = "You are %s years old" % age + "\n"
line3 = "Your birth month is %s" % birthmonth + "\n"

file.write(line1)
file.write(line2)
file.write(line3)

file.close()
file2 = open("customer.txt")
print file2.read()
