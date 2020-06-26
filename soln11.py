"""
Write a Python program to count the occurrences of each word in a given 
sentence
"""

input_sentence = input('Enter a sentence:::  ')
words_in_sentence = input_sentence.split(' ')
word_count = {}
for word in words_in_sentence:  
    word = word.lower()  
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)