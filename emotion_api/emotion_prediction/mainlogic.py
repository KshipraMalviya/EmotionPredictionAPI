import base64
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import nltk
import re
import os
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

base_dir = os.path.dirname(os.path.abspath(__file__))

lg_path = os.path.join(base_dir, 'logistic_regression.pkl')
lb_path = os.path.join(base_dir, 'label_encoder.pkl')
tfidf_vectorizer_path = os.path.join(base_dir, 'tfidf_vectorizer.pkl')

lg = pickle.load(open(lg_path, 'rb'))
lb = pickle.load(open(lb_path, 'rb'))
tfidf_vectorizer = pickle.load(open(tfidf_vectorizer_path, 'rb'))

stopwords_set = set(stopwords.words('english'))

def clean_text(text):
    stemmer=PorterStemmer()
    text=text.lower()
    text=re.sub("[^a-z]"," ",text)
    text=text.split()
    text=[stemmer.stem(word) for word in text if word not in stopwords_set]
    return " ".join(text)

def predict_emotion(input_text):
    cleaned_text=clean_text(input_text)
    input_vector=tfidf_vectorizer.transform([cleaned_text])
    predicted_label=lg.predict(input_vector)[0]
    predicted_emotion=lb.inverse_transform([predicted_label])[0]
    label=np.max(predicted_label)
    return predicted_emotion,label
