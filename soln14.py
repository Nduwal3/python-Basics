"""
Write a Python function to create the HTML string with tags around the 
word(s). 
Sample function and result : 
add_tags('i', 'Python') -> '<i>Python</i>' 
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>' 
"""

def addTags(tag , stringInput):
    opening_tag = '<' + tag + '>'
    closing_tag = '</' + tag + '>'
    html_string = opening_tag + stringInput + closing_tag
    print(html_string)
addTags('i' , 'python')
addTags('b', 'Python Tutorial')
