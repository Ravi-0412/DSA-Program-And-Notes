# 1st method is sorting
# since you have to arrange the ele in ascending order basically so sorting will always a solution
# time: O(nlogn), space: O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()

# Java
"""
import java.util.Arrays;

class Solution {
    public void sortColors(int[] nums) {
        // 1st method is sorting
        // since you have to arrange the ele in ascending order basically so sorting will always a solution
        // time: O(nlogn)
        Arrays.sort(nums);
    }
}
"""

# C++
"""
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        sort(nums.begin(), nums.end());
    }
};
"""

# 2nd Method
"""
Approach:
1) Count the number of 0s, 1s, and 2s in the array.

2) Overwrite the array: first all 0s, then 1s, then 2s.

Time: O(n), Space: O(1) (in-place, just using 3 counters)
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3
        for num in nums:
            count[num] += 1
        index = 0
        for i in range(3):
            for _ in range(count[i]):
                nums[index] = i
                index += 1

# Java
"""
class Solution {
    public void sortColors(int[] nums) {
        int[] count = new int[3];
        for (int num : nums) count[num]++;
        int index = 0;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < count[i]; j++)
                nums[index++] = i;
    }
}
"""

# C++
"""
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count[3] = {0};
        for (int num : nums) count[num]++;
        int index = 0;
        for (int i = 0; i < 3; ++i)
            for (int j = 0; j < count[i]; ++j)
                nums[index++] = i;
    }
};
"""


# 3rd method:
"""
just count the no of 0,1,2 in an list of size '3' then store ans according to count.

3rd method(using double pointer): time=O(N),Space: O(1).. Q is made on this approach only

it can't be done by two pointer so we have to take another pointer also for 
handling the cases like after swapping if low(1st pointer) points to 1 and there is more '0' in the middle
this type of cases can't be handled by the two pointer e.g :[2,0,2,1,1,1,0,1,1]

So we need one more pointer to put all '1' in middle automatically by swapping '0' and '2'.

move the array 0 at front ,1 in the middle and 2 at the last
final goal is to make this 'low' and 'high' pointer points to 
1st and last index of all consecutive 1's respectively.
Before low all will be zero and low will point to the first one at last, 
after high all will be 2, high will point to the last one at last.

This is known as  " dutch partitioning algorithm".

# Note vvi: keep above logic in mind, may be helpful in other problems also

Time Complexity : O(n)
Space Complexity : O(1)
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        

        # current will max point till the last '1',  so 'curr' will never go beyond the 'high'.
        current,low=0,0
        high= len(nums)-1
        # after high all the elements will be two only and before 'low' all the 
        # ele will be '0' only
        while(current<=high):
            if nums[current]== 0:
                # swap it with nums[low] as low will be pointing to 1st one i.e before low all are '0'.
                nums[current],nums[low]= nums[low], nums[current] 
                low += 1
                current += 1 # we have made one correct move. incr here since 'nums[low]]' will contain '1' only can't have either '0' or '2' expect index '0'.
            elif nums[current]== 1:
                # don't swap as main aim to curr to put '1' in the middle, simply incr curr by 1
                current+= 1
            # if nums[current] ==2:
            else:  
                # # swap it with nums[high] as after high all will be '2' only
                nums[current], nums[high]= nums[high], nums[current]
                high-= 1
                # don't move the current since after swapping in this
                # cases current can contain '2' also if nums[high] has also '2'.
        return nums

# Java Code 
"""
import java.util.*;

class Solution {
    public void sortColors(int[] nums) {
        int current = 0, low = 0, high = nums.length - 1;

        // After 'high', all elements will be '2' only.
        // Before 'low', all elements will be '0' only.
        while (current <= high) {
            if (nums[current] == 0) {
                // Swap it with nums[low] as low will be pointing to the first '1'.
                swap(nums, current, low);
                low++;
                current++;  // We have made one correct move. Increment since nums[low] will now contain '1'.
            } else if (nums[current] == 1) {
                // Don't swap, just increment 'current' as '1' should be in the middle.
                current++;
            } else {  // nums[current] == 2
                // Swap it with nums[high] since after 'high' all elements should be '2'.
                swap(nums, current, high);
                high--;
                // Don't move 'current' since after swapping, nums[current] might still be '2'.
            }
        }
    }

    private void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int current = 0, low = 0, high = nums.size() - 1;

        // After 'high', all elements will be '2' only.
        // Before 'low', all elements will be '0' only.
        while (current <= high) {
            if (nums[current] == 0) {
                // Swap it with nums[low] as low will be pointing to the first '1'.
                swap(nums[current], nums[low]);
                low++;
                current++;  // We have made one correct move. Increment since nums[low] will now contain '1'.
            } else if (nums[current] == 1) {
                // Don't swap, just increment 'current' as '1' should be in the middle.
                current++;
            } else {  // nums[current] == 2
                // Swap it with nums[high] since after 'high' all elements should be '2'.
                swap(nums[current], nums[high]);
                high--;
                // Don't move 'current' since after swapping, nums[current] might still be '2'.
            }
        }
    }
};
"""



