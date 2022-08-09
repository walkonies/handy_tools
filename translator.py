import googletrans
import sys

class Translator:
	LANGUAGES = googletrans.LANGUAGES
	UNKOWN = '??'

	def __init__(self):
		self.translator = googletrans.Translator()
		self.in_lang = self.UNKOWN
		self.out_lang = self.UNKOWN
	def setLang(self, inp, out):
		if inp in self.LANGUAGES:
			self.in_lang = inp
		else:
			ID = self.getLangID(inp) 
			if ID:
				self.in_lang = ID
		if out in self.LANGUAGES:
			self.out_lang = out
		else:
			ID = self.getLangID(out) 
			if ID:
				self.out_lang = ID
	def show(self):
		print(str(self)[str(self).index('>')+2:])
	def getTranslation(self, text):
		return self.translate(text).text
	def getSimilar(self, text):
		data = self.translate(text).extra_data['all-translations']
		if data:
			return data[0][1]
		return None
	def getSource(self):
		return self.in_lang if self.in_lang != self.UNKOWN else None
	def getDestination(self):
		return self.out_lang if self.out_lang != self.UNKOWN else None
	def translate(self, text):
		source = self.getSource()
		destination = self.getDestination()
		if source and destination:
			return self.translator.translate(text, src=source, dest=destination)
		elif source:
			return self.translator.translate(text, src=source)
		else:
			return self.translator.translate(text, dest=destination)
	def detectLang(self, text):
		return self.translator.detect(text).lang
	def getLangID(self, lang):
		if lang in self.LANGUAGES:
			return lang
		for language in self.LANGUAGES:
			if self.LANGUAGES[language] == lang:
				return language
		return None
	def swap(self):
		self.setLang(self.out_lang, self.in_lang)
	def __str__(self):
		return f'<Translator object> [{self.in_lang}] -> [{self.out_lang}]'

def printList(lst):
	max_size = 5
	if len(lst) > max_size:
		lst = lst[:max_size]
	print('[',end='')
	for i,item in enumerate(lst):
		if i != len(lst)-1:
			print(item, end=', ')
		else:
			print(item, end=']\n')

def main():
	if len(sys.argv) > 2:
		in_lang = sys.argv[1]
		out_lang = sys.argv[2]
	else:
		in_lang = input('In language: ')
		out_lang = input('Out language: ')

	translator = Translator()
	translator.setLang(in_lang, out_lang)
	translator.show()

	print('\nEnter "q" to quit')
	while True:
		text = input("Text: ")
		if text == 'q':
			break
		elif text == 'swap':
			translator.swap()
			translator.show()
		else:
			translation = translator.getTranslation(text)
			synonyms = translator.getSimilar(text)
			print('Translation:', translation)
			if synonyms:
				print('Possible synonyms:', end=' ')
				printList(synonyms)
			print()

if __name__ == '__main__':
	main()