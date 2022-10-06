# here that number can repeat any no of times
# time: O(n), space: O(1)
# logic: sb number ko pointer mano, like index 1 pe jo number h usko kahan point karna chahiye apne value ke anusar(kis index pe)
# diagram banao like: 'i' index pe kon sa number h say 'x' then 'x' should point to number sitting on index '1' , isi tarah se diagram banao
# finally ek linklist jaisa banega diagram or jo number repeat ho rha hoga wahan pe more than one pointer hoga(you will get that number directly)

# since only 'n' different number is kept as 'n+1' location then there must be atleast one no repeaetd and there must be a cycle 
# now this Q reduces to , find the starting node in a cyclic linklist that will be the ans

# for this , 1) first find the intersection point of slow and fast pointer 
# 2) now take one pointer from start say as 'slow2' and move 'slow' and 'slow2' one step ahead till they meet 
# 3) the node at which they will meet will be the starting node of the cycle

# Note: the distance of 'node at which cycle start' from start and from the node where 'slow' and 'fast' has intersected will be always same
# always keep in mind the above things

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find whether cycle exist or not , but here it will exist for sure
        # for this , find the intersection point of  slow and fast
        slow, fast= 0, 0  # we have to start with number from index '0' only
        while True:
            slow= nums[slow]
            fast= nums[nums[fast]]   # we have to incremenet fast two times so wrote like this
            if fast== slow:
                break
        # now find the starting node of the cycle
        slow1= 0
        while True:
            slow= nums[slow]
            slow2= nums[slow2]
            if slow== slow1:
                return slow


# https://leetcode.com/problems/find-the-duplicate-number/discuss/1892921/Java-9-Approaches-Count-%2B-Hash-%2B-Sort-%2B-Binary-Search-%2B-Bit-%2B-Fast-Slow-Pointers
# Try later with above link approaches