import nltk
from nltk.corpus import wordnet

word = "car"

synsets = wordnet.synsets(word)

print("Word:", word)
print("Number of synsets:", len(synsets))

for synset in synsets:
    print("\nSynset:", synset.name())
    print("Definition:", synset.definition())
    print("Examples:", synset.examples())

    synonyms = synset.lemmas()
    print("Synonyms:", [lemma.name() for lemma in synonyms])
