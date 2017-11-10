#imports
from nltk.corpus import wordnet as wn

#bank
words = []

#helpers
def word_list_without_duplicates(word_list):
    # remove duplicates by putting in a set
    word_list = set(word_list)
    # join word_list together with commas
    return ', '.join(word_list)

def related_synsets(synset):
    return (
        synset.hyponyms() +
        synset.part_holonyms() +
        synset.substance_holonyms() +
        synset.part_meronyms() +
        synset.substance_meronyms()
    )

#loop
while True:

    #input system
    input_text = raw_input("analyze: ")

    #analyzer
    split_input = input_text.split()
    print " "
    for word in split_input:
        print "--"+word.upper()+"--NOUN--",
        synsets = wn.synsets(word, 'n')
        lemma_names = []
        for synset in synsets:
            for entry in related_synsets(synset):
                lemma_names += entry.lemma_names()
        print word_list_without_duplicates(lemma_names),

        print "--"+word.upper()+"--VERB--",
        synsets = wn.synsets(word, 'v')
        lemma_names = []
        for synset in synsets:
            for entry in related_synsets(synset):
                lemma_names += entry.lemma_names()
        print word_list_without_duplicates(lemma_names),

        print "--"+word.upper()+"--ADJ--",
        token_a = wn.synsets(word, 'a')
        lemma_names = []
        for entry in token_a:
            lemma_names += entry.lemma_names()
        print word_list_without_duplicates(lemma_names),

        print "--"+word.upper()+"--ADV--",
        token_r = wn.synsets(word, 'r')
        lemma_names = []
        for entry in token_r:
            lemma_names += entry.lemma_names()
        print word_list_without_duplicates(lemma_names),

        print " "
        print " "

    #adder
    final_input = raw_input("select: ")
    words.append(final_input)

    #shower
    print words

    #exiter
    if input_text == "  ":
        print " "
        print " ".join(words)
        print " "
        break
