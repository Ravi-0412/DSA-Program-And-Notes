# logic: just similar as 'Find 1st negative number in subarray of size 'k'.
# Just we need to put value in that type of data structure in which we can get 'x'th smallest
# in O(1) or logn time and remove any ele in max logn .

# For this we need some type of data structure which store values in sorted order.
# sortedList add and remove ele from 'lst' in 'logn' time . n= no of ele in the list

# time= (n*logk)
# space= O(k)

from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n= len(nums)
        lst= SortedList()
        ans= []
        i, j= 0, 0
        while j < n:
            if nums[j] < 0:  # check if it is negative
                lst.add(nums[j])
            if j - i + 1 >= k:  # once we have subarray of size 'k'.
                if len(lst) < x: 
                    ans.append(0)
                else:
                    ans.append(lst[x-1])
                if nums[i] < 0:     # if "-ve" then decrease the count.
                    lst.remove(nums[i])  # remove the nums[i] from the 'lst'
                i+= 1
            j+= 1
        return ans


#Shorter version of above.
# for every subarray ans will be= xth smallest if <0 else 0.
# i.e ans= min(0, xth smallest).

# Time: Will be more than O(n *logk) because in this we are insertimg every ele.


from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n= len(nums)
        lst= SortedList()
        ans= []
        i, j= 0, 0
        while j < n:
            lst.add(nums[j])
            if j - i + 1 >= k:
                cur= min(0, lst[x-1])
                ans.append(cur)
                lst.remove(nums[i])
                i+= 1
            j+= 1
        return ans
    

# method 2: More better one
# No can lie between -50 <= 50.
# And we only need to care about "-ve" number.

# so we will keep storing the count of negative number in "freq" arr by taking its modulus.
# And when we will reach any window then for getting the kth smallest we will traverse from right to left in "freq" array.
# (opposite since more smaller will be on last)
# whenver we will see count >= x then means we got the ans for that array. so break

# else we will check for count < x and will add '0' to the ans.

# time: 50*n
# space= O(50)

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n= len(nums)
        freq= [0]*51  # store the freq of "-ve" numbers by taking modulus of that.
        ans= []
        i, j= 0, 0
        while j < n:
            if nums[j] < 0:
                freq[abs(nums[j])]+= 1
            if j- i+ 1 >= k:
                cnt= 0
                for num in range(50, 0,-1):
                    cnt+= freq[num]
                    if cnt >= x:
                        ans.append(-num)
                        break
                if cnt < x :
                    ans.append(0)
                if nums[i] < 0:
                    freq[abs(nums[i])]-= 1
                i+= 1
            
            j+= 1
        return ans