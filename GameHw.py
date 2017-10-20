#!/usr/bin/python

from sys import exit

def start():
	print "You are being chased by a monster!!! There is a open field straight ahead a house to the left and a forest to your right."
	print "Where do you go [field] [house] [forest]"

	next = raw_input("> ")
	
	if next == "field":
		field()
	elif next == "house":
		house()
	elif next == "forest":
		forest()
	else:
		dead("The monster caught you and you died")



def start2():
	print"You climb out of the bunker and you see the house and forest again where do you go"

	next = raw_input("> ")

	if next == "house":
		house()
	elif next == "forest":
		forest()
	else:
		dead("The monster turned around and killed you")


def dead(why):
	print why
	exit(0)


def field():
	print "You run into the feild and fall into a underground bunker"
	print "What do you do know run or hide?"
	next = raw_input("> ")
	
	if next == "run":
		dead("You died because the monster caught up to you")
	elif next == "hide":
		print "You hide and wait and hear the monster run by you are know safe"
		raw_input("Press any key to continue")
		start2()

def forest():
	dead("There were more monsters in the woods and you died")


def house():
	print "You encounter and old man"
	print "He says it is dangerous to go alone and tells you to pick one of these"
	print "There are three weapons [1] [2] [3]"
	
	weapons = ["club", "sword", "gun"]

	pick = int(raw_input("> "))

	print "You choose weapon number %d and you got %s" % (pick, weapons[pick-1])
	print "You know have a %s" % (weapons[pick-1])
	print "What do you do next hide or fight with the man"

	next = raw_input("> ")

	if next == "hide":
		print "You guys surrive the night!!"
		print "Press any key to continue"
		dayafter()
	elif next == "fight":
		print" You both go outside to find the monster and you do but the man dies and then you kill the monster"

def dayafter():
	print "The next morning the man asks you if you need a ride home"
	print "You can either [walk] or [drive]"
	next = raw_input("> ")

	if next == "walk":
		print "You start walking and get lost and somehow enter the forest and get killed by the monesters"
		dead()
	elif next == "drive":
		print "You get a ride from the kind man and get home safely and know have a cool story to tell"

start()
