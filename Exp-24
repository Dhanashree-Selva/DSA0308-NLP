import spacy
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

text = input("Enter a text: ")

sentences = [sent.text.strip() for sent in nlp(text).sents]

vectors = [nlp(sentence).vector for sentence in sentences]

scores = []

for i in range(len(vectors) - 1):
    score = cosine_similarity([vectors[i]], [vectors[i + 1]])[0][0]
    scores.append(score)

if scores:
    coherence = sum(scores) / len(scores)
else:
    coherence = 1.0

print("Coherence Score:", round(coherence, 4))

if coherence >= 0.5:
    print("The text is coherent.")
else:
    print("The text is not coherent.")

"""
Python is a programming language. Python is widely used for machine learning. Machine learning is used to build intelligent applications.
"""
