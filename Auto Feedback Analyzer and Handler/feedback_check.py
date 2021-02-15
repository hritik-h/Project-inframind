import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import matplotlib.pyplot as plt

def predict():
    def predict_feedback(message):
        pos = 0
        neg = 0
        model = tf.keras.models.load_model("inframinModel.h5")
        res =  model.predict(message).reshape(-1)
        for each in res:
            if each > .5:
                pos += 1
            else:
                neg += 1
        return (pos,neg)
    	#return testing_padded


    with open('tokenizer.pickle', 'rb') as handle:
    	tokenizer = pickle.load(handle)

    tweets = pd.read_csv('file.csv', header = None)
    emails = pd.read_csv('file1.csv', header = None)

    t = tokenizer.texts_to_sequences(tweets[0])
    t = pad_sequences(t , maxlen = 255)

    t1 = tokenizer.texts_to_sequences(emails[0])
    t1 = pad_sequences(t1 , maxlen = 255) 



    res = (predict_feedback(t), predict_feedback(t1))

    return res

def result_viewer(tup):
    fig, (axs, axs1, axs2) = plt.subplots(1,3)
    fig.tight_layout()
    fig.suptitle('Tweet Analysis')
    axs.pie([tup[0][0],tup[0][1]], labels = ["Positive","Negative"],colors=('green','red'),autopct='%1.1f%%')
    axs.title.set_text('Tweets')
    axs1.pie([tup[1][0],tup[1][1]], labels = ["Positive","Negative"],colors=('green','red'),autopct='%1.1f%%')
    axs1.title.set_text('email')
    axs2.pie([tup[0][0]+tup[1][0],tup[0][1]+tup[1][1]], labels = ["Positive","Negative"],colors=('green','red'),autopct='%1.1f%%')
    axs2.title.set_text('Overall')
    plt.show() 


