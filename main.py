path_to_file = "books/frankenstein.txt"

def count_letters(string):
    dict_letters = {}
    for letter in string:
        letter_lower = letter.lower()
        if letter_lower in dict_letters:
            dict_letters[letter_lower] += 1
        else:
            dict_letters[letter_lower] = 1
    return sorted(dict_letters.items(), key=lambda x: x[1], reverse=True)

def print_report(file, length, most_common_letters):
    print(f"--- Begin report of {file} ---")
    print(f"{length} words found in the document")
    print("\n")
    for key, value in most_common_letters:
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


def main():
    with open(path_to_file) as f:
        file_contents = f.read()
    
    length_words = len(file_contents.split())
    most_common_letters = count_letters(file_contents)

    print_report(path_to_file, length_words, most_common_letters)


main()
