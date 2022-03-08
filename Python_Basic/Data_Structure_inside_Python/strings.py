# mystring= "Hello"
# print(mystring[0])
# s1= "Hello"
# s2= "Satish"
# print(s1+" " +s2)  # will add the given string with char under the " "
# print(s1*3)       # will print the given string '3' times

s3= "Hello World"
# count=0
# for l in s3:        # same as we traverse with num in the list
#     if l=='o':
#         count+= 1
# print(count, 'letters found')

# print('l' in s3)     # will return true if 'l' is presnt in the string otherwise false
# print('llo' in s3)   # true if 'llo' present otherwise false
# print('lloe' in s3)

# print(s3.upper())   # will convert whole char in the string into upper case
# s3= "Hello World"
# print(s3.split())  # wiill produce a list with words of the given string

lst= ['one','two','three','four']
print(' '.join(lst))     # since we are putting space inside ' ' so it will 
                        # join all the words(remove the list) with space in single line 
print(''.join(lst))   
# print(s3.find('lo'))  #gives starting index of the substring
# print(s3.replace('Hello',"good morning"))   # will replace 'hello' with 'goood morning'

# for splitting a string into letters, just typecast it to list
res= "ravi is a good boy"
print(list(res))    # will make a list with all the char of the string


# check whether given string is palindrome or not

# str1= input("enter an string \n")
# l= len(str1)
# l1= int(l/2)
# flag=0
# for i in range(l1):
#     if(str1[i]!=str1[l-i-1]):
#         print("given string is not palindrome")
#         flag=1
#         break;
# if(flag==0):
#     print("given string is palindrome")


# concise way of checking the palindrome
# just check the given string with its reverse

# str1= input("enter an string \n")
# if(str1!=str1[::-1]):
#     print("given string is not palindrome")
# else:
#     print("given string is palindrome")


# str1= input("enter an string \n")
# str1= str1.lower()
# revstr= reversed(str1)     # will return the object only. to get the ele by 
                            # this method you hve to typecast to any data structure in python 
# if list(str1)==list(revstr):
#     print("given string is palindrome")
# else:
#     print("given string is not palindrome")


# str1= "hello guys"
# words= str1.split()   # will make an array of the words of the string
# print(words)
# words.sort()
# print(words)
# for i in words:   # just like we traverse the array since 'words' is a list only
#     print(i)











