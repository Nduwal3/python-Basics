"""
Write a Python program to find the first appearance of the substring 'not' and 
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' 
substring with 'good'. Return the resulting string. 
Sample String : 'The lyrics is not that poor!' 
'The lyrics is poor!' 
Expected Result : 'The lyrics is good!' 
'The lyrics is poor!' 
"""
# 6 replace occurence of 'not' followed by 'poor' with 'good'
def CustomizeSearchAndUpdate():
    input_string = input('Enter a sentence with not followed by poor ::: ')
    words_to_be_checked = ['not' , 'poor']
    words_list = list(input_string.split(' '))
    for word in words_to_be_checked:
        if word not in words_list:
            print("There is no word 'not' followed by 'poor'")
    else:
        if words_list.index('not') < words_list.index('poor'):
            words_to_be_replaced = words_list[words_list.index('not'):words_list.index('poor') + 1]
            words_to_be_replaced_String = (' ').join(words_to_be_replaced)        
            print(input_string.replace(words_to_be_replaced_String , 'good' ))
        else:
            print('not is not followed by poor')

CustomizeSearchAndUpdate()