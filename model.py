from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import Adam
import numpy as np
from training_data_creation import data_creator
def model_c():
	data_creator()
	X=np.load('X_train.npy')
	Y=np.load('Y_train.npy')
	model = Sequential()
	model.add(Dense(32, input_shape=(len(X[0]),), activation='relu'))
	model.add(Dropout(0.2))
	model.add(Dense(64, activation='relu'))
	model.add(Dropout(0.3))
	model.add(Dense(128, activation='relu'))
	model.add(Dropout(0.3))
	model.add(Dense(len(Y[0]), activation='softmax'))

	adam=Adam(lr=0.001)
	model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
	return model,X,Y
