from collections import Counter

string = "To change the overall look of your document. To change the look available in the gallery"
# Convert the string to lowercase and split it into words
words = string.lower().split()

# Use Counter to count occurrences of each word
word_count = Counter(words)

print(word_count)
