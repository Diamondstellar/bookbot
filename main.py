import sys
from stats import get_word_count, character_count, sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_book():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        text = get_book_text(sys.argv[1])
    return text

def turn_list_to_string(lis):
    char_string = ""
    for dic in lis:
        if dic["char"].isalpha():
            char_string += dic["char"] + ": " + str(dic["num"]) + "\n"
    return char_string

book = get_book()
wc = get_word_count(book)
cc = sorted_list(character_count(book))
lc = turn_list_to_string(cc)

print(f"============ BOOKBOT ============\n\
Analyzing book found at books/frankenstein.txt...\n\
----------- Word Count ----------\n\
{wc}\n\
--------- Character Count -------\n\
{lc}\
============= END ===============")
