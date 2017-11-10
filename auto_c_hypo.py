#imports
from nltk.corpus import wordnet as wn
import re

#bank
words = []
joined = " "

#parsing utilities
def return_words_one(entry):
    h_bank = []
    h_bank.append(str(entry))
    regex = r'\w+'
    result = re.findall(regex, h_bank[0])
    print result[1]+',',

def return_words_two(entry):
    h_bank = []
    h_bank.append(str(lemma))
    regex = r'\w+'
    result = re.findall(regex, h_bank[0])
    print result[1]+',',
    print result[4]+',',


#loop
while True:

    #input system
    input = raw_input("analyze: ")

    #analyzer
    split_input = input.split()
    print " "
    for word in split_input:
        try:
            print "--"+word.upper()+"--NOUN--",
            ss = wn.synsets(word, 'n')
            for i in ss:
                for entry in i.hyponyms():
                    return_words_one(entry)
                for entry in i.part_holonyms():
                    return_words_one(entry)
                for entry in i.substance_holonyms():
                    return_words_one(entry)
                for entry in i.part_meronyms():
                    return_words_one(entry)
                for entry in i.substance_meronyms():
                    return_words_one(entry)
        except IndexError:
            pass
        try:
            print "--"+word.upper()+"--VERB--",
            ss = wn.synsets(word, 'v')
            for i in ss:
                for entry in i.hyponyms():
                    return_words_one(entry)
                for entry in i.part_holonyms():
                    return_words_one(entry)
                for entry in i.substance_holonyms():
                    return_words_one(entry)
                for entry in i.part_meronyms():
                    return_words_one(entry)
                for entry in i.substance_meronyms():
                    return_words_one(entry)
        except IndexError:
            pass
        try:
            print "--"+word.upper()+"--ADJ--",
            token_a = wn.synsets(word, 'a')
            for i in token_a:
                for lemma in i.lemmas():
                    return_words_two(entry)
        except IndexError:
            pass
        try:
            print "--"+word.upper()+"--ADV--",
            token_r = wn.synsets(word, 'r')
            for i in token_r:
                for lemma in i.lemmas():
                    return_words_two(entry)
        except IndexError:
            pass
        print " "
        print " "

    #adder
    final_input = raw_input("select: ")
    words.append(final_input)

    #shower
    print words

    #exiter
    if input == "  ":
        print " "
        print " ".join(words)
        print " "
        break
