# time: O(n*logn)

# Note: Here we are not checking the initial guess 'smallest' and 'largest' 
# We are checking if we can get our ans even smaller by by decr the current ele by  'k' and incr the pre(i-1) ele by 'k' .
# just opposite of our assumption as we those things are possible.

# vvi: Here asuming if we can get minimum value by subtracting 'k' from 'i'th ele. 
# so we will update our max by adding 'k' to the previous value as we have to keep minimum and maximum as close as possible to minimise our ans.
# that why we are updating our minimum and maximum by comapring with smallest and largest always.

# Note: totally same as "Minimize the Heights I & 2" on gfg.

# Note: Analyse this proeprly and later do it in O(n) . solution in sheet.
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n= len(nums)
        ans= nums[n-1] - nums[0]  # our ans can't go beyond this. we can also take, ans= float('inf')
                                # will also handle the case when there will be only one ele
        # Assuming we will get smallest and largest by doing '+k' from 1st ele and by '-k' from last ele. Assuming minimum height we can get by doing this.
        smallest= nums[0] + k 
        largest=  nums[n-1] - k
        # But the 'largest' can be <= 'smallest' after operation. so we can get our ans from middle towers also. e.g:[3,5] and k= 4
        
        # checking if middle towers can be our ans. Finding new condidate for ans if possible.
        for i in range(1, n):
            minimum= min(smallest, nums[i] -k)  # we can get smallest from bigger number also after operation.
                                                # Here the current num is geeting decresed by 'k' and in next iteration it will get increased by 'k' 
                                                # in this way we are checking both the possibility for each index.
            maximum=  max(largest, nums[i-1] + k) # we can get largest from smaller number also after operation.
            ans=      min(ans, maximum- minimum)
        return ans


# Here assuming arr[ind] is the maximum value.
# so for minimum we have to subtract 'k' from next ele to keep the value close.
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n= len(nums)
        ans= nums[n-1] - nums[0]  
        # checking if middle towers can be our ans. Finding new condidate for ans if possible.
        for i in range(n-1):
            smallest= min(nums[0] + k, nums[i + 1] -k)  # we can get smallest from bigger number also after operation.
            largest=  max(nums[n-1] -k, nums[i] + k) # we can get largest from smaller number also after operation.
            ans=      min(ans, largest- smallest)
        return ans



# for Q : "Minimize the Heights II". gfg
# here height of tower can't be negative.
# https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        ans= arr[n-1] - arr[0]  # our ans can't go beyond this. we can also take, ans= float('inf')
                                # will also handle the case when there will be only one ele
        # Assuming we will get smallest and largest by doing '+k' from 1st ele and by '-k' from last ele.
        smallest= arr[0] + k 
        largest=  arr[n-1] - k
        # But the 'largest' can be <= 'smallest' after operation. so we can get our ans from middle towers also. e.g:[3,5] and k= 4
        
        # checking if middle towers can be our ans. Finding new condidate for ans if possible.
        for i in range(1, n):
            if arr[i] < k:  # skip because height of tower can't be negative
                continue
            minimum= min(smallest, arr[i] -k)  # we can get smallest from bigger number also after operation.
            maximum=  max(largest, arr[i-1] + k) # we can get largest from smaller number also after operation.
            ans=      min(ans, maximum- minimum)
        return ans

# my mistake
# here we are changing the smallest and largest.

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        ans= arr[n-1] - arr[0]  # our ans can't go beyond this. we can also take, ans= float('inf')
                                # will also handle the case when there will be only one ele
        # Assuming we will get smallest and largest by doing '+k' from 1st ele and by '-k' from last ele.
        smallest= arr[0] + k 
        largest=  arr[n-1] - k
        print(arr, smallest, largest)
        # But the 'largest' can be <= 'smallest' after operation. so we can get our ans from middle towers also. e.g:[3,5] and k= 4
        
        # checking if middle towers can be our ans. Finding new condidate for ans if possible.
        for i in range(1, n):
            smallest= min(smallest, arr[i] -k)  # we can get smallest from bigger number also after operation.
            largest=  max(largest, arr[i-1] + k) # we can get largest from smaller number also after operation.
            ans=      min(ans, largest- smallest)
        return ans