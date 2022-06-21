# method 1: time- o(n), space- o(n)
# just traverse the list from last and keep
# storing the maximum element 
class Solution:
    def leaders(self, A, N):
        max_ele_seen_so_far= A[N-1]
        res= [A[N-1]]
        for i in range(N-2, -1, -1):
            if A[i]>= max_ele_seen_so_far:
                # res = [A[i]] +res
                res.append(A[i])
                max_ele_seen_so_far= A[i]
        res.reverse()
        return res
