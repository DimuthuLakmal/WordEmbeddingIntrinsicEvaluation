__author__ = 'kjtdi'

#This script is for training glove embeddings.
#First we read preprocessed text files consists of sentences in each line and push tokenized sentences to an array.
#Then train glove models with preferred hyper parameters and save trained model into the disk

from sinling.sinhala.tokenizer import SinhalaTweetTokenizer
from glove import Corpus, Glove
import codecs

import os
import pickle

f_1 = codecs.open("Preprocessed/test_1_no_stop.txt", encoding='utf-8', errors='ignore')
f_2 = codecs.open("Preprocessed/test_2_no_stop.txt", encoding='utf-8', errors='ignore')
f_3 = codecs.open("Preprocessed/test_3_no_stop.txt", encoding='utf-8', errors='ignore')
f_4 = codecs.open("Preprocessed/test_4_no_stop.txt", encoding='utf-8', errors='ignore')
f_5 = codecs.open("Preprocessed/test_5_no_stop.txt", encoding='utf-8', errors='ignore')
f_6 = codecs.open("Preprocessed/test_6_no_stop.txt", encoding='utf-8', errors='ignore')

tokenizer = SinhalaTweetTokenizer()

#tokenize sentences and push into an array
sentences = []
for line in f_1:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))

print("Finished File 1")

for line in f_2:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))

print("Finished File 2")

for line in f_3:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))

print("Finished File 3")

for line in f_4:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))

print("Finished File 4")

for line in f_5:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))

print("Finished File 5")

for line in f_6:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))

print("Finished File 6")

#if you want you can save the processed corpus into seperate file in the disk so that you can save your time next time training
pickle_out = open("sentences.pickle","wb")
pickle.dump(sentences, pickle_out)
pickle_out.close()

corpus = Corpus()
corpus.fit(sentences, window=10)

#define glove model with preferred parameters
glove = Glove(no_components=300, learning_rate=0.05)

#train glove model
glove.fit(corpus.matrix, epochs=50, no_threads=8, verbose=True)
glove.add_dictionary(corpus.dictionary)

#save trained model to disk
if not os.path.exists("trained_glove_300_nsw"):
    os.makedirs("trained_glove_300_nsw")

glove.save(os.path.join("trained_glove_300_nsw", "glove_300_nsw.model"))
