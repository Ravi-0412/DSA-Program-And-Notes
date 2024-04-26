# Method 1:
# Brute force
# Time: O(m*n)

# Method 2:
# Time : O(m + n)

# Logic: We only need to care about actual value if that number is present in nums2.
# So we will store the actual value in ans.
# And to check that number is present in nums2 or not in O(1), 
# we need either dictionary or set.

# Using dictionary we can check also and store ans also and later return also easily.

# Here dictionary will store ans for numbers that have answer.
# Note: For number that is present in nums2 but has no answer then at last
# while returning we will automatically get '-1'. 


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st, d = [], {}
        for n in nums2:
            # 'n' will ans for all ele of stack till stack top < n.
            while st and st[-1] < n: 
                d[st.pop()] = n   # pop as we have found the greater ele for num on top of the stack
            st.append(n) 
        return [d.get(x, -1) for x in nums1]   # if there is value of 'x' then
                                                #  return that otherwise return '-1'
        



