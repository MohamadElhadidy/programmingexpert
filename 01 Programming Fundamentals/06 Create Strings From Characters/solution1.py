def create_strings_from_characters(frequencies, string1, string2):
    not_string1, not_string2, together = True, True, True
    for char in string1:
        if char in frequencies:
            if string1.count(char) > frequencies[char]:
                not_string1 = False
            if char in string2:
                if string1.count(char) + string2.count(char) > frequencies[char]:
                    together = False
        else:
            not_string1, together = False, False

    for char in string2:
        if char in frequencies:
            if string2.count(char) > frequencies[char]:
                not_string2 = False
        else:
            not_string2 = False

    if(together):
        return 2
    elif(not_string1 or not_string2):
        return 1
    if(not(not_string1 and not_string2)):
        return 0
