"""
Write a Python program to count the number of characters (character 
frequency) in a string. Sample String : google.com' 
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} 
"""
# 1. Program to count characters of a word
def wordCount(word):
    wordListInLowerCase = (list(word.lower()))
    countDict = dict()
    for char in wordListInLowerCase:
        if char in  countDict:
            countDict[char] = countDict[char] + 1
        else:
            countDict[char] = 1
    print(countDict)

wordCount("summer")