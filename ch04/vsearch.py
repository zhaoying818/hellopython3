def search4vowels(word:str) -> set:
    """Return a boolean based on any vowels found."""
    vowels = set('aeiou')
    #word = input("Provide a word to search: ")
    found = vowels.intersection(set(word))
    return found
