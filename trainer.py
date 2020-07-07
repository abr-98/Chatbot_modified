import tensorflow as tf
from model import model_c

def train():
	callback=tf.keras.callbacks.ModelCheckpoint(filepath='chatbot_model.h5',
                                           monitor='loss',
                                           verbose=1,
                                           save_best_only=True,
                                           save_weights_only=False,
                                           mode='auto')
	model,X,Y=model_c()
	model.fit(X, Y, epochs=500, batch_size=16,callbacks=[callback])

train()