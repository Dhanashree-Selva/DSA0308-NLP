import  nltk
from nltk import CFG
from nltk.parse import ChartParser
grammar=CFG.fromstring ("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat'|'dog'
V -> 'chased'
""")
parser=ChartParser(grammar)
sentence="The cat chased the dog".lower().split()
trees=list(parser.parse(sentence))
if trees:
  print("Sentence is accepted")
  for tree in trees:
    print(tree)
    tree.pretty_print()
else:
  print("Sentence is rejected")
