"""
Write a Python function to insert a string in the middle of a string. 
Sample function and result : 
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]] 
insert_sting_middle('{{}}', 'PHP') -> {{PHP}} 
"""

def insert_string_middle(original_string , string_to_be_inserted):
    index_to_be_inserted = int(len(original_string) / 2)
    string1= original_string[:index_to_be_inserted]
    string2 = original_string[index_to_be_inserted:]
    # print(string1)
    # print(string2)
    new_string = string1 + string_to_be_inserted + string2
    print(new_string)

insert_string_middle('[[]]','Python')
insert_string_middle('{{}}', 'PHP')
