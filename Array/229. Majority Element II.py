# Just little extension of Q :"169. Majority Element".
# Think in same way like 'majority ele'. (Last method).

# There can be maximum two ele in our ans.

# logic: Think in election, you have to find the two condidate who secured more than n//3 votes.
# so first find the two condidates who secured highest votes amon all.
# After that check if there vote count is > n//3.

# Note: Har ele ke pass '3 choice h either condidate1 ho, condidate2 ho ya different ele ho.

# Time: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2= 0, 0
        condidate1, condidate2= None, None
        for n in nums:
            if n== condidate1:
                # vote of condidate1 will increase
                count1+= 1
            elif n== condidate2:
                # vote of condidate2 will increase
                count2+= 1
                
            # agar na hi condidate1 h na hi condidate2 h then 
            # cur ele kuch bhi ho sakte h depending upon value of count1 and count2.
            elif count1== 0:
                # cur ele will become the 1st condidate(one of possible condidate)
                condidate1, count1= n, 1
            elif count2== 0:
                # cur ele will become the 2nd condidate(one of possible condidate)
                condidate2, count2= n, 1
            else:   # count1 > 0 and count 2> 0
                # third condidate came other than one and two.
                # so will minimise the vote of both.
                count1, count2= count1 -1, count2 -1
        # if condidate1== condidate2 and condidate1!= -1:
        #     return [condidate1]
        # ans= []
        # if nums.count(condidate1) > len(nums)//3:
        #     ans.append(condidate1)
        # if nums.count(condidate2) > len(nums)//3:
        #     ans.append(condidate2)
        # return ans

        return [n for n in (condidate1, condidate2) if nums.count(n) > len(nums) // 3]   # shortcut of above lines.
