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


# Note: whenever you have to find the subarray length or count of subarray with given sum 'k' or given xor 'k' . Apply two sum logic
# since "+" has complement "-" i.e given a sum say 'target' then say till any index 'j' totalSum= curSum 
# then if we can find any ele 'x' at index 'i' having such that x= curSum - target,  then we can get  the target by doing sum of all ele from index 'i+1' to 'j'.

# same way xor work because of its property : if res= a^b then res^a= b and res^b= a.
# replace res->curSum , b= target then if we will find 'a' such that a= res ^ b then means we can get the target 'b'.

