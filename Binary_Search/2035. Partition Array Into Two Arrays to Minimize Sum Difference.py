# intution is taken from the Q: "1755. closest subsequence sum"

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n= len(nums)//2   # for dividing the array into half.
        total= sum(nums)
        half= total//2   # ans will be minimum which will be closest to this. this will be our target.
        ans= abs(sum(nums[: n])- sum(nums[n: ]))

        # calculating  the possible sum of subsequences for first half and 2nd half and storing them into array.
        for k in range(1, n):
            left= [sum(comb) for comb in combinations(nums[: n], k)] # when we will choose any 'k' ele from given array then what will be combination.
            right= [sum(comb) for comb in combinations(nums[n: ], n-k)]   # agar first part se 'k' choose karte h then 2nd part se hmko 'n-k' choose karna hoga taki total chosen ele len ka half rahe.
            right.sort()
            for num in left:
                new_target= half - num
                i= bisect_left(right, new_target)
                if 0<= i < len(right):
                    left_ans_sum= num + right[i]
                    right_ans_sum= total- left_ans_sum
                    diff= abs(right_ans_sum - left_ans_sum)
                    ans= min(ans, diff)
        return ans
