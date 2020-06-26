"""
 Write a Python program that accepts a comma separated sequence of words 
as input and prints the unique words in sorted form (alphanumerically). 
Sample Words : red, white, black, red, green, black 
Expected Result : black, green, red, white,red 
"""

comma_separated_list = input("Enter a sequence of words separated by comma::: ")
comma_separated_list =  comma_separated_list.replace(" ","") 
input_list = comma_separated_list.split(',')
input_list_to_set = set(input_list)
print(sorted(input_list_to_set))
