def main():
    path = "./books/frankenstein.txt"
    file_contents = get_contents(path)
    word_count = count_words(file_contents)
    character_list = sort_by_frequency(count_characters(file_contents))
    print(f"--- Begin report of {path} ---\n{word_count} words found in the document\n")
    for character in character_list:
        name = character["character"]
        count = character["count"]
        print(f"The '{name}' character was found {count} times")
    print("--- End report ---")
    

def get_contents(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    word_count = len(string.split())
    return word_count

def count_characters(string):
    # Initial dictionary
    characters = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0,
        'e': 0, 'f': 0, 'g': 0, 'h': 0,
        'i': 0, 'j': 0, 'k': 0, 'l': 0,
        'm': 0, 'n': 0, 'o': 0, 'p': 0,
        'q': 0, 'r': 0, 's': 0, 't': 0,
        'u': 0, 'v': 0, 'w': 0, 'x': 0,
        'y': 0, 'z': 0
    }
    # Make each character lowercase
    lowered_string = string.lower()
    
    # Go through every character in the string, add 1 to
    # corresponding character each time it's found
    for index in range(0, len(lowered_string)):
        if lowered_string[index] in characters:
            characters[lowered_string[index]] += 1
    
    return characters

def sort_by_frequency(dictionary):
    sorted = []
    for character in dictionary:
        sorted.append({
            "character":character, "count":dictionary[character]
        })
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def sort_on(dictionary):
    return dictionary['count']


main()