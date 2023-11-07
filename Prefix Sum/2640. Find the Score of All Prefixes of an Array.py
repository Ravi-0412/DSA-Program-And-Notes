# time= space= O(n)

# Can do in single loop also.

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n= len(nums)
        maxi= nums[0]  # will store max_seen_till_now
        # making the conver array.
        conver= [0]*n
        for i in range(n):
            maxi = max(maxi, nums[i])
            conver[i]= nums[i] + maxi
        # finding the answer array , just score of array only.
        # ans= the prefix sum of arr 'conver'
        ans= [0]*n  # will store the score of array till index 'i' i.e arr[....i]
                    # in Q :" score of an array arr as the sum of the values of the conversion array of arr."
        ans[0]= conver[0]
        for i in range(1, n):
            ans[i]= conver[i] + ans[i-1]
        return ans

# concise version of above

from itertools import accumulate
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        maxTillNow, conver= 0, []  # min val of nums[i]= 1
        for n in nums:
            maxTillNow= max(maxTillNow, n)
            conver.append(n + maxTillNow)
        return accumulate(conver)  # convert the given array into prefix array, original array will be same only.
        # with print you will have to also specify the type like "print(list(accumulate(conver)))" otherwise will give object address.


# To study about accumulate:
# https://www.geeksforgeeks.org/python-itertools-accumulate/

# syntax: 
# itertools.accumulate(iterable[, func]) –> accumulate object

# If no function is passed, addition takes place by default. 
# If the input iterable is empty, the output iterable will also be empty.
