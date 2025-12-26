from stats import get_word_count, character_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    get_word_count(text)
    character_count(text)

main()