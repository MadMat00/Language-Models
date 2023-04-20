# POS tagging program
"""
Il POS tagging serve a classificare le parole in base al loro significato.

Esempio:
    cat: nome
    is: verbo ecc...
"""

import nltk

sentence = "The cat is braking my balls."

tokens = nltk.word_tokenize(sentence)

pos_tags = nltk.pos_tag(tokens)

print(pos_tags)

#leggenda che spiega ai non rettiliani cosa significa ogni tag
for token, tag in pos_tags:
    print(token, ":", nltk.help.upenn_tagset(tag))
