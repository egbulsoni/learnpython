sentence = "the quick brown for jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        if word != "the":
            word_lengths.append(len(word))

word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
ns = [n for n in numbers if n >= 0]
print(numbers)
print(ns)