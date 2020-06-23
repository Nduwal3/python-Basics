"""
Write a Python function that takes a list of words and returns the length of the 
longest one. 
"""
# 7 return longest word from list
list_of_words = (input('enter list of words separated with space')).split(' ')
# ['Hi', "Hello", "Namaste", "hola"]
char_count = 0
longest_word = ''
for item in list_of_words:
    if len(item) > char_count:
        char_count = len(item)
        longest_word = item
print(longest_word)