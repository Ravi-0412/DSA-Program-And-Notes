# logic in notes
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        de= collections.deque()  # we have to remove from 1st while sliding the win
                                # and we have to append at last while poping all the smaller else:
                                # so we need two pointer to keep track at front as well as end
                                # so 'deque' is the best one to use here
        i,j,ans,n= 0,0,[],len(nums)
        while(j<n):
            while de and nums[j]> de[-1]:  # pop until you find any ele greater
                                           # or deque becomes empty
                de.pop()
            de.append(nums[j])   # after that append(you have to append always)
            if j-i+1< k:
                j+= 1
            elif j-i+1== k:
                ans.append(de[0])  # for that subarray first ele of 'deque' will give the ans
                if nums[i]==de[0]:  # before sliding the wind check whether the max ele is at the 'ith' index
                    de.popleft()    # here we have to pop from left since only leftmost was giving the ans
                i+= 1
                j+= 1
        return ans

        