import googletrans
import sys

class Translator:
	LANGUAGES = googletrans.LANGUAGES
	def __init__(self):
		self.translator = googletrans.Translator()
		self.in_lang = 'en'
		self.out_lang = 'es'
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
		print(f'[{self.in_lang}] -> [{self.out_lang}]')
		print('Enter "swap" to flip')
	def getTranslation(self, text):
		return self.translate(text).text
	def getSimilar(self, text):
		return self.translate(text).extra_data['all-translations']
	def translate(self, text):
		return self.translator.translate(text, src=self.in_lang, dest=self.out_lang)
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
		return f'<Translator object> in_lang: {self.in_lang} out_lang: {self.out_lang}'



def main():
	if len(sys.argv) > 2:
		in_lang = sys.argv[1]
		out_lang = sys.argv[2]
	else:
		in_lang = input('In language: ')
		out_lang = input('Out language: ')

	translator = Translator()
	translator.setLang(in_lang, out_lang)

	print('\nEnter "q" to quit')
	while True:
		text = input("Text: ")
		if text == 'q':
			break
		elif text == 'swap':
			translator.swap()
		else:
			translation = translator.translate(text)
			print('Translation:', translator.getTranslation(text))
			synonyms = translator.getSimilar(text)
			if synonyms:
				print('Possible synonyms:', synonyms[0][1])
			print()

if __name__ == '__main__':
	main()