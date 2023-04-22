# method 1:
# very easy and simple using "sortedList"
# Read about "sorteContainers here": 
# https://grantjenks.com/docs/sortedcontainers/sortedlist.html

# logic: SortedList store the ele in sorted order and after removing also it maintain the sorted order.
# time complexity of adding 'lst.add(num)' and removing "lst.remove()" is logn. n= no of ele in list.

# Note: may interviewer may not accept this and may ask for some other solution i. using heaps.
# time: O(n*logk)
from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans= []
        lst= SortedList()
        i, j= 0, 0
        while j < len(nums):
            lst.add(nums[j])
            if j - i + 1 >= k:
                if k & 1:
                    median= lst[k//2]
                    ans.append(median)
                else:
                    median= (lst[k//2 -1] + lst[k//2])/2
                    ans.append(median)

                lst.remove(nums[i])
                i+= 1
            j+= 1
        return ans
    

# method 2: using heaps
# Try later and understand properly.
# solutions in sheet.
