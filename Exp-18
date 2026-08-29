import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet

sentences = ["I went to the bank to deposit money","I sat at the bank of river"]
for sentence in sentences:
  words = sentence.split()
  result = lesk(words, "bank")
  print("Sentence:", sentence)
  print("Ambiguous word: bank")
  if result:
      print("Selected sense:", result.name())
      print("Definition:", result.definition())
  else:
      print("No sense found")
  print()
