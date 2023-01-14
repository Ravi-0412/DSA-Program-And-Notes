class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2= 0, 0
        condidate1, condidate2= None, None
        for n in nums:
            if n== condidate1:
                count1+= 1
            elif n== condidate2:
                count2+= 1
            elif count1== 0:
                condidate1, count1= n, 1
            elif count2== 0:
                condidate2, count2= n, 1
            else:  # third condidate came other than one and two.
                # so will minimise the vote of both.
                count1, count2= count1 -1, count2 -1
        print(condidate1, condidate2)
        # if condidate1== condidate2 and condidate1!= -1:
        #     return [condidate1]
        # ans= []
        # if nums.count(condidate1) > len(nums)//3:
        #     ans.append(condidate1)
        # if nums.count(condidate2) > len(nums)//3:
        #     ans.append(condidate2)

        return [n for n in (condidate1, condidate2) if nums.count(n) > len(nums) // 3]
        return ans
