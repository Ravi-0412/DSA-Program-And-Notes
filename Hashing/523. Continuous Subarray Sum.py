# method 1: 

# time: O(n*A), A= log(6^sum(arr))

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumTillIndex= collections.defaultdict(int)   # {sum: index}
        curSum= 0
        for i in range(len(nums)):
            curSum+= nums[i]
            if i >= 1: 
                if curSum % k== 0:
                    return True
                # Duplicate sum so in between sum must be zero. Here it also mean that there is consecutive zero since nums[i]>= 0 only.
                if curSum in sumTillIndex and i- sumTillIndex[curSum] >= 2:  # to handle the case when there is consective zero. [5,0,0,0]
                    return True                                              
                
                else:
                    j= 1
                while curSum - k*j >= 0:  # All number is positive so we can do like this
                    if (curSum - k*j) in sumTillIndex:  # means between these sum(subarray) is multiple of 'k'
                        if i- sumTillIndex[(curSum - k*j)] >= 2:
                            return True
                    j+= 1
            if curSum not in sumTillIndex:   # updating always will give wrong ans. [5,0,0,0,0,0]
                sumTillIndex[curSum]= i
        return False


# method 2: 
# very concise and better. just same logic only.
# logic: instead of storing sum, we are storing remainder. same meaning only.
# Do by this only. not above one

# Idea: if sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. 
# So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i. 
# Once some later sum(nums[:i']) % k == sum(nums[:i]) % k and i' - i > 1, we return True.

# Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n).
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumTillIndex= {0: -1}   # {modulo_sum: index} # we will get this 'modulus' till index 'i' when we will divide by 'k'.
                               # we may get modulus= 0 later so to handle that initially we are mapping {0:-1}
        curSum= 0
        for i in range(len(nums)):
            curSum+= nums[i]
            curSum= curSum % k
            if curSum in sumTillIndex:  # duplicate remainder
                pre= sumTillIndex[curSum]
                if i - pre >= 2:
                    return True
            else:
                sumTillIndex[curSum]= i 
        return False

# My mistakes in method 1:
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumTillIndex= collections.defaultdict(list)   # {sum: index}
        curSum= 0
        for i in range(len(nums)):
            if nums[i]== 0:
                return True
            curSum+= nums[i]
            if i >= 1: 
                if curSum % k== 0:
                    return True
                else:
                    j= 1
                while curSum - k*j >= 0:
                    if (curSum - k*j) in sumTillIndex:  
                        if i- sumTillIndex[(curSum - k*j)] >= 2:
                            return True
                    j+= 1

            sumTillIndex[curSum]= i
        return False


