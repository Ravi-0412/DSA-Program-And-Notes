# # Note: Whenever you are asked to 'find distinct ele in a range' 
# Also think of hashmap i.e [num: frequency]
# vvi: At any point of time, len(hashmap) will give 'no of distinct ele' because hashmap doesn't store duplicates.

# Method 1:
# Calculate the prefixDistinct(traverse from left to right) and suffixDistinct(traverse from right to left) 
# separately and store into hashmap.

# Then again traverse array and calculate the ans.

# In this we need to travserse three times.

# Time = space = O(n)

# Method 2: In one travsersal

# logic: calculate the freq of all ele and store into 'suffixDistinct'.

# now traverse the array, keep updating the 'suffixDistinct' and 'prefixDistinct'.
# keep decreasing the count of 'num' from suffixDistinct and if freq becomes= 0 then delete that num.
# keep incr the count of 'num' in 'prefixDistinct'.

# Time = space = O(n)

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n= len(nums)
        suffixDistinct= Counter(nums)  # will give no of distinct ele in [i....n - 1]
        prefixDistinct= {}            # will give no of distinct ele in [0....i]
        ans= [0]*n
        for i, num in enumerate(nums):
            prefixDistinct[num]= 1 + prefixDistinct.get(num, 0)
            suffixDistinct[num]-= 1
            if suffixDistinct[num]== 0:
                del suffixDistinct[num]
            diff= len(prefixDistinct) - len(suffixDistinct)
            ans[i]= diff
        return ans
    
