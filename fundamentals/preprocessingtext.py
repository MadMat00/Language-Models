# Text preprocessing program
from nltk.stem.porter import PorterStemmer
import nltk

text = """
frase di esempio per il preprocessing del testo. la frase è composta da 10 parole. che in realtà non sono 10 ma sono di
meno, ma adesso che ci penso, forse sono più di 10. ma non so. sto scrivendo a caso per vedere se funziona il programma.
ciao
"""
text = text.lower()

# Tokenize the text
tokens = text.split()

# Stem the tokens
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Print the stemmed tokens with stopwords
print("Non filtrate:\n",stemmed_tokens)

# Remove stopwords
stopwords = set(nltk.corpus.stopwords.words('italian'))
filtered_tokens = [token for token in stemmed_tokens if token not in stopwords]
print("Filtrate:\n",filtered_tokens)
