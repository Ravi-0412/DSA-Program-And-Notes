# Q: remove a given substring from the string
# logic: if the current value starts from the given substring or not
# same logic to skip a word or anything

# but after removing a substring if it can form the substring in the next 
# iteration with the help of char removing of the substring then this method
# won't work

def remove_char(str1,str2,ans):
    if not str1:   # if 'str1' is empty
        return ans
    elif not  str1.startswith(str2):   # if not starts with given string
        ans+= str1[0]           # add to the ans
        return remove_char(str1[1:],str2,ans)  # now call the function again from next index
        # print(ans)
    else:  # if starts with the the given substring
        n=len(str2)  #call fun by skipping this much len
        return remove_char(str1[n:],str2,ans)  # in this case you have too call the function 
                                                # by skipping the len(substring) as since it has 
                                            # matched so we have to remove 

str1= input("enter any string: ")
str2= input("enter the substring to remove: ")
ans= ""
print(remove_char(str1,str2,ans)) 