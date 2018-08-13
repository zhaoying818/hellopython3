vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search: ")
found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
        
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s)')
