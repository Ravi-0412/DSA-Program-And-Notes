# For the first k elements, we arrange in the following way: 1, k + 1, 2, k, 3, k - 1, ....
# i.e if 'i' is even then res[i]= i//2 + 1 else res[i]= (k + 1) - (i-1)//2
# For the remaining elements, we set a[i] = i + 1, for i = k + 1, ....,n
# i.e res[i]= i + 1.

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]: 
        if k >= n:
            return None
        res= [0]*n
        res[0]= 1
        # filling first 'k' elements
        for i in range(1, k + 1):
            if i % 2== 0:
                res[i]= i//2 + 1
            else:
                res[i]= (k + 1) - (i-1)//2
        # now we have got 'k' distinct number. we only need to maintain diff= '1' 
        # filling from 'k+1' to 'n'.
        for i in range(k+1, n):
            res[i]= i + 1
        return res
