# Q: remove a given substring from the string
# logic: if the current value starts from the given substring or not
# same logic to skip a word or anything

# but after removing a substring if it can form the substring in the next 
# iteration with the help of char removing of the substring then this method
# won't work
# method1:

# def remove_char(str1,str2,ans):
#     if not str1:   # if 'str1' is empty
#         return ans
#     elif not  str1.startswith(str2):   # if not starts with given string
#         ans+= str1[0]           # add to the ans
#         return remove_char(str1[1:],str2,ans)  # now call the function again from next index
#         # print(ans)
#     else:  # if starts with the the given substring
#         n=len(str2)  #call fun by skipping this much len
#         return remove_char(str1[n:],str2,ans)  # in this case you have too call the function 
#                                                 # by skipping the len(substring) as since it has 
#                                             # matched so we have to remove 

# print(remove_char("asmGeeksasmasmForasmGeeks","asm","")) 


# other way of writing the same logic
def remove_char(str1,str2):
    ans= ""
    if len(str1)<len(str2):
        return str1
    if str1[:len(str2)]==str2:
        return remove_char(str1[len(str2):],str2)

    else:
        smallAns= remove_char(str1[1:],str2)
        ans+= str1[0] + smallAns
    return ans

print(remove_char("asmGeeksasmasmForasmGeeks","asm")) 