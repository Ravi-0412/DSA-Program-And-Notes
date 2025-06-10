# 1st method: time o(n),space o(n) 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp,n= nums.copy(), len(nums)
        k= k%n
        for i in range(n):
            nums[(i+k)%n]= temp[i]
        return nums


# 2nd method: optimising the space complexity to O(1) for right rotation
# logic: 1)Reverse the last 'k' elements.. Q given reverse right so reverse the last 'k' elements
# 2) Reverse the remaining ele 'n-k' element from start 
# 3) and finally reverse the whole array 

# Time: o(n),space: o(1)


# for left rotation : 
# logic: 1)Reverse the first 'k' elements..Q given reverse left so reverse the first 'k' elements
# 2) Reverse the remaining ele 'n-k' from last i.e from index 'k+1' to 'n-1'
# 3) and finally reverse the whole array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n= len(nums)   
        k=k%n
        def reverse(a,l,h):
            i,j=l,h
            while(i<j):
                nums[i],nums[j]= nums[j],nums[i]
                i+= 1
                j-= 1
            
        reverse(nums,n-k,n-1)   # last 'k' elements
        reverse(nums,0,n-k-1)   # remaining 'n-k' ele from start
        reverse(nums,0,n-1)

# Java
"""
// Method 1: 
class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;
        int[] temp = nums.clone();  // Create a copy of the original array
        
        for (int i = 0; i < n; i++) {
            nums[(i + k) % n] = temp[i];  // Place elements in their new positions
        }
    }
}


// Method 2: 
class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;
        
        reverse(nums, n - k, n - 1);   // last 'k' elements
        reverse(nums, 0, n - k - 1);    // remaining 'n-k' elements from start
        reverse(nums, 0, n - 1);        // reverse the entire array
    }
    
    private void reverse(int[] nums, int l, int h) {
        int i = l, j = h;
        while (i < j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
    }
}
"""

# C++ Code 
"""
//Method 1

#include <vector>
#include <algorithm> // For std::copy

class Solution {
public:
    void rotate(std::vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;
        std::vector<int> temp = nums;  // Create a copy of the original vector
        
        for (int i = 0; i < n; i++) {
            nums[(i + k) % n] = temp[i];  // Place elements in their new positions
        }
    }
};

//Method 3

#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;
        
        reverse(nums, n - k, n - 1);   // last 'k' elements
        reverse(nums, 0, n - k - 1);  // remaining 'n-k' elements from start
        reverse(nums, 0, n - 1);      // reverse the entire array
    }
    
private:
    void reverse(vector<int>& nums, int l, int h) {
        int i = l, j = h;
        while (i < j) {
            swap(nums[i], nums[j]);
            i++;
            j--;
        }
    }
};
"""