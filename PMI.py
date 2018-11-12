from nltk.corpus import brown
import unicodedata
import re
from math import log

bigram_freq  = {}
unigram_freq = {}
total_bigram = 0
total_unigram = 0
cnt = 0

def calculate_PMI(word1 , word2):
	prob_bigram  = bigram_freq[(word1, word2)]/total_bigram
	prob_unigram1 = unigram_freq[word1] / total_unigram
	prob_unigram2 = unigram_freq[word2] / total_unigram
	print prob_bigram , prob_unigram1 , prob_unigram2
	return log( ((prob_bigram) ) / (prob_unigram1 * prob_unigram2)  )



for sent in brown.sents():
	i = 0
	pre = ""
	for word in sent:
		word = str(word)
		word = re.sub('[^A-Za-z0-9]+', '', word)
		if(len(word)==0):
			continue
		if word not in unigram_freq:
			unigram_freq[word] = 0
		unigram_freq[word] += 1
		total_unigram += 1
		if(i>0):
			bigram = (pre , word)
			if bigram not in bigram_freq:
				bigram_freq[bigram] = 0
			bigram_freq[bigram] += 1
			total_bigram += 1
		i += 1
		pre = word


print calculate_PMI('hong' , 'kong')


