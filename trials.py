"""Python functions for JavaScript Trials 1."""

# DONE
def output_all_items(items):
    for item in items:
        print(item)

# DONE
def get_all_evens(nums):
    evenNums = []
    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)
    
    return evenNums

# DONE
def get_odd_indices(items):
    result = []

    for i in range(len(items)):
        if i % 2 == 0:
            result.append(items[i])

    return result

# DONE
def print_as_numbered_list(items):
    for count, value in enumerate(items):
        print (count, value)

# DONE
def get_range(start, stop):
    return range(start, stop)


def censor_vowels(word):
    chars = []

    for letter in word:
        if 'aeiou'

        chars.append(letter)
    return " ".join(chars)

def snake_to_camel(string):
    camel_case = []

    for word in string:
        camel_case.append(word.uppercase(0)+word.lowercase(1:))

    return " ".join(camel_case)

# DONE
def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest

# DONE
def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) -1]:
            result.append(char)

    return "".join(result)

# DONE
def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1

    return parens == 0


# DONE
def compress(string):
    compressed = []

    currChar = ''
    charCount = 0

    for char in string:

        if char != currChar:
            compressed.append(currChar)

            if (charCount > 1):
                compressed.append(str(charCount))
            
            currChar = charchar
            charCount = 0

        charCount +=1
    
    # Last letter
    compressed.append(currChar)
    if charCount > 1:
        compressed.append(str(charCount))
    
    return ''.join(compressed)
            