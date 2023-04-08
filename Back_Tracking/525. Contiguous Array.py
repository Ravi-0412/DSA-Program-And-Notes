# method 1 : Brute force
# for each subarray count no of zero and one.
# time: O(n^2)



# method 2: 
# using variable sliding window.

# time= space= O(n)
# Note: we can apply exactly same logic(even same code) in Q asking "longest substring/subarray having equal no of count of both when each ele can be of two type only".
# e.g: "Find the max length of substring having equal no of lowercase and uppercase letter" , "count  the no of substring having equal no of lowercase and uppercase letter" etc.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count= 0   #  if num== 0,  decr count by '1' by and if num== 1 incr count by '1'.
        maxLen= 0  # to handle the case when all num is either '0' or '1' only.   maxLen= float('-inf') will give '-inf' onlyin such case
        hashmap= {}   # [count: index]
        for i in range(len(nums)):
            if nums[i]== 0:
                count-= 1
            else:   #  nums[i]== 1
                count+= 1
            if count== 0:  # means we have found equal no of '0' and '1' till index 'i'.
                maxLen= i+ 1
            if count in hashmap:   # since we got duplicate of 'count'. so in between these two count must be '0' only then only we can get same count.
                maxLen= max(maxLen, i- hashmap[count])
            else:
                hashmap[count]= i
        return maxLen
