# Specific_Related_Word_Prompter
This script analyzes user input and suggests more specific words the author could use, as well as a series of related words that may be valuable. It is an interface build on top of Wordnet (https://wordnet.princeton.edu/)

## Installation

1. If you do not already have the Natural Language Toolkit (NLTK), installation instructions can be found [here](http://www.nltk.org/install.html).
2. Clone this repo (or simply download the 'auto_c_hypo.py' file to your Desktop) 

## How to run

SpecificRelated Word Prompter is a command-line application (for now). Follow these steps to run it:

1. Place 'auto_c_hypo.py' on your Desktop (or preferred location)
2. Open your terminal 
3. Change your directory to the location of 'auto_c_hypo.py' (e.g. `cd Desktop` if file is on your Desktop)
4. Type `python auto_c_hypo.py`
5. Type some langauge into your terminal (e.g. "man"), then press Enter
6. The terminal will then display more specific alternative words for the words that you type, as well as some related words.
7. Select which alternative words you want to use (e.g. "adonis" for "man") by retyping them and hitting Enter (you can also just retype your original word to keep it). In this way, you build up a longer composition. 
8. To stop the program and print out the text you've entered, type in " " when asked for a prompt. You may have to enter this up to three times for the program to quit and print out the text you've compiled so far.
