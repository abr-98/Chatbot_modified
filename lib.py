from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import 	WordNetLemmatizer
import re
lem = WordNetLemmatizer()



def swap_pronouns(phrase):
	if 'I' in phrase:
		return re.sub('I','you',phrase)
	if 'my' in phrase:
		return re.sub('my','your',phrase)
	else:
		return phrase

def filter_command(phrase):
	tokens=word_tokenize(phrase)
	tags = nltk.pos_tag(tokens)

	work=[]
	work_f=[]
	subject=[]
	number=[]
	adj=[]
	query=[]
	name=0
	for tup in tags:
		if "VB" in tup[1]:
			work.append(tup[0])
		if "CD" in tup[1]:
			number.append(tup[0])
		if "JJ" in tup[1]:
			adj.append(tup[0])
		if "NN" in tup[1]:
			subject.append(tup[0])
		if "W" in tup[1] and "that" not in tup[0]:
			query.append(tup[0]) 
	for w in work:
		work_f.append(lem.lemmatize(w.lower()))
	if query:
		if "you" in tokens or "your" in tokens:
			if "VB" in nltk.pos_tag(tokens[0])[1]:
				task=1
			task=0
		if 'weather' not in tokens or 'news' not in tokens or 'headlines' not in tokens: 
			task=1
	elif 'play' in work_f or 'song' in subject or 'play' in subject:
		task=2
	elif 'book' in work_f or 'book' in tokens[0]:
		task=3
	elif 'weather' in subject:
		task=4
	elif 'news' in subject or 'headlines' in subject:
		task=5
	else:
		
		if '?' in tokens:
			task=1
		else:
			task=0	
	
	return task,work_f,subject,number,adj,query
