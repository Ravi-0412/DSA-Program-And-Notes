# just excatly same code as "713. Subarray Product Less Than K".
# After adding each ele, just find the length of valid subarray then that add to 'count'.

def NoOfSubarray(arr, k):
    n= len(arr)
    i, j= 0, 0
    curSum= 0
    count= 0
    while j < n:
        curSum+= arr[j]
        # i should go till 'j' because if there is any ele greater than 'k' itself then we will have to remove all.
        while i<= j and curSum >= k:  
            curSum-= arr[i]
            i+= 1
        count+= j - i + 1
        j+= 1
    return count


# arr= [1, 11, 2, 3, 15] 
arr= [2, 5, 6]
k = 10
print(NoOfSubarray(arr, k))

