class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, n= [], len(nums)
        total_possible_subsets= 1 << n
        # write in binary form of all the possible subsets like for n= 3 ,write from 0 to 7
        # har possbile subset num(0 to 7 e.g) ke liye set bit find karo or
        # jis position pe set bit ho, us position wale ele ko ans me add kar do us possible subset num ke liye
        for i in range(total_possible_subsets):
            temp= []
            # check whether the bit is set or not at 'jth' position for each 'i'
            for j in range(n):
                # if set then add the num at that index to the 'temp'
                if i & (1 << j):
                    temp.append(nums[j])
            ans.append(temp)
        return ans
#

# a lot of approaches also there in recusrion topic for this Q