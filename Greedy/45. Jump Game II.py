# Q is totally same as "jump game 1 " but changed the explanation to confuse.
# Here we have to find the minimum no of jumps required to go to last index.
# method 1: we can do by DP like jump game 1 but will go in O(n^2)

# applying greedy
# logic: jahan tak abhi pahunche h wahan tak ke index ko use karke or kitna door pahunch sakte h and so on.
# Totally like we apply multisource bfs.
# note: jahan bhi min time, min distance, min jump nikalna ho bhut sara options ko consider karke 
# then multisource bfs should come into mind.
# e.g: Q like rotten oranges, burning tree etc..

# finding the range we can go by 1st jump and and next jump by taking ele of range that we got in first jump and so on.
# Being greedy about how far we can reach...
# just think this as multisource bfs.
# 'l', 'r' tell the range of curr level you are considering now. after considering each level you incr the 'ans' by '1'.

# easier and better one. Totally same as multiospurce bfs logic.
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, l, r= 0, 0, 0  
        while r < len(nums)- 1:  # if it breaks when we have reached the last point
            farthest= 0  # will tell how far we can reach using the index we have alraedy reached. after for loop 'r' will be equal to farthest only.
            for i in range(l, r+1):  # taking the all elemnents in range and calculating how far we can reach with help of them. Multisource bfs 
                farthest= max(farthest, i+ nums[i])
            ans+= 1
            l,r= r +1, farthest   # 'l' will equal to 'r+1' so avoid calculation till 'l' again since for till 'l' we have already calculated before.
        return ans
 

# method 2: good one
# same way we solved 'Jump Game'.
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps= 0   # will tell the min no jumps required. will tell only how many level we traversed to raech the last index.
        farthest= 0   # will tell how farthest index we have reached till now using all the node we have visited till current level
        lastJumpedPos= 0  # will tell the range of the next level. after reaching here only we can incr our 'jump' as we have already reached till here.
        for i in range(len(nums) -1):   # loop will go till 'n-1' only
            farthest= max(farthest, i + nums[i])
            if i== lastJumpedPos:   # means if we have considered all the ele at curr level.
                lastJumpedPos= farthest  # increasing the range i.e ele to be considered in next level.
                jumps+= 1
        return jumps

# we only need to run loop till 'n-2' because we will must reach 'n-1' in next level since it is given that there is at least one path possible.
# i.e considering all the level before we will must reach the last index.


# Similar Q:
# ) 1024. Video Stitching
# 2) 