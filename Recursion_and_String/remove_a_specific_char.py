
# def remove_char(str1,ch,ans):
#     if not str1:   # if 'str1' is empty
#         return ans
#     if str1[0]!=ch:     # if deosn't match
#         ans+= str1[0]   # add to the ans
#     return remove_char(str1[1:],ch,ans)  # now call the function again from next index

# method 2:
def remove_char(str,ch):
    ans= ""
    if not str:
        return ""
    if str[0]!= ch:  # hmko 'ch' nhi mila isliye add kar diye bhai
        ans+= str[0]
    return ans+ remove_char(str[1:],ch)   # baki tmko agar nhi mile to add karke hmko send kar dena


str1= input("enter any string: ")
ch= input("enter the char to remove: ")
ans= ""
print(remove_char(str1,ch))

    