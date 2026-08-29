from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is a programming language",
    "Python is used for machine learning",
    "Machine learning is a branch of artificial intelligence",
    "Artificial intelligence uses Python"
]

query = input("Enter search query: ")

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform([query])

scores = cosine_similarity(query_vector, tfidf_matrix)[0]

ranked_documents = scores.argsort()[::-1]

print("\nRanked Documents:")

for i in ranked_documents:
    print(f"Document {i + 1}: {documents[i]} -> Score: {scores[i]:.4f}")


"""
Enter search query: Python machine learning
"""
