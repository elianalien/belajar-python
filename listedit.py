ten_things = "apple orange crows telephone light sugar"

print "wait there's not 10 ten things in the list, lets fix that"

stuff = ten_things.split(' ')
more_stuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "adding: ", next_one
	stuff.append(next_one)
	print "there's %d item now" % len(stuff)

print "there we go: ", stuff
print "let's do some things with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop() + " now list : ", len(stuff)
print ' '.join(stuff)
print '#'.join(stuff[0:5])