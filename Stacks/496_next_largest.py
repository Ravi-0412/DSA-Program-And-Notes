# very very concise with the help of dict andd stack
# will not work for duplicates ele
# for leetcode type Q
def nextGreaterElement(findNums, nums):
    st, d = [], {}
    for n in nums:
        while st and st[-1] < n:  # when we have found next greater ele.
                                  # for pre ele if stack not empty
                                 # next greater ele will be 'n'
            d[st.pop()] = n   # pop as we have found the greater ele for num on top of the stack
                             # dict will map each distinct ele with its nearest neighbour till st[-1]<n
                             # dict doesn't sore duplicates
                             # assign the stack top with 'n' as val in dict till st[-1] <n
        st.append(n)   # append 'n' if stack is empty or  greater ele is not found yet
    print(d)  # dict will map each ele with their next greater right if exist i.e except the last ele and the largest ele of the array
    return [d.get(x, -1) for x in findNums]   # if there is value of 'k' then
                                              #  return that otherwise return '-1'

nums1 = [4,1,2]
nums2 = [1,3,4,2,8,5,6]
print(nextGreaterElement(nums1,nums2))


