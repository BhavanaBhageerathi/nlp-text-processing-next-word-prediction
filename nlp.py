# -*- coding: utf-8 -*-

"""
DEMONSTRATE NLP TASKS LIKE TOKENIZATION,LEMMATIZATION,STEMMING,STOPWORD REMOVAL USING LIBRARIES nltk and spaCy
"""

# pip install nltk spacy

# #download the english model for spacy
# python -m spacy download en_core_web_sm

#import the required packages
import nltk
import spacy

from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer,WordNetLemmatizer

#download the necessary resources
#punkt and punkt_tab are secure dataset packs required by the natural language Toolkit(NLTK) to handle sentence and word tokenization
nltk.download('punkt')
nltk.download("punkt_tab")
nltk.download('stopwords')
nltk.download('wordnet')

#load the spacy model
nlp=spacy.load("en_core_web_sm")

#define a sample text
mytext='''the cat sat on the mat. The dog lay on the rug.
The cat chased the dog. The dog barked at the cat'''
print("original text",mytext)

#task1:Tokenization- splitting the text into words
mytokens=word_tokenize(mytext)
print("Tokenization using NLTK",mytokens)

#task2:remove all the stopwords eg:'the','is'
#stopwrds edhokjeyahnen namk ariyanum atb nammal dwnld aki vechit ond..load that..then compare it with each word in our txt
set_of_stop_words= set(stopwords.words("english"))
#if words in our token are present in the set of stopwords
#discard them
filtered_tokens=[word for word in mytokens if word.lower() not in set_of_stop_words]
print("stop word removed tokens using NLTK",filtered_tokens)#mytokensile listin oro wordine edkugua enit elathonum lwr case convert akuga enit checkif it is not in stop words set if not then store it to filtered_tokens

#task3: stemming (Reduce the words into its root form)
stemmer= PorterStemmer()
#using a for loop stem each word in the filtered_tokens
stemmed_filtered_tokens=[stemmer.stem(word) for word in filtered_tokens]
print("stemmed tokens using NLTK",stemmed_filtered_tokens)

#task4: Lemmatization (reduce words into dictionary form)
lemmatizer=WordNetLemmatizer()
lemmatized_filtered_tokens=[lemmatizer.lemmatize(word) for word in stemmed_filtered_tokens]
print("lemmatized tokens using NLTK",lemmatized_filtered_tokens)

#task5: Finding POS -Parts of speech#oro wordine edth ath edh parts of speechil varuemnn tag chyna paripadi
mypos= [(token.text,token.pos_) for token in nlp(mytext)]
print("POS using spacy",mypos)

"""NLP WORD PREDICTION USING N-GRAM(BI-GRAM) USING THE LIST OF TOKENS THAT WE HAVE"""

#import required function for creating bigram
import random
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import defaultdict

#create a bigram(n gram with n=2)
#n-gram is a lamngiage model that predicts the probability of a given n-gram within any sequence of words in a lamguage
bigram= list(ngrams(mytokens,2))
print("bigrams using nltk",bigram)#[('firstword','nextword),("nextword",'nexttonextword")]

#using the bigram,create a dictionary of word predictions
word_dict=defaultdict(list)
for word1,word2 in bigram:
  word_dict[word1].append(word2)
word_dict#the vannal adtha varunna words edhoke.. etc
#{keyword":[list of next possible words]}

#define a function to do the prediction
def predict_next_word(word):
  if word in word_dict:
    #pick a random value for the key"word" in the word_dict
    return random.choice(word_dict[word])
  else:
    return "word not found"

print(predict_next_word("the"))

print(predict_next_word("dog"))