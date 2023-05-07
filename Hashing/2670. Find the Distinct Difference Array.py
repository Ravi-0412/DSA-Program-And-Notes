# logic: calculate the freq of all ele and store into 'suffixDistinct'.

# now traverse the array, keep updating the 'suffixDistinct' and 'prefixDistinct'.
# keep decreasing the count of 'num' from suffixDistinct and if freq becomes= 0 then delete that num.
# keep incr the count of 'num' in 'prefixDistinct'.

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n= len(nums)
        suffixDistinct= Counter(nums)
        prefixDistinct= {}
        ans= [0]*n
        for i, num in enumerate(nums):
            prefixDistinct[num]= 1 + prefixDistinct.get(num, 0)
            suffixDistinct[num]-= 1
            if suffixDistinct[num]== 0:
                del suffixDistinct[num]
            diff= len(prefixDistinct) - len(suffixDistinct)
            ans[i]= diff
        return ans
    
