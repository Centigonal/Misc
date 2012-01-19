import random

class markov(object):

	def __init__(self):
		self.markovdict = {}
	
	def add(self,words):
		words = words.replace("(","")
		words = words.replace(")","")
		words = words.replace("."," .")
		words = words.replace(","," ,")
		words = words.replace("?"," ?")
		words = words.replace("!"," !")
		words = words.replace(":","")
		words = words.replace(";","")
		words = words.replace('"',"")
	
		sentence = words.split()
		for wordnum in xrange(len(sentence)-1):
			if sentence[wordnum] in self.markovdict:
				self.markovdict[sentence[wordnum]].append(sentence[wordnum+1])
			else:
				self.markovdict[sentence[wordnum]] = [sentence[wordnum+1]]
	
	
	def speak(self,length):
		output = ''
		word = random.choice(self.markovdict.keys())
		for n in range(length):
			if word in '.,!?':
				output = output.rstrip() + word + ' '
			else:
				output += word + ' '
			word = random.choice(self.markovdict[word])
		return output.strip()
	
	
	def sentence(self):
		output = ''
		word = random.choice(self.markovdict.keys())
		while word != "END OF SENTENCE":
			if word in '.,!?':
				output = output.rstrip() + word + ' '
				if word in '.!?':
					return output.strip()
			else:
				output += word + ' '
			word = random.choice(self.markovdict[word])
		return output.strip()
	
	
	def paragraph(self,length):
		while len(update.split()) <= length:
			update += self.sentence() + ' '	