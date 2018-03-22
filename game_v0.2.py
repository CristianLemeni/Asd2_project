import time
import sys
import object
import game_linked_list
#import binar

import random

class Node:
	def __init__(self,initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newnext):
		self.next = newnext
		
class UnorderedList:

	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()

		return count

	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

def game():
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print ("The Murderer's Shadow")
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	time.sleep(1)
	intro = """
		On a friday night you and some friends went out for a drink.
	You had a great time and after a few hours of drinking heavily
	your friends thought of a great game. 'What if one of us goes into
	old man Joe's house. I heard it's hunted.' You look around at the rest of your friends
	and they all seem pretty exited. 'Man, ghosts don't exist, how much did you drink?'
	An arguments breaks out and you decide it's time to call in for the night.
		'Hey, are you going already?' You nod. 'What scared of ghost?' laughter breaks out
	and you say you aren't 'So then you go in and see what you find'.
		Shaking your head you ask what do they want you to get for them.
	'I heard Joe had an old book full drawings that he did when he was a kid.'
		After leaving the bar you all head down a few dark streets until you're at the edge of
	town. A few houses lay here and there but at this hour all of them are quiet.
		You check your watch: it's 3:23 AM
	As you are starting to think that this is a bad idea your friends stop and point at a house
	'That's the one'
	The shadowy house stands upon a small hill. It's surroundings lie full with weeds and a 
	small wooden fence. Looking at the site you feel a chill and start to shake a bit. 
	'Come on, you're not afraid are you?'. You shake your head and press on.
		They all look at you as you approach the house and while being with the group
	provided some feeling of safety it's all gone now, replaced with a growing feeling of unease.
	It's just a stupid book, you think, I just have to find it and leave this creepy house.
		As you approach the house it seems even worse up close. As you pass the fence, you see
	that most of the windows have been boarded up except the ones on the upper floor.
		Time has sure taken it's toll on the house. The walls are dirty with a few small holes
	here an there. As you approach the front porch, you see that it's full of cracks. For almost a
	second you swear you saw a rat enter beneath the wooden boards.
			You cautiously step on the porch and it breaks the silence with a loud creak. You stand 
	still for a few seconds and listen. No insects or animals, no birds nothing. The silence is deafening.
		Suddenly a gust of wind slowly opens the front door. Like the boards on the porch, the door lets
	out a loud creak.
		With a deep breath you go inside to get the stupid book.
	"""
	print intro
	


class player():
	def __init__(self):
		self.inventory = []
	def print_inventory(self):
		for item in self.inventory:
			print(item,'\n')

	

def Instructiuni():
	print("Commands")
	print("'go [direction]'")
	print("'take [object]'")
	print("'search'")
	print("'use' [item] on [object]")
	print("----------")
	
def Status():
	print("You are in " + rooms[current_room]["name"])
	print("inventory : " + str(inventory))

def search():
		return rooms[current_room]["object"]

inventory = []
	
rooms = {
			1:{"name" : "the foyer",
				"east" : 2,
				"object" : "book"
				},
			2:{"name" : " the dining room",
				"west" : 1,
				"north" : 3,
				"east" : 8},
			3:{"name" : "the kitchen",
				"north" : 9,
				"west" : 4},
			4:{"name" : "the living room",
				"west" : 6,
				"south" : 5},
			5:{"name" : "study",
				"north" : 4},
			6:{"name" : "the master beedroom",
				"east" : 4,
				"south" : 7},
			7:{"name" : "the master bathroom",
				"north" : 6,
				"south" : 8},
			8:{"name" : "the west side porch",
				"north" : 7,
				"east" : 9},
			9:{"name" : "the front porch",
				"west" : 8,
				"north" : 1,
				"east" : 10},
			10:{"name" : "the east side porch",
				"west" : 2,
				"south" : 9},
			11:{"name" : "the hidden room",
				"south" : 3},
			12:{"name" : "the second hidden room",
				"east" : 4}
		}
		
current_room = 1
game()
Instructiuni()
"""
while True:
	Status()
			
	action = raw_input(">").lower().split()
	
	if action[0] == "go":
		if action[1] in rooms[current_room]:
			current_room = rooms[current_room][action[1]]
		else:
			print("You can't go there!")
			
	if action[0] == "take":
		if "object" in rooms[current_room] and action[1] in rooms[current_room]["object"]:
			inventory += [action[1]]
			print(action[1] + " taken")
			del rooms[current_room]["object"]
		else:
			print("You can't " + action[1])
			
	if action[0] == "search":
		if "object" in rooms[current_room]:
			print rooms[current_room]["object"]
		else:
			print("There is nothing of interest here")
			
"""	



print Status()

mylist = UnorderedList()

mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
mylist.add(6)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

