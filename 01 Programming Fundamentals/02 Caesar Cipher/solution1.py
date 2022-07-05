def caesar_cipher(string, offset):
    new_string = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for key, char in enumerate(string):
        for key2, char2 in enumerate(alphabet):
            if char == char2:
                position = key2 - offset
                new_string.append(alphabet[position])
    return "".join(new_string) 

