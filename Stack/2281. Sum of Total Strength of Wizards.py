# This Q is combination of : 1) "907. Sum of Subarray Minimums"  and 2 ) "84. Largest Rectangle in Histogram".

# Logic: 
# For each strength[i], we can find a non-empty index range (left, right) where strength[i] is the min value. 
# So for all subarrays in this range including strength[i], the total strength is strength[i] * the sum of those subarray sums.

# Note: The reason we use < on left but <= on right is to avoid duplicates.
# e.g: 1 2 3 4 2 3 4 2 1
# for subarray '2 3 4 2' ,  we want to calculate the strength using the 2nd 2 but not the first 2.

# Note vvi: The techniques regarding prefix sum and monostack come to our minds respectively, 
# when we see the problem involves to find the sums and find the minimums of the subarrays.

# Note: understand the last part properly i.e how we are adding into ans.

# Note: more explanation in notes , page no: 38

# Time : O(n)

class Solution:
    def totalStrength(self, a: List[int]) -> int:
        mod = 10 **9 + 7
        n = len(a)
        next_smaller_left =  [-1] * n   # will store the 'index' where strengh[index] <= strength[i] 
                                        # Tab tak left me jana h jb tak <= na mil jaye
        next_smaller_right = [-1] * n   # will store the 'index' where strengh[i] < strength[index]
                                        # Tab tak right me jana h jb tak strictly chota (< )  na mil jaye

        # 1st getting the next_smaller <= on right
        # traverse left to right
        stack1 = []
        for i in range(n):
            while stack1 and a[stack1[-1]] > a[i]:
                # means we got the next_smaller right  < for stack.pop().
                ind = stack1.pop()
                next_smaller_right[ind] = i
            stack1.append(i)
        
        # Now getting the next_smaller <= on left
        # traverse rigth to left
        stack2 = []
        for i in range(n-1, -1, -1):
            while stack2 and a[stack2[-1]] >= a[i]:
                # means we got the next_smaller left  <= for stack.pop(). 
                ind = stack2.pop()
                next_smaller_left[ind] = i
            stack2.append(i)
        # print(next_smaller_left)
        # print(next_smaller_right)
        
        # Calculate the prefix sum in 'prefix' arr
        prefix = [0]*(n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + a[i]) % mod
        
        # Now calculate prefix Sum of 'prefix' in 'prefPrefix'.
        prefPrefix = [0] *(n + 2)
        for i in range(n + 1):
            prefPrefix[i + 1] = (prefPrefix[i] + prefix[i])  % mod
        print(prefix)
        print(prefPrefix)

        # prePrefix is two index ahead of 'i'. 
        # 'left' and 'right'  is excluded i.e from 'left + 1' to 'right -1' we have to consider.
        # right -1 = right + 1 in prePrefix and so on for left.
        # see the notes for proper visualisation.
        
        ans= 0
        for i in range(n):
            left = next_smaller_left[i]  #     
            if next_smaller_right[i] == -1:
                right = n # here making one index ahead(i.e n instead of n-1) and adding '+1' in ans will make two index ahead.
            else:
                right = next_smaller_right[i]
            # Here left denotes the lowest index and 'right' denotes the highest index for which 'a[i]' is minimum
            # just we do in 'rain trapping problem'.
            ans += a[i] * ((prefPrefix[right + 1] - prefPrefix[i + 1]) *(i - left) - (prefPrefix[i + 1] - prefPrefix[left + 1]) *(right - i)) % mod
        
        return ans % mod



# Note: understand the above solution properly and try to do in one pass also.

