from sys import exit

def goldroom():
	print "this room is full of gold. how much do you take?"

	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("learn to write a fuckin number, man!")

	if how_much < 50:
		print "Nice, you're not greedy"
		exit(0)
	else:
		dead("you freakin greedy")

def bearroom():
	print "there is a bear here"
	print "the bear has a bunch of honey"
	print "the fat bear is in front of another door"
	print "how are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("the bear looks at you than slaps your face off")
		elif next == "taunt bear" and not bear_moved:
			print "the bear has moved from the door. You can go through it now"
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("the bear get pissed off and chews your legs off")
		elif next == "open door" and bear_moved:
			goldroom()
		else:
			print "i got no idea what that means"

def cthulhuroom():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "flee or head?"

	next = raw_input("> ")

	if "flee" in next:
		start()

	elif "head" in next:
		dead("well thats tasty!")
	else: 
		cthulhuroom()

def dead(why):
	print why, "good Joob!"
	exit(0)

def start():
	print "you're in the dark room"
	print "there is a door to your right and left"
	print "which one do you take?"

	next = raw_input("> ")

	if next == "left":
		bearroom()
	elif next == "right":
		cthulhuroom()
	else: 
		dead("you stumble around the room until you starve")


start()