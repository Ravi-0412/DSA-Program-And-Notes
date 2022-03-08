# https://www.geeksforgeeks.org/python-string-methods/

# lower(): Converts all uppercase characters in a string into lowercase
# upper(): Converts all lowercase characters in a string into uppercase
# title(): Convert string to title case i.e convert first letter of each word capital

text= "hii my name is Ravi Raushan"
print(text.title())


# Function	    Description

# chr()	        Converts an integer to a character   # converts from ascii value to the character
# ord()	        Converts a character to an integer   # gives the ascii value of that character
# len()	        Returns the length of a string
# count()	    Returns the number of occurrences of a substring in the string.
# startswith()	Returns “True” if a string starts with the given prefix
# endswith()	Returns “True” if a string ends with the given suffix
# find()	    Returns the lowest index of the substring if it is found, else return '-1'
# index()	    Returns the position of the first occurrence of a substring in a string, else raises exception
# isalnum()	    Checks whether all the characters in a given string is alphanumeric or not
# isalpha()	    Returns “True” if all characters in the string are alphabets
# isdigit()	    Returns “True” if all characters in the string are digits
# islower()	    Checks if all characters in the string are lowercase
# isnumeric()	Returns “True” if all characters in the string are numeric characters
# isupper()	    Checks if all characters in the string are uppercase
# lower()	    Converts all uppercase characters in a string into lowercase
# replace()	    Replaces all occurrences of a substring with another substring

# count() Parameters
# count() method only requires a single parameter for execution.
#  However, it also has two optional parameters:
# substring - string whose count is to be found.
# start (Optional) - starting index within the string where search starts.
# end (Optional) - ending index within the string where search ends.

print(text.count('a'))   # exactly same as list
print(text.index('a'))
