"""Python functions for JavaScript Trials 1."""

# DONE
def output_all_items(items):
    """
    >>> output_all_items(['a', 25, '45', None])
    a
    25
    45
    None
    """

    for item in items:
        print(item)

# DONE
def get_all_evens(nums):
    """
    >>> get_all_evens([7, 8, 10, 1, 2, 2])
    [8, 10, 2, 2]
    """

    evenNums = []
    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)
    
    return evenNums

# DONE
def get_odd_indices(items):
    """
    >>> get_odd_indices([1, 'hello', True, 500])
    [1, True]
    """

    result = []

    for i in range(len(items)):
        if i % 2 == 0:
            result.append(items[i])

    return result

# DONE
def print_as_numbered_list(items):
    """
    >>> print_as_numbered_list([1, 'hello', True])
    0 1
    1 hello
    2 True
    """

    for count, value in enumerate(items):
        print (count, value)

# DONE
def get_range(start, stop):
    """
    >>> get_range(2, 8)
    [2, 3, 4, 5, 6, 7]
    """

    nums = []
    for num in range(start, stop):
       nums.append(num)

    return nums


def censor_vowels(word):
    """
    >>> censor_vowels('chocolate')
    'ch*c*l*t*'
    """

    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)

    return ''.join(chars)

# DONE
def snake_to_camel(string):
    """
    >>> snake_to_camel('what_is_up')
    'WhatIsUp'
    """

    camel_case = []

    for word in string.split('_'):
        camel_case.append(word[0].upper() + word[1:].lower())

    return ''.join(camel_case)



# DONE
def longest_word_length(words):
    """
    >>> longest_word_length(['what', 'is', 'the', 'longest', 'word', 'length'])
    7
    """
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest

# DONE
def truncate(string):
    """
    >>> truncate('aaaabbbbcccca')
    'abca'
    >>> truncate('hi***!!!! wooow')
    'hi*! wow'
    """
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) -1]:
            result.append(char)

    return "".join(result)

# DONE
def has_balanced_parens(string):
    """
    >>> has_balanced_parens('((This) (is) (good))')
    True
    >>> has_balanced_parens('(Oh no!)(')
    False
    """

    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        if char == ')':
            parens -= 1

    return parens == 0


# DONE
def compress(string):
    """
    >>> compress('aabbaabb')
    'a2b2a2b2'
    >>> compress('gooooodjjjoob')
    'go5dj3o2b'
    """
    compressed = []

    currChar = ''
    charCount = 0

    for char in string:

        if char != currChar:
            compressed.append(currChar)

            if (charCount > 1):
                compressed.append(str(charCount))
            
            currChar = char
            charCount = 0

        charCount +=1
    
    # Last letter
    compressed.append(currChar)
    if charCount > 1:
        compressed.append(str(charCount))
    
    return ''.join(compressed)
            