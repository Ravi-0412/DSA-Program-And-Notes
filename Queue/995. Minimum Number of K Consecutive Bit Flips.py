# Logic: Since we are doing XOR operation, even flips will be equal to zero flips, odd flips will be equal to one flip.
#  So, instead of modifying K bits every time we encounter zero, we can just track the current number of flips.

# How to do ?
# we are using a queue to track flips. When we 'flip', we put the end index of our flip (i + K - 1) into our queue.
# this will indicate till index 'i+k-1' we have done one more flips.
# VVI: The size of the queue will indicate number of flips for all elements in range from queue[0] to queue[n-1].
# After each index remove the elements from front of queue if it won't cover the upcoming elements.

# Note: that we dont actually flip the values in the array. Since all possible values are 0 and 1, 
# we can simply use a knowledge of "how many times" any given index has been flipped to know the 
# whats the current state of the value is.

# Time = sapce = O(n)

from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        is_flipped = deque()
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                if not is_flipped or len(is_flipped) % 2 == 0:
                    # if no flip or flipped even times then value will be '0' only so we need to flip
                    ans += 1
                    is_flipped.append(i + k - 1)  # last index till where we have to flip to make nums[i] = 1
            else:
                # if nums[i] == 1 and flipped odd times then we need to flip
                if len(is_flipped) % 2 != 0:
                    ans += 1
                    is_flipped.append(i + k - 1)
            # now remove the element from front of queue if interval in queue is not in range for upcoming elements
            if is_flipped and i >= is_flipped[0]:
                is_flipped.popleft()
        return ans if not is_flipped else -1  # return ans if queue is empty means we have made all elements = 1 else -1


# java
"""
class Solution {
    public int minKBitFlips(int[] nums, int k) {
        int n = nums.length;
        Queue<Integer> isFlipped = new LinkedList<>();
        int ans = 0;
        for(int i = 0 ; i < n; i ++){
            if(nums[i] == 0 ) {
                if(isFlipped.isEmpty() || isFlipped.size() % 2 == 0) {
                    // if no flip or flipped even times then value will be '0' only so we need to flip
                    ans += 1;
                    isFlipped.offer(i + k -1); // last index till where we have to flip to make nums[i] = 1
                }
            }
            else {
                // if nums[i] == 1 and flipped odd times then we need to flip
                if(isFlipped.size() % 2 != 0) {
                    ans += 1;
                    isFlipped.offer(i + k -1);
                }
            }
            // now remove the element from front of queue if interval in queue is not in range for upcomingh elements
            if(!isFlipped.isEmpty() && i >= isFlipped.peek())
                isFlipped.poll();
        }
        return isFlipped.isEmpty() ? ans : -1;  // return ans if queue is empty means we have made all elemnts = 1 else -1
        
    }
}
"""
