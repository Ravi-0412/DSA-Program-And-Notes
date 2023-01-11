# method 1: just sort and store ele in set then in list.
# time: O(n)= space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct_ele= sorted(list(set(nums)))
        print(distinct_ele)
        if len(nums)== 0: return 0
        ans= 1
        count= 1
        i= 0
        while (i +1) < len(distinct_ele):
            if distinct_ele[i+1]!= distinct_ele[i] + 1:
                # ans= max(ans, count)    # updating here will give the incorrect ans as when your ans lies at last
                #  then you will not able to update that.
                count= 1
            elif distinct_ele[i+1]== distinct_ele[i] + 1:
                count+= 1
                ans= max(count, ans)
            i+= 1
        return ans





