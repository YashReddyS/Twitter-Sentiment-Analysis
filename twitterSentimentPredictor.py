
import numpy as np
from keras.models import load_model
import pickle
from keras.preprocessing.sequence import pad_sequences


# Load model
model = load_model('best_model.h5')

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def predict_class(text):
    '''Function to predict sentiment class of the passed text'''

    text = np.expand_dims(text, axis=0)

    sentiment_classes = ['Negative', 'Neutral', 'Positive']
    max_len = 50

    # Transforms text to a sequence of integers using a tokenizer object
    xt = tokenizer.texts_to_sequences(text)
    # Pad sequences to the same length
    xt = pad_sequences(xt, padding='post', maxlen=max_len)
    # Do the prediction using the loaded model
    yt = model.predict(xt).argmax(axis=1)
    # Print the predicted sentiment
    return sentiment_classes[yt[0]]

#predict_class(["@Tesmanian_com The Tesla China team is amazing"])