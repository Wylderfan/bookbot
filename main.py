def sort_on(dict_item):
    return dict_item[1]
def main():
    char_dict = {
            "a": 0,"b": 0, "c": 0,"d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,"o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
            }
    char_list = []
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    for c in file_contents.lower():
        if c in char_dict:
            char_dict[c] += 1
    char_items = list(char_dict.items())
    char_items.sort(key=sort_on, reverse=True)
    for char, count in char_items:
        print(f"The '{char}' character was found {count} times")
main()
