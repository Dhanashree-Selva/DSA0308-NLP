import nltk
from nltk.tokenize import word_tokenize

# Download resources (Run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input sentence
text = "The quick brown fox jumps over the lazy dog."

# Tokenize
words = word_tokenize(text)

# POS Tagging
tags = nltk.pos_tag(words)

print("Word\t\tPOS Tag")
print("-"*30)

for word, tag in tags:
    print(f"{word:12}{tag}")
