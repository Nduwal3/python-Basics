"""
Write a Python program to add 'ing' at the end of a given string (length should 
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the 
string length of the given string is less than 3, leave it unchanged. 
Sample String : 'abc' 
Expected Result : 'abcing' 
Sample String : 'string' 
Expected Result : 'stringly' 
"""
# 5 appending characters at end of string based on given string input
def customizeString(word):
    if len(word) >= 3:
        lettersToAppend = 'ing'
        if word[-3:] != lettersToAppend:
            print(word + '{}'.format(lettersToAppend))
        else:
            print(word + '{}'.format('ly'))
    else:
        print('word should contain atleast 3 characters')

customizeString('lying')