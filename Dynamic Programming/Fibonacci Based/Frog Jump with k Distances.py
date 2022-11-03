# Recursive way
def frogJump(n, heights,k) :
    if n==1:  # means we have reached the destination so simply return '0'
        return 0
    
    # just do by minimal base case and check condition while calling the function
    # if n==2: # only we have to go one step 
    #     return abs(heights[1] - heights[0])
    mn= 9999999
    for i in range(1,k+1):
        if n-i >=1
    mn= min(abs(heights[n-1]-heights[n-i-1]) + frogJump(n-i,heights))   # height idexing is strating from '0' but stair count from 1
    return mn

# memoization
# time: O(n*k)