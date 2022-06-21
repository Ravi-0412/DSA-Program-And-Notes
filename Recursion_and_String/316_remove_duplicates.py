# time: O(n^2), space: o(n)

def remove_duplicates(str1, ans):
    if len(str1)==0:
        # return ''.join(sorted(ans))   # to print in sorted order
        return ans
    if str1[0] not in ans:   # if not in the ans then just put in the ans
        ans+= str1[0]
    return remove_duplicates(str1[1:], ans)  # call the function for next index

print(remove_duplicates("aaaabbbeeecdddd",""))


# submitted on gfg 
# same order but in lexographical order
def removeDups(self, S):
    ans= ""
    for i in range(len(S)):
        if S[i] not in ans:
            ans+= S[i]
    return ans


# iterative way to reduce the time complexity
# time: O(nlogn)
# this will just remove the duplicates but order will not the same
def remove(str1,ans):
    ans+= str1[0]
    for i in range(1,len(str1)-1):
        if str1[i]!=str1[i-1]:
            ans+= str1[i]
    return ans
str1= "aaaabbbeeecdddd"
# print(remove(''.join(sorted(str1)), ""))
# print(''.join(sorted(str1)))


# submitted on Leetcode
def removeDuplicateLetters(self, s: str) -> str:
    LastIndex= [0]*26  # will store the last index occurences of the char
    # LastIndex will tell whether to delete that char from ans or not
    for i in range(len(s)):
        LastIndex[ord(s[i]) - ord('a')]= i    # for 'a' index= 0, for 'b' index= 1 and so on
    stack= []
    for i in range(len(s)):
        curr= ord(s[i]) - ord('a')  # will help in checking the last index
        if s[i] in stack:  # if curr char is already in stack then skip and do nothing
            continue
        # otherwise check if stack_top > curr_char and if it is then check whether they are occuring again after curr_char or not
        # repeat this till stack become empty 
        # if stack_top is occuring again after curr_char then we can pop the stack_top and consider its final occurences
        while stack and ord(stack[-1]) > ord(s[i]) and LastIndex[ord(stack[-1]) - ord('a')] > i:
            stack.pop()
        stack.append(s[i])
    # now stack will contain the ans but we have to return in form of string'
    # so store in form of string and return, that will be the final ans
    ans= ""
    for i in range(len(stack)):
        ans+= stack[i]
    return ans


