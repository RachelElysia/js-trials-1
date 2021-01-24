"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)

def get_all_evens(nums):
    evenNums = []
    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)
    
    return evenNums


def get_odd_indices(items):
    result = []

    for i in range(len(items)):
        if i%2 ==0:
            result.append(items[i])

def print_as_numbered_list(items):
    for count, value in enumerate(items):
        print (count, value)

def get_range(start, stop):
    


def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
