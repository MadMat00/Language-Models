"""
Attempt to create a phrase predictor in python.
It will work by importing a text file, by goin 
trought all the phrases it will use a dictionary 
to store the words and then memorize what are the 
words that appears next and the probability of
that word to appear next.

"""

#import the libraries to read the txt  file
import os
import re
import json

#function to read the txt file
def read_file(file_name):
    file = open(file_name, 'r')
    file_content = file.read()
    file.close()
    return file_content

#function to create the dictionary
def create_dictionary(text):
    dictionary = {}
    phrases = text.split('.')
    for phrase in phrases:
        words = phrase.split(' ')
        for i in range(len(words)-1):
            if words[i] not in dictionary:
                dictionary[words[i]] = {}
            if words[i+1] not in dictionary[words[i]]:
                dictionary[words[i]][words[i+1]] = 1
            else:
                dictionary[words[i]][words[i+1]] += 1
    #saves the dictionary in a json file
    with open('Next Word Predictor\\dict.json', 'w') as fp:
        json.dump(dictionary, fp, indent=4)


    return dictionary

#function to predict the next word
def predict_next_word(dictionary, word):
    if word in dictionary:
        next_words = dictionary[word]
        next_word = max(next_words, key=next_words.get)
        return next_word
    else:
        return None
#new predict next word function that returns a list of the next words and their probability
def predict_next_word_list(dictionary, word):
    if word in dictionary:
        next_words = dictionary[word]
        next_word = max(next_words, key=next_words.get)
        return next_word
    else:
        return None
    
    
text = read_file('Next Word Predictor\\text.txt')
dictionary = create_dictionary(text)

print(predict_next_word_list(dictionary, 'cursus'))



