# 1st method: brute force(two nested loops)

# 2nd method: using dictionary 
# time: O(n), space: O(n)
# logic: for every ele, find the remaining sum then 
# check the remaining sum is present in the hashamp or not 
# if remaining sum is already present in the dictionary return its value 
# if not present then add the current ele into hashmap with its index
def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap= {}
        for i in range(len(nums)):
            rem_sum= target- nums[i]  # search for rem_sum in dictionary
            # searching will take O(1)
            if rem_sum in hashmap:  # if present then return the ans
                return hashmap[rem_sum], i  
            else:  # if not present then store the array val as key with index as values
                hashmap[nums[i]]= i   # since we have to return index so store index as value with remaining sum


