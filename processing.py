
import numpy as np
import nltk
"nltk.download('punkt')"
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenization(sentence):
    return nltk.word_tokenize(sentence)

def stemmer(word):
    return stemmer.stem(word.lower())

def bag_of_word(tokenized_sentence,words):
    sentence_words = [stemmer(word) for word in tokenized_sentence]

    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag