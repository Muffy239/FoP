import re

# 1. Write a function that uses a regex expression to return the boolean True if the string that is passed in contains only upper and lowercase letters, numbers, and underscores.
# Exmaples:
# Input: 'The quick brown fox jumps over the lazy dog.'
# Output: False
# Input: 'Python_Exercise_1'
# Output: True


#! 1 COMPLETE
# sentence = "Python_Exercise_1"

# def regexOne(givenString):
    
#     pattern = r'[a-zA-Z0-9_]+'
#     return bool(re.fullmatch(pattern, givenString))

# print(regexOne(sentence))


# 2. Write a function that uses a regex expression to return the boolean True if the string that is passed in starts with the number 5.
# Exmaple:
# Input: '6-563345'
# Output: False
# Input: '5-762145'
# Output: True


#! 2 COMPLETE
# sentence = '5-762145'

# def regexOne(sentence):
    
#     pattern = r'^5'
    
#     return bool(re.search(pattern, sentence))

# print(regexOne(sentence))


# 3. Write a function that uses a regex expression to return the boolean True if the string that is passed in has a number at the end.
# Exmaple:
# Input: 'abcdef'
# Output: False
# Input: 'abcdef7'
# Output: True

#! 3 COMPLETE
# sentence = 'abcdef'

# def regexFinder(sentence):
    
    
#     pattern =r'[0-9$]'
    
#     return bool(re.search(pattern,sentence))

# print(regexFinder(sentence))


# 4. Write a function that uses a regex expression to return a list of all the instances of dog or dogs.
# Exmaple:
# Input: 'Hey dog, how are you dog, where are all the dogs? Man these dogs are lost dog on it.'
# Output: ['dog', 'dog', 'dogs', 'dogs', 'dog']


# #! 4 COMPLETE
# sentence = 'Hey dog, how are you dog, where are all the dogs? Man these dogs are lost dog on it.'

# def regexFinder(sentence):
    
    
#     pattern = r'(dog[s]?)'
    
#     return  re.findall(pattern,sentence)
    
# print(regexFinder(sentence))


# 5. Write a function that uses a regex expression to return a list that only includes the numbers.
# Exmaple:
# Input: 'Ten 10, Twenty 20, Thirty 30'
# Output: ['10', '20', '30']

#! 5 COMPLETE
# sentence = 'Ten 10, Twenty 20, Thirty 30'

# def regexFinder(sentence):
    
#     pattern =r'[0-9]+'
    
#     return re.findall(pattern, sentence)

# print(regexFinder(sentence))

# 6. Write a function that uses a regex expression to return a list with all the words that start with 'a' or 'e'.
# Exmaple:
# Input: 'The following example creates an array list with 50 elements.'
# Output: ['example', 'an', 'array', 'elements']


#! 6 COMPLETE

# sentence = 'The following example creates an array list with 50 elements.'

# def regexFinder(sentence):
    
#     pattern =r'\b[ea]\w*'
    
#     return re.findall(pattern, sentence)

# print(regexFinder(sentence))




# 7. Write a function that uses a regex expression to abbreviate 'Road' as 'Rd.' in a given string.
# Exmaple:
# Input: '21 Rainbow Road'
# Output: '21 Rainbow Rd.'

#! 7 COMPLETE

# sentence = '21 Rainbow Road'

# def regexFinder(sentence):
    
#     pattern = r'\bRoad'
    
#     return re.sub(pattern, 'Rd.', sentence)

# print(regexFinder(sentence))


# 8. Write a function that uses a regex expression to replace all occurrences of space, comma, or period with a colon.
# Exmaple:
# Input: 'Python Exercises, PHP exercises.'
# Output: 'Python:Exercises::PHP:exercises:'



# 9. Write a function that uses a regex expression to return a list of all words in a string that are exactly five characters long.
# Exmaple:
# Input: 'The quick brown fox jumps over the lazy dog.'
# Output: ['quick', 'brown', 'jumps']

#! 8 COMPLETE

# sentence = 'The quick brown fox jumps over the lazy dog.'

# def regexFinder(sentence):
    
#     pattern = r'\b\w{5}\b'
    
#     return re.findall(pattern, sentence)

# print(regexFinder(sentence))


# 10. Write a function that uses a regex expression to return a string that has all extra spaces removed. One space between words should be kept, but any extra spaces should be removed.
# Exmaple:
# Input: 'Python      Exercises'
# Output: 'Python Exercises'



# 11. Write a function that uses a regex expression to return a string with all non-alphanumeric characters removed.
# Exmaple:
# Input: '**//Python Exercises// - 12. '
# Output: 'PythonExercises12'



# 12. Write a function that uses a regex expression to return a list of words that was split by capital letters.
# Exmaple:
# Input: 'PythonTutorialAndExercises'
# Output: ['Python', 'Tutorial', 'And', 'Exercises']



# 13. Write a function that uses a regex expression to return the following string replacement that is case-insensitive.
# Exmaple:
# Input: 'Hello HOTDOG, how are you? Do you even like hotdogs?'
# Output: 'Hello CUPCAKE, how are you? Do you even like cupcakes?'



# 14. Write a function that uses a regex expression to return a string that has all words that are between 1 and 3 characters removed.
# Exmaple:
# Input: 'The quick brown fox jumps over the lazy dog.'
# Output: 'quick brown jumps over lazy.'



# 15. Write a function that uses a regex expression to return a list of strings who's parenthesis section has been removed.
# Exmaple:
# Input: ['example (.com)', 'w3resource', 'github (.com)', 'stackoverflow (.com)']
# Output: ['example', 'w3resource', 'github', 'stackoverflow']



# 16. Write a function that uses a regex expression to return a string with all the lowercase letters removed.
# Exmaple:
# Input: 'KDeoALOklOOHserfLoAJSIskdsf'
# Output: 'KDALOOOHLAJSI'



# 17. Write a function that uses a regex expression to return the boolean True if the string passed in has an 'a' followed by two or three 'b's. Otherwise return False.
# Exmaple:
# Input: 'ab'
# Output: False
# Input: 'aabbbbbc'
# Output: True



# 18. Write a function that uses a regex expression to return the boolean True if the string passed in has lowercase letters joined with a underscore. Otherwise return False.
# Exmaple:
# Input: 'aab_Abbbc'
# Output: False
# Input: 'aab_cbbbc'
# Output: True



# 19. Write a function that uses a regex expression to return the boolean True if the string passed in has one uppercase letter followed by lowercase letters. Otherwise return False.
# Exmaple:
# Input: 'PYTHON'
# Output: False
# Input: 'AaBbGg'
# Output: True



# 20. Write a function that uses a regex expression to return the boolean True if the string passed in has proper punctuation. Otherwise return False.
# Exmaple:
# Input: 'The quick brown fox jumps over the lazy dog'
# Output: False
# Input: 'The quick brown fox jumps over the lazy dog.' (proper punctuation can be more than just a period...)
# Output: True
