import nltk
from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()
import json
import pickle

def preprocess():
	words=[]
	words_f=[]
	tags=[]
	docs=[]
	ignore_words = ['?', '!',',','.']
	with open('intents.json') as file:
		intents=json.load(file)

	for i in intents["intents"]:
		for pattern in i['patterns']:
			w=nltk.word_tokenize(pattern)
			words.extend(w)

			docs.append((w, i['tag']))

			if i['tag'] not in tags:
				tags.append(i['tag'])

	for w in words:
		if w in ignore_words:
			continue
		else:
			w_1=lem.lemmatize(w.lower())
			words_f.append(w_1)
	words_f = sorted(list(set(words_f)))


	pickle.dump(words_f,open('words.pkl','wb'))
	pickle.dump(tags,open('tags.pkl','wb'))
	return words_f,tags,docs