from preprocessing import preprocess
from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()
import numpy as np
import random


def data_creator():
	words,tags,docs=preprocess()

	out_array=[0] * len(tags)
	train=[]

	for doc in docs:

		bag_of_words=[]
		patt=doc[0]
		patt_f=[]
		## Accessing the first part of a tuple (word,tag)

		for pat in patt:
			p=lem.lemmatize(pat.lower())
			patt_f.append(p)

		for word in words:
			if word in patt_f:
				bag_of_words.append(1)

			else:
				bag_of_words.append(0)


		# Creating vector of words

		output_req=list(out_array)
		output_req[tags.index(doc[1])] = 1
		#print(len(bag_of_words))
		#print(len(output_req))
		train.append([bag_of_words, output_req])
	random.shuffle(train)
	train=np.array(train)
	X_train=list(train[:,0])
	Y_train=list(train[:,1])	
	print("1")
	np.save('X_train.npy',X_train)
	np.save('Y_train.npy',Y_train)
    
#data_creator()
