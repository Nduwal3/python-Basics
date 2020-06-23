"""
Write a Python program to get a single string from two given strings, separated 
by a space and swap the first two characters of each string. 
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz' 
"""
#4. string concat
def stringConcat(string1 , string2):
    print('{}{}'.format(string2 , string1))

stringConcat('xyz','abc')