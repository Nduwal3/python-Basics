"""
Write a Python program to remove the characters which have odd index 
values of a given string. 
"""

word = 'balance'
word_updated = word
for char in word:
    if word.index(char) % 2 != 0:
        word_updated = word_updated.replace(char , '')
print(word_updated)
