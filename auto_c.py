#autocomplete by character (!)
#https://pypi.python.org/pypi/autocomplete/0.0.104
#import autocomplete
#autocomplete.load()
#print autocomplete.predict("the", "b")

#from autocomplete import models
#models.train_models("some giant string")

#autocomplete by word (!)
import sys
import random
from collections import defaultdict
def build_conditional_probabilities(corpus):
	"""
	The function takes as its input a corpus string (words separated by
	spaces) and returns a 2D dictionnary of probabilities P(next|current) of
	seeing a word "next" conditionnaly to seeing a word "current".
	"""
	# First we parse the string to build a double dimension dictionnary that
	# returns the conditional probabilities.

	# We parse the string to build a first dictionnary indicating for each
	# word, what are the words that follow it in the string. Repeated next
	# words are kept so we use a list and not a set.
	tokenized_string = corpus.split()
	previous_word = ""
	dictionnary = defaultdict(list)
	for current_word in tokenized_string:
		if previous_word != "":
			dictionnary[previous_word].append(current_word)
		previous_word = current_word
	# We know parse dictionnary to compute the probability each observed
	# next word for each word in the dictionnary.
	for key in dictionnary.keys():
		next_words = dictionnary[key]
		unique_words = set(next_words) # removes duplicated
		nb_words = len(next_words)
		probabilities_given_key = {}
		for unique_word in unique_words:
			probabilities_given_key[unique_word] = \
				float(next_words.count(unique_word)) / nb_words
		dictionnary[key] = probabilities_given_key
	return dictionnary

def bigram_next_word_predictor(conditional_probabilities, current, next_candidate):
	"""
	The function takes as its input a 2D dictionnary of probabilities
	P(next|current) of seeing a word "next" conditionnaly to seeing a word
	"current", the current word being read, and a next candidate word, and
	returns P(next_candidate|current).
	"""
	# We look for the probability corresponding to the
	# current -> next_candidate pair
	if conditional_probabilities.has_key(current):
		if conditional_probabilities[current].has_key(next_candidate):
			return conditional_probabilities[current][next_candidate]
	# If current -> next_candidate pair has not been observed in the corpus,
	# the corresponding dictionnary keys will not be defined. We return
	# a probability 0.0
	return 0.0

# An example corpus to try out the function
#corpus = "the cat is red the cat is green the cat is blue the dog is brown"
corpus = "This is the winter of our discontent! Don't you think so! I do think so! That's the end of all of us. And you too!"
# We call the conditional probability dictionnary builder function
conditional_probabilities = build_conditional_probabilities(corpus)

#autocomplete by word (!)

#def next_word (word):
#	return random.choice(conditional_probabilities[word].keys())

#autocomplete by phrase (!)

#def next_phrase(word, n):
#	if n == 0:
#		return phrase
#	else:
#		token = next_word(word)
#		phrase.append(token)
#		return next_phrase(token, n-1)

#phrase = []
#next_phrase("This", 8)
#s = " "
#print s.join(phrase)

#search for word in sentences (!) [maybe redundant bc of regular expressions]

#def find_sentences(word):
#	corpus_one = corpus.replace("!", "@")
#	corpus_two = corpus_one.replace(".", "@")
#	corpus_three = corpus_two.replace("?", "@")
#	corpus_four = corpus_three.split("@")
#	word_in_sentence = []
#	for line in range(len(corpus_four)-1):
#		if word in corpus_four[line]:
#			word_in_sentence.append(corpus_four[line])
#	return word_in_sentence
#print find_sentences("the")
