"""
Write a Python program to get a string from a given string where all 
occurrences of its first char have been changed to '$', except the first char itself. 
Sample String : 'restart' 
Expected Result : 'resta$t' 
"""
# 3. replace other occurence of 1st character with $
word = 'Sunshine'
word = word.lower()
firstLetter = word[0]
replaced_word = word.replace(firstLetter , '$' )
result = replaced_word.replace('$' , firstLetter  , 1)
print(result)