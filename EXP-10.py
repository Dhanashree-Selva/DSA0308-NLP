# Transformation-Based Tagging (Simple Rule-Based)

sentence = input("Enter a sentence: ")

words = sentence.split()

# Initial tagging
tags = []

for word in words:
    if word.lower() in ["is", "am", "are", "was", "were"]:
        tags.append("VB")
    elif word.lower() in ["a", "an", "the"]:
        tags.append("DT")
    else:
        tags.append("NN")      # Default tag

print("\nInitial Tags")
for w, t in zip(words, tags):
    print(f"{w} --> {t}")

# Transformation Rule:
# If a word ends with 'ing' and is tagged as NN,
# change it to VBG.

for i in range(len(words)):
    if words[i].endswith("ing") and tags[i] == "NN":
        tags[i] = "VBG"

print("\nAfter Applying Transformation Rule")
for w, t in zip(words, tags):
    print(f"{w} --> {t}")
