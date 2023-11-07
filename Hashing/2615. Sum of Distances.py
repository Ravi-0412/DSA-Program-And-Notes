# Note: This Q is exactly same as "2121. Intervals Between Identical Elements".

# store the indexes at which all unique ele has occured. [num: [indexes]]. 
# Now, traverse the hashmap and if len(value) w.r.t any key is== 1 then unique ele so set the value at this index(value[0])= 0.

# if len(value) != 1 means duplicate is present.
# Then in this case  we will find the pairwise sum of difference.

# suppose if want to find the ans for index 'k' then
# ans[k]=(no_ele_left_side_of_k * k - leftSum_all_indexes_before_k) + (rightSum_all_indexes_after_k- no_ele_right_side_of_k * k).

# how we derived the above formula?
# Note: indices will be automatically stored in sorted order. 
# so we can apply this logic to get 'pairwise sum of difference' in O(n).

# suppose we are calculating for index 'k'.
# let there is three indices a,b,c with same value as nums[k] on left side and x,y be two indices with same value as nums[k] on right side.
# then ans for 'k'= (a- k + b- k+ c- k)  +  (x- k + y- k)   # left and right side
# ans=((a + b+ c) -(3*k)) + ((x+ y) - 2*k) = 
# (no_ele_left_side_of_k * k - leftSum_all_indexes_before_k) + (rightSum_all_indexes_after_k- no_ele_right_side_of_k * k)

# how to calculate for next index in O(1)?
# suppose we move from 'i' to 'i+1' in hashmap then
# leftSum for 'i+1'= leftSum + i, rightSum for 'i+1'= rightSum- i

# note: we are indirectly calculating the prefixSum and suffixSum for every index.

# Note vvi: When it comes to accumulation on history data in the same direction, think of prefix sum / postfix sum technique

# Note vvvi: Keep in mind how we calculate the pairwise sum of difference in O(n) for sorted array.

# time= space= O(n)

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        valueToIndexes= collections.defaultdict(list)   # [value: indexes]
        for i, num in enumerate(nums):
            valueToIndexes[num].append(i)  # all indices will get stored in ascending order only.
        for num, indices in valueToIndexes.items():
            if len(indices)== 1:  # unique ele
                ind= indices[0]
                nums[ind]= 0
            else:
                n= len(indices)
                leftSum= 0  
                rightSum= 0   # will be equal to sum of all indices
                for num in indices:
                    rightSum+= num
                for i, ind in enumerate(indices):
                    curAns= 0
                    noLeftSide= i
                    noRightSide= n- i  # including the curr ind also because we have to subtarct curr index value also from 'preRight'
                    curAns+= (ind * noLeftSide)- leftSum
                    curAns+= rightSum- (ind *noRightSide)
                    nums[ind]= curAns
                    leftSum+= ind
                    rightSum-= ind
        return nums

# Related Q: 
"2731. Movement of Robots"