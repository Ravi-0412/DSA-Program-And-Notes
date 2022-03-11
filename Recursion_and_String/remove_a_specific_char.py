# Q: remove a given character from the string
def remove_char(str1,ch,ans):
    if not str1:   # if 'str1' is empty
        return ans
    if str1[0]!=ch:     # if deosn't match
        ans+= str1[0]   # add to the ans
    return remove_char(str1[1:],ch,ans)  # now call the function again from next index


str1= input("enter any string: ")
ch= input("enter the char to remove: ")
ans= ""
print(remove_char(str1,ch,ans))

    