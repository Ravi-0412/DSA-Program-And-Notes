# Logic: First append 'k-1' element from start because 
# for finding ans for last element we will need 'k-1' element from start.
# Take two pointer 'i' and 'j'(i = 0, j= 0) and run a while loop(while j < len(nums) )
# and keep on incrementing 'j' and when you find any non-alternating sequence(nums[j] == nums[j -1]) then make i = j.
# At any time 'j -i +1' will give the length of subarray having 'alternating sequence'. 
# So check each time if 'j -i + 1 >= k' then increment ans by '1'.

# Note vvi: Follow up question.
# Q) If we were asked to find no of alternating subarray having size >= k 
# then instead of incrementing ans by '1' we will increase our ans by 'len(subarray) - (k - 1) i.e '(j - i + 1) - (k -1)'.
# Because 'j' can combine with this much subarray including previous ele and form a valid subarray.

# tIme = O(n)
# space = O(k) => for appending 'k' element.

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k - 1):
            colors.append(colors[i])
        n = len(colors)
        ans = 0
        i , j = 0, 1
        while j < n:
            if colors[j] == colors[j - 1]:
                i = j
            if j - i + 1 >= k:
                ans += 1
            j += 1
            
        return ans


# Later try to do in O(1) space.