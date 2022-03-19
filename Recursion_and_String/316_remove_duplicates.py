# time: O(n^2), space: o(n)

def remove_duplicates(str1, ans):
    if len(str1)==0:
        return ''.join(sorted(ans))   # to print in sorted order
    if str1[0] not in ans:   # if not in the ans then just put in the ans
        ans+= str1[0]
    return remove_duplicates(str1[1:], ans)  # call the function for next index

# print(remove_duplicates("aaaabbbeeecdddd",""))


# iterative way to reduce the time complexity
# time: O(nlogn)

def remove(str1,ans):
    ans+= str1[0]
    for i in range(1,len(str1)-1):
        if str1[i]!=str1[i-1]:
            ans+= str1[i]
    return ans
str1= "aaaabbbeeecdddd"
print(remove(''.join(sorted(str1)), ""))


