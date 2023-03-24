# logic: same logic as "Allocate minimum no of pages".
# Only Diff is that here we have to maximise rather than minimising.
# for maximising we use the pattern of dinding the "last index of an ele".
# i.e use start <=end in while loop and at last we return 'end.

# we need to divide into 'k+1' pieces. And we can only give consecutive chunks to one people.

# Meaning of isPossible(minSweetness) function?
# Ans: if myself take minSweetness as 'mid' then can we give total sweetness >= 'mid' as some of chunks to each of my friends and me also i.e in 'k+1' parts?
# since every friend must get >= sweetness than me.

# totally same as '410. Split Array Largest Sum' .
# How? => we have to divide the array into 'k+1' subarrays such that minimum sum of any of the subarray is maximum.
# just here if possible(mid), then we have to increase instead of decrease and vice versa.

# just same logic as 'find last index of an ele'.

# for range:
# 1) start: we can min of all
# 2) end:   we can take sum(arr)  when k= 0  => more constraint way ,we can take max of average.

# submitted on lintcode(LC Premium)
# time: O(n*log(A)), A= sum(sweetness)//(k+1)
class Solution:
    def maximize_sweetness(self, sweetness: List[int], k: int) -> int:
        n= len(sweetness)
        start, end= min(sweetness), sum(sweetness)//(k+1)  # max i can get = sum(sweetness)//(k+1)
        while start <= end:
            mid= start + (end-start)//2
            if self.isPossible(sweetness,n, k +1 ,mid):  # search for even more bigger but mid can be the ans also.
                start= mid + 1
            else:
                end= mid -1
        return end

    def isPossible(self, A, N, M, minSweetness):
        chunks, sum= 0, 0
        for i in range(N):
            sum+= A[i]
            if sum >= minSweetness:   # after any people get the minSweetness then start giving next chunks to different people.
                chunks+= 1
                sum= 0
        return chunks >= M