# Recursive way
def frogJump(n, heights,k) :
    if n==1:  # means we have reached the destination so simply return '0'
        return 0
    
    # just do by minimal base case and check condition while calling the function
    # if n==2: # only we have to go one step 
    #     return abs(heights[1] - heights[0])
    mn= float('inf')
    for i in range(1,k+1):
        if n-i >=1:
            mn= min(mn, abs(heights[n-1]-heights[n-i-1]) + frogJump(n-i,heights, k))   # height idexing is starting from '0' but stair count from 1
    return mn

# heights= [10,30,40,50,20]
heights= [10,20,10]
n= len(heights)
# print(frogJump(n, heights,3))

print(frogJump(n, heights,1))


# memoization
# time: O(n*k)
