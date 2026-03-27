with open('lost.txt') as f:
 words = [word.lower() for line in f for word in line.split()]
 words_no_punct = ["".join(char for char in word if char.isalpha())
 for word in words]
print(words_no_punct[:20]) # Print first 20 words as a QC check