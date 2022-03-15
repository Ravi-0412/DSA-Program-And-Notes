#just swap the ele starting from 0 with last corresponding ele before mid
# submitted on leetcode
# input in form of an array string 
# same logic for string 
#time- O(n) ,Space- O(1)

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # mid= len(s)//2
        # n= len(s)
        # for i in range(mid):
        #     s[i],s[n-i-1]= s[n-i-1], s[i]

        # return s[::-1]  # or one line ans

        #another method by recursion
        #time- O(n^2) ,Space- O(n)

        ans= []
        if len(s)==1:
            new_list= []
            new_list.append(s[-1])
            return new_list
        smallAns= Solution().reverseString(s[1:])
        ans+= smallAns
        ans.append(s[0])
        return ans


arr= ["h","e","l","l","o"]
l1= Solution()
# print(l1.reverseString(arr))


# another method
# just the conversion of 1st iterative method
#time- O(n) ,Space- O(1)
def reverse(arr,start,end):
    if start== end:
        return arr
    arr[start], arr[end]= arr[end], arr[start]
    start,end= start+1, end-1
    return reverse(arr,start,end)

arr= ["h","e","l","l","o"]
# print(reverse(arr,0,len(arr)-1))


# reversing a string
def StringReverse(str1):
        ans= ""
        if len(str1)==1:
            local_ans= ""
            local_ans+= str1[0]
            return local_ans
        smallAns= StringReverse(str1[1:])
        ans+= smallAns
        ans+= str1[0]
        return ans

print(StringReverse("hello"))
print(StringReverse("raushn"))
