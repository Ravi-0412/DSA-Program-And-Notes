# Q is totally same as "jump game 1 " but changed the explanation to confuse.

# method 1: we can do by DP like jump game 1 but will go in O(n^2)

# applying greedy
# like how far we can go in one jump from curr index and after that how far we can go from all the ele in those jumps.
# just totally like multisource bfs we are applying.

# finding the range we can go by 1st jump and and next jump by taking ele of range that we got in first jump and so on.
# Being greedy about how far we can reach...
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, l, r= 0, 0, 0
        while r< len(nums)- 1:  # if it breaks when we have reached the last point
            farthest= 0  # will tell how far we have reached till now. aftewr for loop 'r' will be equal to farthest only.
            for i in range(l, r+1):  # taking the all elemnents in range and calculating how far we can reach with help of them.
                farthest= max(farthest, i+ nums[i])
            ans+= 1
            l,r= r +1, farthest   # 'l' will equal to 'r+1'
        return ans
