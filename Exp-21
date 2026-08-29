import spacy

nlp = spacy.load("en_core_web_sm")

sentence = input("Enter a sentence: ")

doc = nlp(sentence)

for chunk in doc.noun_chunks:
    print("Noun Phrase:", chunk.text)
    print("Meaning:", chunk.root.lemma_)

"""
The intelligent student reads a book.
"""
