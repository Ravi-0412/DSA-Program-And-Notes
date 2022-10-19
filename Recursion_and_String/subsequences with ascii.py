# for every char there will be there possibilty
# so total subset= 3^n (n= no of characters
# 
def subset(str1,ans):
    if not str1:  # if empty then that will be one of the subset and that will be in 'ans'
        print(ans)
        return
    subset(str1[1:], ans + str1[0])  # when you include the current character
    subset(str1[1:], ans)   # when you don't include the current character
    subset(str1[1:],ans + str(ord(str1[0])))   # include the ascii value of the character

str1= input("enter any string: ")
ans= ""
print("all the subsets of given string with ascii value are: ") 
# subset(str1,ans)
# subset("abc",ans)


# for returning all into a list
def subset1(str1,ans):
    if not str1:  # if empty then that will be one of the subset and that will be in 'ans'
        local=[ans]
        return local
    first= subset1(str1[1:], ans + str1[0])  # when you include the current character
    second= subset1(str1[1:], ans)   # when you don't include the current character
    third= subset1(str1[1:],ans + str(ord(str1[0])))   # include the ascii value of the character
    return first + second + third
str1= input("enter any string: ")
ans= ""
print("all the subsets of given string with ascii value are: ") 
print(subset1(str1,ans))
