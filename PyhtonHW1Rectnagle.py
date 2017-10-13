#!/usr/bin/python

print "Enter the length of the rectangle"
length = int(raw_input())

print "Enter the width of the retangle"
width = int(raw_input())

area = length*width

print "If you want perimeter type A if you want area type B"
input = raw_input()

perimeter = (length)+(width)*2

if input == "A":
	print (perimeter)
elif input == "B":
	print (area)

