from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
import nltk

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('punkt_tab')

sentence = input("Enter a sentence: ")
word = input("Enter the word to disambiguate: ")

tokens = word_tokenize(sentence)

sense = lesk(tokens, word)

if sense:
    print("Word:", word)
    print("Synset:", sense.name())
    print("Meaning:", sense.definition())
else:
    print("No sense found.")

"""
I went to the bank to deposit money.
bank
"""
