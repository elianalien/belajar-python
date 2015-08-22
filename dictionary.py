states = {
	'oregon': 'or',
	'florida': 'fl',
	'california': 'ca',
	'new york': 'ny',
	'michigan': 'mi',
}

cities = {
	'ca': 'san francisco',
	'mi': 'detroit',
	'fl': 'jacksonville'
}
	

cities['ny'] = 'new york'
cities['or'] = 'portland'

print '-' * 10
print "ny states has : ", cities['ny']
print "or states has : ", cities['or']

print '-' * 10
print "michigan abbrev : ", states['michigan']
print "florida abbrev : ", states['florida']

print '-' * 10
print "michigan has: ", cities[states['michigan']]
print "florida has: ", cities[states['florida']]

print '-' * 10
print "cities items are ", cities.items()
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

print '-' * 10
print "states items are ", states.items()
for states, abbrev in states.items():
	print "%s is abbreviated %s" % (states, abbrev)
