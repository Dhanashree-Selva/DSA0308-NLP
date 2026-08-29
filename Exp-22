import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter a text: ")

doc = nlp(text)

entities = {}

for token in doc:
    if token.pos_ in ["NOUN", "PROPN"]:
        entities[token.text] = token.text

for token in doc:
    if token.text.lower() in ["he", "she", "it", "they"]:
        previous = [t.text for t in doc[:token.i] if t.pos_ in ["NOUN", "PROPN"]]
        if previous:
            print(token.text, "->", previous[-1])

  """
  John went to the park. He played football.
  """
