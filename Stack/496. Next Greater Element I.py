# Logic: We only need to care about actual value if that no is present in nums2.
# So we will store the actual value in ans.
# And to check that no is presnet in nums2 or not in O(1), 
# we need either dictionary or set.

# sing dictionary we can check also and store ans also and later return also easily.

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
        

# Can do by other way also.


