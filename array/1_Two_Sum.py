# 1st method: brute force(two nested loops)

# 2nd method: 
# time: O(n)
def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap= {}
        for i in range(len(nums)):
            rem_sum= target- nums[i]  # search for rem_sum in dictionary
            if rem_sum in hashmap:  # if present then return the ans
                return hashmap[rem_sum], i
            else:  # if not present then store the array val as key with index as values
                hashmap[nums[i]]= i


