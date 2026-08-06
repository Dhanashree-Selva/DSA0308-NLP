import nltk

# Rule-based grammar
patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ly$', 'RB'),
    (r'.*ness$', 'NN'),
    (r'.*ment$', 'NN'),
    (r'.*ous$', 'JJ'),
    (r'.*able$', 'JJ'),
    (r'.*s$', 'NNS'),
    (r'.*', 'NN')
]

tagger = nltk.RegexpTagger(patterns)

sentence = input("Enter a sentence: ").split()

tags = tagger.tag(sentence)

print("\nWord\tPOS")
print("-"*25)

for word, tag in tags:
    print(f"{word:12}{tag}")
