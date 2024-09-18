# just totally same as "300. LIS". This problem is asking for LIS in two dimension.
# Only difference is that here envelopes will be random i.e aage-piche ho sakta and so on(see the 1st example explanation).
# vvi why sort?
# to check easily which can go into other envelope. 

# vvi Basic of these types of Q:
# This problem is asking for LIS in two dimensions, width and height. Sorting the width reduces the problem by one dimension. 
# If width is strictly increasing, the problem is equivalent to finding LIS in only the height dimension.
# However, when there is a tie in width, a strictly increasing sequence in height may not be a correct solution. 
# For example, [[3,3] cannot fit in [3,4]].Sorting height in descending order when there is a tie prevents such a sequence to be included in the solution.

# The same idea can be applied to problems of higher dimensions. For example, box fitting is three dimensions, width, height, and length. 
# Sorting width ascending and height descending reduces the problem by one dimension. 
# Finding the LIS by height further reduces the problem by another dimension. When find LIS based on only length, it becomes a standard LIS problem.

# main: [3, 4] cannot contains [3, 3], so we need to put [3, 4] before [3, 3] when sorting otherwise it will be counted as an increasing number if the order is [3, 3], [3, 4].

# vvi: indirectly aisa Q ko kisi tarah hmko 1D me le aana h taki direct LIS wala logic lga sake (bina kuch change kiye).

# time: O(2^n)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key= lambda x: [x[0], -x[1]])  # agar width same hua to phle usko aage rakhna h jiska height jyada ho(isliye, -x[1]).
        # sort to phla ele ke anusar hi hoga but in case of equal kaise sort karna h isliye other parameter pass kar rhe. negative no show nhi karega 'nums' me actual hi show karega. 
        # sorting parameter sirf sort karne ke liye h.
        # nums= sorted(envelopes, key= lambda x: [x[0], -x[1]])   # we can do like this also

        nums= [ele[1] for ele in envelopes]   # storing only the height since we have to check only the height. Now totally same as LIS.
        return self.helper(0, -1, nums)
        
    def helper(self, ind, pre_ind, arr):
        if ind== len(arr):
            return 0
        take= 0
        notTake= self.helper(ind +1, pre_ind, arr)  # if we not include
        # when we include but we can only include in following condition only.
        if pre_ind== -1 or arr[ind] > arr[pre_ind]:  # when can only include if strictly increasing
            take= 1+ self.helper(ind +1, ind, arr)
        return max(take, notTake)

# even after memoisation, will give TLE since after memoisation time= O(n^2).
# But n is '10^5' so.

# applying the binary search logic of LIS.
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key= lambda x: [x[0], -x[1]])  # agar width same hua to phle usko aage rakhna h jiska height jyada ho(isliye, -x[1]).
        # sort to phla ele ke anusar hi hoga but in case of equal kaise sort karna h isliye other parameter pass kar rhe. negative no show nhi karega 'nums' me actual hi show karega. 
        # sorting parameter sirf sort karne ke liye h.
        # nums= sorted(envelopes, key= lambda x: [x[0], -x[1]])   # we can do like this also

        nums= [ele[1] for ele in envelopes]   # storing only the height since we have to check only the height. Now totally same as LIS.
        sub= []  # will store the ele in strictly increasing order only.
        for num in nums:
            if not sub or sub[-1] < num:
                sub.append(num)
            else: # find the position of num in sub and replace that ind with num
                idx= bisect.bisect_left(sub, num)  # simply bisect_left(sub,num). 
                sub[idx]= num  # no neeed to check if 'idx'>= len(sub) because this case is already handled in above 'if' condition.
        return len(sub)




# my mistake 1:
# was working because i was chekcing both the dimension separately.
# correct only but TLE.
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        return self.helper(0, -1, envelopes)
    def helper(self, ind, pre_ind, envelopes):
        if ind== len(envelopes):
            return 0
        # if we not include
        take= 0
        notTake= self.helper(ind +1, pre_ind, envelopes)
        # when we include but we can only include in following condition only.
        if pre_ind== -1 or (envelopes[ind][0] > envelopes[pre_ind][0] and envelopes[ind][1] > envelopes[pre_ind][1] ): 
            take= 1+ self.helper(ind +1, ind, envelopes)
        return max(take, notTake)

# mistake in sorting. 
# memoisation. TLE since n= 10^5 so (n^2) will not work.
# time: O(n^2)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        n= len(envelopes)
        dp= [[-1 for j in range(n+1)] for i in range(n +1)]
        return self.helper(0, -1, envelopes, dp)
    def helper(self, ind, pre_ind, envelopes, dp):
        if ind== len(envelopes):
            return 0
        if dp[ind][pre_ind + 1]!= -1:
            return dp[ind][pre_ind + 1]
        # if we not include
        take= 0
        notTake= self.helper(ind +1, pre_ind, envelopes, dp)
        # when we include but we can only include in following condition only.
        if pre_ind== -1 or (envelopes[ind][0] > envelopes[pre_ind][0] and envelopes[ind][1] > envelopes[pre_ind][1] ): 
            take= 1+ self.helper(ind +1, ind, envelopes, dp)
        dp[ind][pre_ind +1]= max(take, notTake)
        return dp[ind][pre_ind + 1]

    

# my mistakes 2:
# But this will not work e.g: if we select any evelope having very large 'width' or 'height' then we will not able to choose a lot of enevelopes further.
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        print(envelopes)
        n= len(envelopes)
        pre= (envelopes[0][0], envelopes[0][1])  # width and height of first envelope
        ans= 1   # first ele must be there since it has smallest width and height than all.
        for i in range(1, n):
            if envelopes[i][0] > pre[0] and envelopes[i][1] > pre[1]:
                print(i)
                ans+= 1
                pre= (envelopes[i][0], envelopes[i][1])
        return ans
        
# Java correct solution
"""
import java.util.Arrays;

class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        // Step 1: Sort the envelopes by width (ascending). If the widths are equal, sort by height (descending).
        Arrays.sort(envelopes, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1]; // Sort by height in descending order if widths are the same
            } else {
                return a[0] - b[0]; // Sort by width in ascending order
            }
        });
        
        // Step 2: Extract the heights array (since widths are sorted, now we only care about heights for LIS)
        int[] heights = new int[envelopes.length];
        for (int i = 0; i < envelopes.length; i++) {
            heights[i] = envelopes[i][1];
        }
        
        // Step 3: Find the length of the longest increasing subsequence in heights
        return lengthOfLIS(heights);
    }
    
    // Helper method to find the length of the longest increasing subsequence (LIS)
    private int lengthOfLIS(int[] nums) {
        int[] lis = new int[nums.length];
        int size = 0;
        
        for (int num : nums) {
            int idx = Arrays.binarySearch(lis, 0, size, num);
            if (idx < 0) {
                idx = -(idx + 1);  // binarySearch returns negative insertion point if not found
            }
            lis[idx] = num;  // Place the number in its correct position in the lis array
            if (idx == size) {
                size++;  // Increase the size if a new element is added at the end of the lis array
            }
        }
        
        return size;  // The size of the lis array will be the length of the LIS
    }
}

"""
