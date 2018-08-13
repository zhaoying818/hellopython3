def search4vowels():
    """Display any vowels found in a asked-for word."""
    vowels = set('aeiou')
    word = input("Provide a word to search: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
