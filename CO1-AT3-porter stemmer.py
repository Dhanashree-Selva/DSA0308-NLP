class PorterStemmer:

    # Function to calculate measure (m)
    def measure(self, stem):

        vowels = "aeiou"
        m = 0
        prev_is_vowel = False

        for ch in stem:

            is_vowel = ch in vowels

            # Count Vowel → Consonant transitions
            if prev_is_vowel and not is_vowel:
                m += 1

            prev_is_vowel = is_vowel

        return m


    # Step 2 of Porter Stemmer
    def step2(self, word):

        # Rule 11 : IZATION → IZE
        if word.endswith("ization"):

            stem = word[:-7]      # Remove "ization"

            if self.measure(stem) > 0:
                return stem + "ize"

        # Rule 13 : ATOR → ATE
        if word.endswith("ator"):

            stem = word[:-4]      # Remove "ator"

            if self.measure(stem) > 0:
                return stem + "ate"

        return word


# ---------------- Main Program ----------------

# Create an object
ps = PorterStemmer()

# Input words
word1 = "organization"
word2 = "operator"

# Display results
print("Original Word :", word1)
print("Stem :", word1[:-7])
print("Measure Value :", ps.measure(word1[:-7]))
print("Stemmed Word :", ps.step2(word1))

print()

print("Original Word :", word2)
print("Stem :", word2[:-4])
print("Measure Value :", ps.measure(word2[:-4]))
print("Stemmed Word :", ps.step2(word2))
