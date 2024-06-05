# Method 1 : Brute force: O(n^ 4)

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)

        def checkEqualXor(i, j, k):
            x1 , x2 = 0, 0
            for ind in range(i, j):
                x1 ^= arr[ind]
            for ind in range(j, k + 1):
                x2 ^= arr[ind]
            return x1 == x2
        
        cnt = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if checkEqualXor(i, j, k):
                        cnt += 1
        return cnt


# Method 2: Brute force with prefix sum
# 1)  check each possible pair using three loops.
# 2) for checking xor between pair(i, j), we can use same logic as "prefix sum".
# Because '^' also follow complement property like '+' and '-'.
# e.g" a ^ b = c => b = a ^ c and a = b ^ c

# tIme: O(n^3)


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)

        xor_pair = [0]*(n + 1)
        for i in range(n):
            xor_pair[i + 1] = xor_pair[i] ^ arr[i]

        cnt = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if xor_pair[j] ^ xor_pair[i] == xor_pair[k + 1] ^ xor_pair[j]:
                        cnt += 1
        return cnt

# Method 3: Optimising to O(n^2)
# Logic: 1) We are searching for sub-array of length ≥ 2 and we need to split it to 2 non-empty arrays 
# so that the xor of the first array is equal to the xor of the second array. 
# vvi: 2)  This is equivalent to searching for no of sub-array with xor = 0.
# Reason: if we combine both arrays then xor should be = 1.

# 3) so just find the subarray checkinmg each pair(i, j) having xor = 0
# if xor = 0 then add ans = length_subarray - 1 

# why ?
# if length is 'n' then no of ways we can divide it in (i, j, k) = n -1 (no of element should >= 2).


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)

        xor_pair = [0]*(n + 1)
        for i in range(n):
            xor_pair[i + 1] = xor_pair[i] ^ arr[i]
        
        cnt = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if xor_pair[j + 1] ^ xor_pair[i] == 0:
                    length = j - i + 1    
                    cnt += length - 1
        return cnt

# othwe way of checking equal xor 
cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if xor_pair[j + 1] == xor_pair[i] :
            # if xor at index 'i-1' = xor at index 'j' then it means
            # xor from 'i' to 'j' = 0
            length = j - i + 1    
            cnt += length - 1


# Method 4:
# Similar way as : "560. Subarray Sum Equals K".

# 1) suppose we are at index 'j' and if we have seen same xor before at any 'i' then
# it means xor from 'i + 1' to 'j' = 0.

# 2) so if we count the occurrence of every xor and sum of all the indexes at which we have seen same xor then
# we can get the ans.
# How ?
# e.g: array : a[0], a[1].... a[n - 1]
# say currently we are at index j and let xor([0...j]) = x.

# Now say x has occurred 3 times previously at indices (i1, i2, i3) then 
# our answer for j will be = (j - i1 - 1) + (j - i2 - 1) + (j - i3 - 1)

# simplyfying above :
# f * j - (i1 + i2 + i3) - f = (j - 1) * f - (i1 + i2 + i3)
# f = no. of times x has occurred previously.

# (i1 + i2 + i3) = sum of all the indices where x has occurred previously.

# for this we will need two map, one to store the frequency and other to find the sum.

# if we do like this then we will get less ans.
# ans = 0
# for j in range(n):
#     cur_xor ^= arr[j]
#     ans += freq[cur_xor] * j - sum_indexes[cur_xor] - freq[cur_xor]
#     freq[cur_xor] += 1
#     sum_indexes[cur_xor] += j
# return ans

# why above one will give wrong ans. say  when we have to include say '0 - 4'
# i.e say at index 'j = 4', it has same xor at index '0'.
# then in this case ans should be = 4
# but checking like this will give ans = 3
# how? 
# It will subtract '1'(freq[0]) also. 
# this will only happend when we will find xor at any index = 0 (which is same as our base case)
# so we have to avoid this .
# to avoid this don't subtract 'freq[cur_xor]' in ans rather add 'j+1' in sum and subtarct sum only.

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        freq        = collections.defaultdict(int)
        sum_indexes = collections.defaultdict(int)   # sum of indices where cur_xor has occured before
        freq[0] = 1  
        sum_indexes[0] = 0
        cur_xor = 0
        ans = 0
        for j in range(n):
            cur_xor ^= arr[j]
            ans += freq[cur_xor] * j - sum_indexes[cur_xor]
            freq[cur_xor] += 1
            sum_indexes[cur_xor] += j + 1
        return ans


