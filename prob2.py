strings = ['tie', 'shoes', 'hello there', 'dog', 'do', 'brags', 'the quick brown fox jumped over the lazy dog']

sorted_strings = sorted(strings, key=lambda x: (len(x), x))
print(sorted_strings)