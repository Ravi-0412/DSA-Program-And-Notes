# to avoid duplicates , to bring all the duplicates together so that we can easily check for duplicates
# and best way to bring same ele together is just sort the array.
# and for every ele apply two sum if its not duplicate. and since sorted so we can use two pointer approach for Two sum.

# note: in case if we find any ans then before incr start or end  pointer ,we will check for duplicates 
# for any one of them because if we simply incr both then it can lead to duplicate ans.
# No need to check in unequal case.

# Also in outer loop, we will only apply "two sum" for cur number if it is distinct only.



# time: O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, n= [],len(nums)
        for i in range(n-2):
            if i>0 and nums[i]== nums[i-1]:   # simply skip so that no duplicate come in the ans
                continue
            start, end= i+1, n-1
            while start< end:
                threeSum= nums[i] + nums[start] + nums[end]
                if threeSum>0:
                    end-= 1
                elif threeSum <0:
                    start+= 1
                else:  # means we have found one of the ans.
                    ans.append([nums[i],nums[start], nums[end]])
                    # in this case there can be duplicates after 'start' pointer and before right pointer, 
                    # which may lead to duplicate if they form total= 0
                    # so either incr 'start' to new ele or decr 'end' to new element. No need to move both otherwise we may miss some answers.
                    start+= 1
                    # checking for duplicates
                    while start < end and nums[start]== nums[start-1]:
                        start+= 1
        return ans



