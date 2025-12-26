from stats import get_word_count, character_count, sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_book():
    text = get_book_text("books/frankenstein.txt")
    return text

book = get_book()
wc = get_word_count(book)
cc = sorted_list(character_count(book))

print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\n{wc}\n--------- Character Count -------\n")