
import re
import nltk
import pickle
import numpy as np
from keras.models import load_model
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

token_path = "C:/Users/RYuK/NewTweetAnalysis/tokenizer.pickle"

#Loading model
model = load_model("C:/Users/RYuK/SentAnalysiModel01.h5")
history = pickle.load(open("C:/Users/RYuK/SentAnalysiHistory.p", 'rb'))


def decontracted(phrase):
    # specific
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    phrase = re.sub(r"http\S+", "", phrase)
    return phrase

stopwords= set(['br', 'the', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
            'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
            'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',\
            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',\
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
            's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
            've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',\
            "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',\
            "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", \
                'won', "won't", 'wouldn', "wouldn't"])


def clean_sentences(sentence):
    lines = []
    
    for sent in sentence:
        review_text = decontracted(sent)       
        review_text = re.sub("[^a-zA-Z]"," ", review_text)
        review_text = ' '.join(e.lower() for e in review_text.split() if e.lower() not in stopwords)
        words = word_tokenize(review_text.lower())
        lemmatizer = WordNetLemmatizer()
        lemma_words = [lemmatizer.lemmatize(i) for i in words]
        lines.append(lemma_words)
    
    return(lines)

def tokenize(lines,token_path):
    tokenized = pickle.load(open(token_path, 'rb'))
    tokenized.fit_on_texts(lines)
    word_index = tokenized.word_index
    lines = tokenized.texts_to_sequences(lines)
    lines = pad_sequences(lines,maxlen = 50,truncating= 'post',padding='post')
    return lines

def prediction(text):
    x = text
    x_review = clean_sentences(x)
    x_token = tokenize(x_review,token_path)
    preds = model.predict(x_token)

    return preds



if __name__ == "__main__":
    text = [
        "Tenet is a good movie"
        ]

print(prediction(text))