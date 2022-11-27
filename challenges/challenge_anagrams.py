def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    if len(first_string) == 0:
        return False
    for char in first_string:
        if char not in second_string:
            return False
    return True
