def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()
    if len(first_string) != len(second_string):
        return False
    else:
        for letter in first_string:
            if letter in second_string:
                second_string = second_string.replace(letter, "", 1)
            else:
                return False
        return True
