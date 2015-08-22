from sys import argv

script, filename = argv

print "erase %r" % filename
print "press return button"

raw_input("?")

print "opening file"
target = open(filename, 'w')

print "truncate the file"
target.truncate()

print "questions"

line1 = raw_input("1st line: ")
line2 = raw_input("2nd line: ")
line3 = raw_input("3rd line: ")

print "writing to file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "finished"
target.close()