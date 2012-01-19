import random

class markov(object):

	def __init__(self):
		self.markovdict = {}
	
	def add(self, words, order=1):
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
		orderedsentence = []

		for wordnum in xrange(0,len(sentence)-order*2):
			appendword = ''
			for i in xrange(order, order*2):
				appendword += sentence[wordnum+i] + ' '
			orderedsentence.append(appendword.strip())
		self.markovdict[appendword.strip()] = ['END OF SENTENCE']
		print appendword.strip(), self.markovdict[appendword.strip()]
		for wordnum in xrange(len(orderedsentence)-order):
			if orderedsentence[wordnum] in self.markovdict:
				self.markovdict[orderedsentence[wordnum]].append(orderedsentence[wordnum+1])
			else:
				self.markovdict[orderedsentence[wordnum]] = [orderedsentence[wordnum+1]]

	def clear(self):
			self.markovdict = {}
	
	
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
		update = ''
		while len(update.split()) <= length:
			update += self.sentence() + ' '
		return update.strip()
