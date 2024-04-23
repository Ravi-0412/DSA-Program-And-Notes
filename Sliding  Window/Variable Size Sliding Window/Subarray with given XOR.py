# just same way "560.Subarray sum equals k" and "Longest subArray having sum k"


# what we are doing actually?
# Ans: supoose we calculated 'xorr' then if can find 'x' such that x= B ^ xorr then means we can get 'B' no of times 'x' we got till now.


# Proof:  Say at any index 'j', total xor = 'cur_xor' and let say we have seen xor = 'cur_xor ^ k' before at index 'i' and other indices also.
# let take 'cur_xor ^ k' at index 'i' and xor from 'i+1' to 'j' is 'X' then, we can write:
# cur_xor(xor till now) = xor_till_i ^ X and xor_till_i = cur_xor ^ k then
# cur_xor = cur_xor ^ k ^ X then we will get X = K.

# So our aim is to find the number of such 'x' and for this we are using hashmap to store the count of each xor we got till now.

# why this is working?
# say if res= a^b then res^a= b and res^b= a. (property of xor)
# res= xor till now. so we by taking the xor of 'res' with 'k' indirectly we are finding the another number 'a' or 'b'.


# time: O(n), space: O(1).

class Solution:
    def solve(self, A, B):
        prefix_xor= {0: 1}   # [cur_xor: freq] # to handle the case when cur_xor= B itself  then cur_xor ^ B= 0. 
                            # means one subarray we have found(from '0' to curr index)
        ans= 0
        cur_xor= 0
        for num in A :
            cur_xor^= num
            if (cur_xor ^ B) in prefix_xor:
                ans+= prefix_xor[cur_xor ^ B]
            prefix_xor[cur_xor]= 1+ prefix_xor.get(cur_xor, 0)
        return ans


