def findMax(nums):              
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right) // 2
    # max and min will always lie in the unsorted part
        if nums[left] >nums[mid]:   # means array from 'mid' to 'right' is unsorted
            right = mid-1            # so max will lie beyond mid and mid can also be the maximum

        else:      # here it will guarantee that array from 
        # mid to right is sorted and start to mid is unsorted
        # so max will lie in this range only 
            left= mid
    # after loop will fail , start and end will point to 
    # the same ele and that will be the maximum ele
    # because both are merging towards the index of max ele in each iteration
    # return nums[left]
    
    return nums[left]

# nums= [3,4,5,1,2]
# nums= [7,8,9,1,2,3]
# nums= [6,7,8,9,1,2]
# nums= [8,9,1,2]
# nums= [6,8,9,10,3,4,5]
# nums= [9,1,2,3]

# nums= [6,7,8,9,1]
# nums= [5,6,7,8,9,1,2,3,4]
# nums= [1,2,3,4]


print(findMax(nums))

