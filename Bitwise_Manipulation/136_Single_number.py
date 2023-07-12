#submitted on leetcode ,Time: o(n), space: o(n)
def singlenumber(nums):
    hashmap= {}
    for i in nums:
        if i not in hashmap:
            hashmap[i]= 1
        else:
            hashmap[i]+= 1
    for key,value in hashmap.items():
        if(value%2!=0):
            return key
            break
    # return 0   #if many elements occur odd times or no elements occur odd times(for gfg)
nums = [4,1,2,1,2]
print(singlenumber(nums))

# method 2:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

# 3rd method: best one using XOR operation
# Time: o(n), space: o(1)
# logic: xor with any number itself is zero and xor of any number with zero is the number itself.
# so when we will take xor of all ele, we will be left with the 'single number' 
# because all will be pair so they will get cancel('0') automatically.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans= 0
        for num in nums:
            ans^= num
        return ans
            
        