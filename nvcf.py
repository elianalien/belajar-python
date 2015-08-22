def printargsaddr(*args):
	arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12 = args
	print "arg inp 1: %r, arg inp 2: %r" % (arg1,arg2)
	print "arg inp 1: %r, arg inp 2: %r" % (arg3,arg4)
	print "arg inp 1: %r, arg inp 2: %r" % (arg5,arg6)
	print "arg inp 1: %r, arg inp 2: %r" % (arg7,arg8)
	print "arg inp 1: %r, arg inp 2: %r" % (arg9,arg10)
	print "arg inp 1: %r, arg inp 2: %r" % (arg11,arg12)
	print args
	print args[1], args[4]

def printargtwo(arg1,arg2):
	print "arg inp 1: %r, arg inp 2: %r" % (arg1,arg2)

def printone(arg1):
	print "arg1: %r" % arg1

printargsaddr("test1", "test2","ahahah", "kecoak","kelelawar", "smut","drak", "ula","ini", "itu","deh", "ah",)
printargtwo("elian","daiva")
printone("el")