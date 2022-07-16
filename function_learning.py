# General Function Definition from line 3 to line 10 . Not to run.

# def a_descriptive_name(optional arguments):
# """A documentation string"""
#
# # Your function's code goes here
# # Your function's code goes here
# # Your function's code goes here
#
# return optional_value





# Definition of function
# def search_for_vowels():
#     vowels = set('aeiou')
#     input_sentence = input('Enter a sentence')
#     input_sentence_set = set(input_sentence)
#     print(vowels.intersection(input_sentence_set))

# def search_for_vowels(sentence):
#     vowels=set('aeiou')
#     return vowels.intersection(set(sentence))

def search_for_letters(sentence: str, letters: str='aeiou') -> set:
    """ Searches for user-given letters in a given sentence"""
    return set(letters).intersection(set(sentence))


input_phrase = input("Please Enter a sentence ")
input_letters = input("Please enter the letters you wish to search for ")

# print(search_for_letters(input_phrase, input_letters))

print(search_for_letters(input_phrase))
