
# just same logic as "Longest Subarray having sum= k" but here we will update every time to minimise the length.
def lenOfSmallestSubarr(A, N, K) : 
    prefix_sum= {0:-1}    # will store the extra sum(may be negative or positive).
    min_length,curr_sum= float('inf'), 0
    for i in range(N):
        curr_sum+= A[i]
        if (curr_sum-K) in prefix_sum:                                  
            min_length= min(min_length,i-prefix_sum[curr_sum-K])  
        prefix_sum[curr_sum]= i  
            
    return min_length

# arr= [2, 4, 6, 10, 2, 1]
# K = 12 

# arr= [1, 2, 4, 3, 2, 4, 1] 
# K = 7

arr= [-8, -8, -3, 8]
k= 5

n= len(arr)

print(lenOfSmallestSubarr(arr, n, k))