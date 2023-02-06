# Brute force: O(n^2)


# method 2: use bit
# submitted on interview Bit

# what we are doing actually?
# Ans: supoose we calculated 'xorr' then if can find 'x' such that x= B ^ xorr then means we can get 'B' no of times 'x' we got till now.
# So our aim is to find the number of such 'x' and for this we are using hashmap to store the count of each xor we got till now.

# for more details read the striver logic in sheet.
# time: O(n), space: O(1).

class Solution:
    def solve(self, A, B):
        count= 0
        xorr= 0  # will store the xor till now
        xor_count= {}  # will store the xor that occured till now with their count
        for num in A:
            xorr= xorr ^ num
            if xorr== B:
                count+= 1
            if B ^ xorr in xor_count:  # if present means at this point we can get xor= B for different distinct(than before) subarrays.
                count+= xor_count[B ^ xorr]
            if xorr in xor_count:
                xor_count[xorr]+= 1
            else:
                xor_count[xorr]= 1
        return count


