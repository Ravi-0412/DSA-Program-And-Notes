# Logic:  
"""
Since we have to include all the given number in permutation.
This Q reduces to 'Find the next greater number than the given number only using the digit of the given number'.
and for finding this we can start from righmost side.
Sbse smallest matlab last se hi replacement khojna hoga, kyonki starting se replace kiye to number bda ho jayega.

e.g: [9, 4, 8, 3, 6, 5, 2, 1]
Next greater = [9, 4, 8,5,1,2,3,6]
Think how we will reach till here?
i) '3' ko replace karna hoga iske next greater se i. 5
'3' kaise milega?
Ans: Last se agar traverse karenge tb ascending order ka flow yhi pe tutega matlab is number se next bda chahiye from right side.(say 'i-1')
ii) For finding next number, again traverse from last , say 'j'.
iii) Now swap these two.(i-1, j)
iv) after swapping to make sure that formed number is next greater, we need to make number from index 'i' to last in increasing order(if we see from front)
which is in decreasing order as of now. For this just reverse number from index 'i' to last.
v) We will get our ans.

#Below explanation for coding purpose.

Note: No need to traverse whole number we only need to rearrange numbers from index 'i -1' to last index such that
nums[i] > nums[i -1] i.e find the 1st index 'i-1' which breaks the ascending order rule from last.
it means we have got a smaller number at 'i-1' so we can rearrange ele from index 'i-1' to last index to get
our ans i.e next greater number.

Steps:
1) 
i.e find 'i-1' such that nums[i] > nums[i - 1]  then ,
(from index 'i' to last ele, element will be in descending order.

Now we have to rearrange all numbers from 'i-1' to last to get the ans.
Numbers before 'i-1' won't matter in ans. Replacing with any number before 'i-1' will give larger number than expected.

2) We will have to bring 1st number greater than nums[i-1] from right side i.e from index 'i' to last
at index 'i-1'.
So find the 1st element greater than 'nums[i-1]' from right.
ie. we have to search j' from last such that nums[j] > nums[i-1] 

3) Now we have found correct number for index 'i-1' which is at index 'j'.
so swap(i-1, j)

4) After swapping, number from index 'i' to last will be in descending order only
So to get minimum number value from index 'i' to last, we will have to reverse array from index 'i' to last.

5) Finally you will get the ans.

For visualisation take e.g : [9, 4, 8, 3, 6, 5, 2, 1]
i = 4, j = 5

Time complexity : O(n)
Space Complexity : O(1)
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n= len(nums)
        i= n- 1  # will point to the index such that nums[i] < nums[i-1] from the right.
        j= n- 1  # will point to the index such that nums[j] > nums[i -1] from the right.

        # 1) first find 'i'.
        while i> 0 and nums[i-1] >= nums[i]:
            i-= 1
        if i== 0:
            # Means number given number is the largest number so just return the smallest number
            return nums.reverse()
        # 2)  find 'j'.
        while nums[i-1] >= nums[j]:
            j-= 1
        # 3) now swap the 'j' and 'i-1'.
        nums[j], nums[i-1]= nums[i-1], nums[j]
        # 4) reverse the arr from index 'i' to last.
        # return nums[:i] + (nums[i+1:])[::-1]   # this will not work. because 'nums[:i]: create another array but nums[i:] modifies the same arr'.
        nums[i:]= nums[i:][::-1]


# Java code:
"""
import java.util.*;

class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int i = n - 1;  // will point to the index such that nums[i] < nums[i-1] from the right
        int j = n - 1;  // will point to the index such that nums[j] > nums[i -1] from the right

        // 1) first find 'i'.
        while (i > 0 && nums[i - 1] >= nums[i]) {
            i--;
        }
        if (i == 0) {
            // Means the given number is the largest number, so just return the smallest number
            reverse(nums, 0, n - 1);
            return;
        }
        // 2) find 'j'.
        while (nums[i - 1] >= nums[j]) {
            j--;
        }
        // 3) now swap 'j' and 'i-1'.
        swap(nums, j, i - 1);
        // 4) reverse the array from index 'i' to last.
        reverse(nums, i, n - 1);
    }

    private void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start++, end--);
        }
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int i = n - 1;  // will point to the index such that nums[i] < nums[i-1] from the right
        int j = n - 1;  // will point to the index such that nums[j] > nums[i -1] from the right

        // 1) first find 'i'.
        while (i > 0 && nums[i - 1] >= nums[i]) {
            i--;
        }
        if (i == 0) {
            // Means the given number is the largest number, so just return the smallest number
            reverse(nums.begin(), nums.end());
            return;
        }
        // 2) find 'j'.
        while (nums[i - 1] >= nums[j]) {
            j--;
        }
        // 3) now swap 'j' and 'i-1'.
        swap(nums[j], nums[i - 1]);
        // 4) reverse the array from index 'i' to last.
        reverse(nums.begin() + i, nums.end());
    }
};
"""
