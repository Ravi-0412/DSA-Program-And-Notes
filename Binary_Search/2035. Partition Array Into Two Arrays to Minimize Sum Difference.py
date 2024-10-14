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

# Without using inbuilt comb function and inbuilt binary search function
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        def generate_combinations(arr, k):
            # Helper function to generate combinations of k elements using backtracking
            res = []
            comb = []
            
            def backtrack(start):
                if len(comb) == k:
                    res.append(sum(comb))
                    return
                for i in range(start, len(arr)):
                    comb.append(arr[i])
                    backtrack(i + 1)
                    comb.pop()
            
            backtrack(0)
            return res

        def binary_search_left(arr, target):
            # Custom binary search to find the leftmost insertion point
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        n = len(nums) // 2  # Divide the array in half
        total = sum(nums)
        half = total // 2  # We want to get as close as possible to half of the total sum
        ans = abs(sum(nums[:n]) - sum(nums[n:]))  # Initial answer based on splitting the array in half

        # Calculate possible sums of subsequences for the first half and second half
        for k in range(1, n + 1):
            left = generate_combinations(nums[:n], k)  # Generate all combinations of size k from the first half
            right = generate_combinations(nums[n:], n - k)  # Generate all combinations of size n-k from the second half

            right.sort()  # Sort the second half sums for binary search

            for num in left:
                new_target = half - num
                i = binary_search_left(right, new_target)

                # Check the difference with the ceiling value (if it exists)
                if 0 <= i < len(right):
                    left_ans_sum = num + right[i]
                    right_ans_sum = total - left_ans_sum
                    diff = abs(right_ans_sum - left_ans_sum)
                    ans = min(ans, diff)

        return ans
