# for every char there will be there possibilty. 
# Possible subsequences of the string generated by including either the characters or the ASCII value of the characters. 
# 1) either include the char itself  2) either include the ascii value if char  3) or neither include char nor ascii value.
# so total subset= 3^n (n= no of characters)
# 
def subset(str1,ans):
    if not str1:  # if empty then that will be one of the subset and that will be in 'ans'
        print(ans)
        return
    subset(str1[1:], ans + str1[0])  # when you include the current character
    subset(str1[1:], ans)   # when you don't include the current character neither the ascii value
    subset(str1[1:],ans + str(ord(str1[0])))   # include the ascii value of the character

# str1= input("enter any string: ")
# ans= ""
# print("all the subsets of given string with ascii value are: ") 
# subset(str1,ans)
# subset("abc",ans)


# for returning all into a list
def subset1(str1,ans):
    if not str1:  # if empty then that will be one of the subset and that will be in 'ans'
        return [ans]
    first= subset1(str1[1:], ans + str1[0])  # when you include the current character
    second= subset1(str1[1:], ans)   # when you don't include the current character
    third= subset1(str1[1:],ans + str(ord(str1[0])))   # include the ascii value of the character
    return first + second + third
# str1= input("enter any string: ")
# ans= ""
# print("all the subsets of given string with ascii value are: ") 
# print(subset1(str1,ans))

# more concise way of above
def subset2(str1,ans):
    if not str1:  # if empty then that will be one of the subset and that will be in 'ans'
        return [ans]
    res= []
    res+= subset2(str1[1:], ans + str1[0])  # when you include the current character
    res+= subset2(str1[1:], ans)   # when you don't include the current character
    res+= subset2(str1[1:],ans + str(ord(str1[0])))   # include the ascii value of the character
    return res
str1= input("enter any string: ")
ans= ""
print("all the subsets of given string with ascii value are: ") 
print(subset2(str1,ans))