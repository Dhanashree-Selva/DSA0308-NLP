import re

text = """Artificial Intelligence (AI) is transforming industries across the world.
AI is used in healthcare to assist doctors in diagnosis, in banking to detect fraud,
and in education to provide personalized learning experiences.
Many companies invest heavily in AI research because AI improves efficiency and enables intelligent decision-making.
As AI continues to evolve, professionals with AI skills are in high demand."""

# Sentence Split
sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]

# Word Split
words = re.split(r'\s+', text)

print("Total Sentences:", len(sentences))
print("Total Words:", len(words))

print("\nSentences:")
for s in sentences:
    print(s)

print("\nWords:")
print(words)
