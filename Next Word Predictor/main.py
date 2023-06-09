"""
Attempt to create a phrase predictor in python.
It will work by importing a text file, going 
trought all the phrases and using a dictionary 
to store the words; it will then memorize what
words appear next and the associated probability.
"""
# TODO: create usecase for os and re modules
# import os
# import re
import json


def read_file(file_name: str) -> str:
    """Function that reads a given txt file
    returning its content as a string"""
    with open(file_name, "r") as file:
        file_content = file.read()
    
    return file_content


def create_dictionary(text: str) -> dict:
    """Function that creates and returns
    a dictionary using a given text"""
    dictionary = {}
    phrases = text.split('.')
    
    for phrase in phrases:
        words = phrase.split(' ')
        for i in range(len(words)-1):
<<<<<<< HEAD
            if words[i] not in dictionary:
                dictionary[words[i]] = {}
            if words[i+1] not in dictionary[words[i]]:
                dictionary[words[i]][words[i+1]] = 1
            else:
                dictionary[words[i]][words[i+1]] += 1
    #saves the dictionary in a json file
    with open('Next Word Predictor\\dict.json', 'w') as fp:
=======
            # searches for the word in the dictionary, 
            # if it doesn't exist it creates it
            dictionary.setdefault(words[i], {})
            sub_dictionary = dictionary[words[i]]
            # searches for the next word in the sub_dictionary,
            # if it doesn't exist it creates it, and increments it
            sub_dictionary[words[i+1]] = sub_dictionary.get(words[i+1], 0) + 1
                
    # saves the dictionary in a json file
    with open('prova\\dict.json', 'w') as fp:
>>>>>>> 34b55d2da064db1dc05fbfecd8eb8d92638cefcb
        json.dump(dictionary, fp, indent=4)

    return dictionary


def predict_next_word(dictionary: dict, word: str) -> str | None:
    """Function that predicts a likely next word
    using a given dictionary and word"""
    if word in dictionary:
        next_words = dictionary[word]
        next_word = max(next_words, key=next_words.get)
        return next_word
    else:
        return None
<<<<<<< HEAD
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
=======
>>>>>>> 34b55d2da064db1dc05fbfecd8eb8d92638cefcb


if __name__ == "__main__":
    text = read_file('prova\\text.txt')
    dictionary = create_dictionary(text)

    print(predict_next_word(dictionary, 'cursus'))
