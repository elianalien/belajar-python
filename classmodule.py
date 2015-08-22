class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def singmeasong(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["happy bday to you",
					"i dont want to get sued",
					"so ill stop right there"])

bullsonparade = Song(["they rally around the family", 
						"with pocket full of shells"])

happy_bday.singmeasong()
bullsonparade.singmeasong()
