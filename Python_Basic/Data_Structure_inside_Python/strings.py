# mystring= "Hello"
# print(mystring[0])
# s1= "Hello"
# s2= "Satish"
# print(s1+" " +s2)
# print(s1*3)

s3= "Hello World"
# count=0
# for l in s3:
#     if l=='o':
#         count+= 1
# print(count, 'letters found')

# print('l' in s3)
# print('llo' in s3) 
# print('lloe' in s3)

# print(s3.upper())
# s3= "Hello World"
# print(s3.split())  # wiill produce a list with words of the given string

lst= ['one','two','three','four']
print(' '.join(lst))     # since we are putting space inside ' ' so it will 
                        # join all the words(remove the list) with space in single line 
print(''.join(lst))
# print(s3.find('lo'))  #gives index of start of string
# print(s3.replace('Hello',"good morning"))

# for splitting a string into letters, just typecast it to list
res= "ravi is a good boy"
print(list(res))
print(str(res))  # will join the whole as a one as a string. this only join the list 
                 # with ele inside ""  not any list
 

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

# str1= input("enter an string \n")
# if(str1!=str1[::-1]):
#     print("given string is not palindrome")
# else:
#     print("given string is palindrome")

# str1= input("enter an string \n")
# str1= str1.lower()
# revstr= reversed(str1)
# if list(str1)==list(revstr):
#     print("given string is palindrome")
# else:
#     print("given string is not palindrome")


# str1= "hello guys"
# words= str1.split()
# print(words)
# words.sort()
# print(words)
# for i in words:
#     print(i)











