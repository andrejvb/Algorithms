def is_palindrome_iterative(word):
    if len(word) <= 1:
        return True
    elif word == '':
        return False
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome_iterative(word[1:-1])


print(is_palindrome_iterative('agua'))
