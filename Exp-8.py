# Simple Stochastic POS Tagger

import random

# Dictionary with possible POS tags
tag_dictionary = {
    "book": ["NN", "VB"],
    "play": ["NN", "VB"],
    "run": ["NN", "VB"],
    "apple": ["NN"],
    "beautiful": ["JJ"],
    "quickly": ["RB"]
}

sentence = input("Enter a sentence: ").lower().split()

print("\nWord\tAssigned POS")
print("-"*30)

for word in sentence:
    if word in tag_dictionary:
        tag = random.choice(tag_dictionary[word])
    else:
        tag = "NN"
    print(f"{word:12}{tag}")
