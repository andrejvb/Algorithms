def is_anagram(first_string, second_string):
    string1 = first_string.lower()
    string2 = second_string.lower()
    sorted_string1 = quicksort(string1)
    sorted_string2 = quicksort(string2)
    if len(sorted_string1) | len(sorted_string2) == 0:
        return (first_string, second_string, False)
    string1_return = ''.join(sorted_string1)
    string2_return = ''.join(sorted_string2)
    return (string1_return, string2_return, string1_return == string2_return)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


# arr = 'roma'
# sorted_arr = quicksort(arr)
print(is_anagram('amor', 'roma'))
