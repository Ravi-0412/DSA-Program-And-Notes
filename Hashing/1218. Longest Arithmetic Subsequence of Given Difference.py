# Method 1: Exactly same code of Q :" 1027. Longest Arithmetic Subsequence"

# Time: O(n^2)
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n= len(arr)
        dp = collections.defaultdict()
        for i in range(n):
            for j in range(i):
                diff= arr[i] - arr[j]
                if diff != difference:
                    continue
                # Agar is diff ka koi sequence index 'j' pe h tb uska length me  add kar do '+1'
                # Nhi to ye dono dono ko mila ke ek nya sequence bna ko at index 'i' having length= 2
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
        # Ab give difference ka Ap ka max length return kar do.
        ans = 1
        for key, value in dp.items():
            if key[1] == difference:
                ans = max(ans, value)
        return ans


# Method 2: Optimised one

# Just similar to 'Two Sum".

# Difference: Here we need to find the max length also.
# For this we will store in value the 'length of sequence'.

# Observation vvi: if 'num' is the next number of sequence then 'num-difference' must be present there.
# Otherwise we will start new sequence from cur 'num'.
# On this observation, we can think of hashamp like :"2453. Destroy Sequential Targets".

# While Traversing if 'num - difference' say = 'num1' is already there then means 'num - num1'= difference.
# So will add '+1' to 'num1' else we will start new seq from here so we will update 'lengths[num] = 1'.

# Time : O(n)= space

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        lengths = collections.defaultdict(int)  # [num : length] => length of AP with given difference when last number considered is 'num'.
        ans = 1
        for num in arr:
            lengths[num] = 1 + lengths[num - difference]
            ans = max(ans, lengths[num])
        return ans


# Note : isme  Q "2453. Destroy Sequential Targets" ka same remainder wala concept nhi lagega kyoni
# Yahan order of ele matter karega i.e (next wala pichle se bda hoga and order me hoga) but us Q me matter nhi karega.