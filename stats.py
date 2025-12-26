def get_word_count(text):
    words = text.split()
    number = len(words)
    print(f"Found {number} total words")

def character_count(text):
    char_num = {}
    lower = text.lower()
    for char in lower:
        if char not in char_num:
            char_num[char] = 1
        else:
            if char in char_num:
                char_num[char] += 1
    print(char_num)