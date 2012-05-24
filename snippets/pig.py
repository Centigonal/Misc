def converto(str):
	str = str.lower()
	translatedwordslist = []
	for word in str.split():
		if word.startswith(("sh","th")):
			word = word[2:] + word[:2] + "ay"
		elif not word.startswith(("a","e","i","o","u")):
			word = word[1:] + word[0] + "ay"
			print word,3
		else:
			word += "ay"
		translatedwordslist.append(word)
	print ' '.join(translatedwordslist)
converto("importing images into the army painter")