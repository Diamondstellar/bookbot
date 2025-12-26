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
    return char_num

def sorted_list(dictionary):
    def sort_on(x):
        return x["num"]
    ordered = []

    for char in dictionary:
        base = {"char": "a", "num": 0}
        base["char"] = char
        base["num"] = dictionary[char]
        ordered.append(base)
    ordered.sort(reverse=True, key=sort_on)
    return ordered
