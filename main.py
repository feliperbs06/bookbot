path_to_file = "books/frankenstein.txt"

def count_letters(string):
    dict_letters = {}
    for letter in string:
        letter_lower = letter.lower()
        if letter_lower in dict_letters:
            dict_letters[letter_lower] += 1
        else:
            dict_letters[letter_lower] = 1
    return dict_letters

def print_report(file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    dict_letters = count_letters(file_contents)
    most_common_letters = sorted(dict_letters.items(), key=lambda x: x[1], reverse=True)
    
    print(f"--- Begin report of {file} ---")
    print(f"{len(file_contents.split())} words found in the document")
    print("\n")
    for key, value in most_common_letters:
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


print_report(path_to_file)