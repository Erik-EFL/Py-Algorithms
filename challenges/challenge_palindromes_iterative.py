def is_palindrome_iterative(word):
    if word == "" or len(word) == 0:
        return False

    low_index = len(word) // 2

    for i in range(low_index):
        if word[i] != word[-i - 1]:
            return False

    return True
