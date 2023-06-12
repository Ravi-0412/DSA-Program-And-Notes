#just swap the ele starting from 0 with last corresponding ele before mid
# submitted on leetcode
# input in form of an array string 
# same logic for string 
#time- O(n) ,Space- O(1)

class Solution:
    def reverseString(self, s: list[str]) -> None:
        # mid= len(s)//2
        # n= len(s)
        # for i in range(mid):  # reverse till mid
        #     s[i],s[n-i-1]= s[n-i-1], s[i]

        # return s[::-1]  # or one line ans

        #another method by recursion
        #time- O(n^2) ,Space- O(n)

# another method
# just the conversion of 1st iterative method
#time- O(n) ,Space- O(1)
def reverse(arr,start,end):
    if start== end:
        # means reversing is complete
        return arr
    arr[start], arr[end]= arr[end], arr[start]
    return reverse(arr,start+1,end-1)

# arr= ["h","e","l","l","o"]
# print(reverse(arr,0,len(arr)-1))


# reversing a string
def StringReverse(str1):
        ans= ""
        if len(str1)==1:
            return str1[0]
        smallAns= StringReverse(str1[1:])
        ans+= smallAns + str1[0]
        return ans

print(StringReverse("hello"))
print(StringReverse("raushn"))


# other way , pyhton new concept
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:]= s[::-1]
# s[:] = s[::-1] is required NOT s = s[::-1] because you have to edit the list inplace.  # 2nd case will print the same string
# s[:] = is editing the actual memory bytes s points to,    and s = points the variable name s to other bytes in the memory.