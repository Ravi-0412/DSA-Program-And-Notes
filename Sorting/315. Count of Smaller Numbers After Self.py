# Exactly same as '493.Reverse pair'.

# Difference in both questions: 
# Note: While merging only we will get ans and element position changes while merge ,
# and for updating the ans we need to keep track of index as well.

# so : 1) create another array with [nums[i], i] 
# 2) Apply exact same 'method 2' for counting ans of '493.Reverse Pairs'.
# Only thing here add the count for that particular index.


# Very better solution

# Time: O(n + m)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numsIndex = [[nums[i], i] for i in range(n)]  # we need index also to update ans
        ans = [0]*n
        self.merge_sort_count_inversion(numsIndex, 0, n-1, ans)
        return ans
    
    def merge_sort_count_inversion(self, numsIndex,low,up, ans):
        if low < up:   # to check if there is more than one element.
            mid= low+ (up-low)//2
            self.merge_sort_count_inversion(numsIndex, low, mid, ans)
            self.merge_sort_count_inversion(numsIndex, mid+1, up, ans)
            self.merge(numsIndex, low, mid, up, ans)
        
    def smaller_count(self, numsIndex, low, mid, up, ans):

        j = mid + 1  # 'j' point to the 1st ele on right
        # we have to count pair for each ele on left side
        for i in range(low, mid +1):
            while j <= up and numsIndex[i][0] > numsIndex[j][0]:
                j+= 1
            ind = numsIndex[i][1]
            # just subtract the 1st index of right side to get no of element smaller than 'ind' on right.
            ans[ind] += j- (mid + 1)   # Adding the no of element smaller than index 'ind' on right.
        
    def merge(self, arr,low,mid,up, ans):
        self.smaller_count(arr, low, mid, up, ans)

        low1,up1,low2,up2= low,mid,mid+1,up
        b= []
        while low1<= up1 and low2<= up2:
            if arr[low1][0] <= arr[low2][0]:
                b.append(arr[low1])
                low1 +=1
            else:  # all ele from low1 to up1 will be greater so count= up1- low + 1
                b.append(arr[low2])
                low2 +=1

        while low1<=up1:
            b.append(arr[low1])
            low1+=1
        while low2<=up2:
            b.append(arr[low2])
            low2+=1

        j= low
        k= 0
        while j<=up:
            arr[j] = b[k]
            j+= 1
            k+= 1


# Read below solutions also later

# Method 2:

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numsIndex = [[nums[i], i] for i in range(n)]  # we need index also to update ans
        ans = [0]*n
    
        def merge_sort_count_inversion(numsIndex,low,up):
            if low < up:   # to check if there is more than one element.
                mid= low+ (up-low)//2
                merge_sort_count_inversion(numsIndex, low, mid)
                merge_sort_count_inversion(numsIndex, mid+1, up)
                merge(numsIndex, low, mid, up)
        
        def merge(arr,low,mid,up):
            low1,up1,low2,up2= low,mid,mid+1,up
            numElemsRightArrayLessThanLeftArray = 0  # will store count of ele from right array
                        # that moved to merged array 'b'.
            b= []
            while low1<= up1 and low2<= up2:
                if arr[low1][0] <= arr[low2][0]:
                    ind = arr[low1][1]
                    ans[ind] += numElemsRightArrayLessThanLeftArray
                    b.append(arr[low1])
                    low1 +=1
                else:  # all ele from low1 to up1 will be greater so count= up1- low + 1
                    numElemsRightArrayLessThanLeftArray += 1
                    b.append(arr[low2])
                    low2 +=1

            while low1<=up1:
                ind = arr[low1][1]
                ans[ind] += numElemsRightArrayLessThanLeftArray
                b.append(arr[low1])
                low1+=1
            while low2<=up2:
                b.append(arr[low2])
                low2+=1

            j= low
            k= 0
            while j<=up:
                arr[j]= b[k]
                j+= 1
                k+= 1

        merge_sort_count_inversion(numsIndex, 0, n-1)
        return ans

# My mistake:
# i was not able to optimise the merge to O(m + n).
# e.g : left-subarray: [9, 11, 15], right-subarray: [2, 5, 6] .

# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        List<int[]> numsIndex = new ArrayList<>(); // Store value and index
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            numsIndex.add(new int[]{nums[i], i});
        }

        mergeSortCountInversion(numsIndex, 0, n - 1, ans);
        return Arrays.asList(Arrays.stream(ans).boxed().toArray(Integer[]::new));
    }

    private void mergeSortCountInversion(List<int[]> numsIndex, int low, int up, int[] ans) {
        if (low < up) { // Check if more than one element exists
            int mid = low + (up - low) / 2;
            mergeSortCountInversion(numsIndex, low, mid, ans);
            mergeSortCountInversion(numsIndex, mid + 1, up, ans);
            merge(numsIndex, low, mid, up, ans);
        }
    }

    private void smallerCount(List<int[]> numsIndex, int low, int mid, int up, int[] ans) {
        int j = mid + 1; // 'j' points to the first element on the right side

        for (int i = low; i <= mid; i++) {
            while (j <= up && numsIndex.get(i)[0] > numsIndex.get(j)[0]) {
                j++;
            }
            int ind = numsIndex.get(i)[1];
            ans[ind] += j - (mid + 1); // Count elements smaller than index 'ind' on right
        }
    }

    private void merge(List<int[]> arr, int low, int mid, int up, int[] ans) {
        smallerCount(arr, low, mid, up, ans);

        int low1 = low, up1 = mid, low2 = mid + 1, up2 = up;
        List<int[]> temp = new ArrayList<>();

        while (low1 <= up1 && low2 <= up2) {
            if (arr.get(low1)[0] <= arr.get(low2)[0]) {
                temp.add(arr.get(low1));
                low1++;
            } else {
                temp.add(arr.get(low2));
                low2++;
            }
        }

        while (low1 <= up1) {
            temp.add(arr.get(low1++));
        }
        while (low2 <= up2) {
            temp.add(arr.get(low2++));
        }

        for (int i = low, k = 0; i <= up; i++, k++) {
            arr.set(i, temp.get(k));
        }
    }
}
//Method 2
import java.util.*;

class Solution {
    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        List<int[]> numsIndex = new ArrayList<>();
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            numsIndex.add(new int[]{nums[i], i}); // Storing values with indices
        }

        mergeSortCountInversion(numsIndex, 0, n - 1, ans);
        return Arrays.asList(Arrays.stream(ans).boxed().toArray(Integer[]::new));
    }

    private void mergeSortCountInversion(List<int[]> numsIndex, int low, int up, int[] ans) {
        if (low < up) { // Check if more than one element exists
            int mid = low + (up - low) / 2;
            mergeSortCountInversion(numsIndex, low, mid, ans);
            mergeSortCountInversion(numsIndex, mid + 1, up, ans);
            merge(numsIndex, low, mid, up, ans);
        }
    }

    private void merge(List<int[]> arr, int low, int mid, int up, int[] ans) {
        int low1 = low, up1 = mid, low2 = mid + 1, up2 = up;
        int numElemsRightArrayLessThanLeftArray = 0; // Tracks count of smaller elements in right array
        List<int[]> temp = new ArrayList<>();

        while (low1 <= up1 && low2 <= up2) {
            if (arr.get(low1)[0] <= arr.get(low2)[0]) {
                int ind = arr.get(low1)[1];
                ans[ind] += numElemsRightArrayLessThanLeftArray;
                temp.add(arr.get(low1));
                low1++;
            } else {
                numElemsRightArrayLessThanLeftArray++;
                temp.add(arr.get(low2));
                low2++;
            }
        }

        while (low1 <= up1) {
            int ind = arr.get(low1)[1];
            ans[ind] += numElemsRightArrayLessThanLeftArray;
            temp.add(arr.get(low1++));
        }

        while (low2 <= up2) {
            temp.add(arr.get(low2++));
        }

        for (int i = low, k = 0; i <= up; i++, k++) {
            arr.set(i, temp.get(k));
        }
    }
}
"""

# C++ Code 
"""
//Method 1
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<pair<int, int>> numsIndex; // Store value and index
        vector<int> ans(n, 0);

        for (int i = 0; i < n; i++) {
            numsIndex.push_back({nums[i], i});
        }

        mergeSortCountInversion(numsIndex, 0, n - 1, ans);
        return ans;
    }

private:
    void mergeSortCountInversion(vector<pair<int, int>>& numsIndex, int low, int up, vector<int>& ans) {
        if (low < up) { // Check if more than one element exists
            int mid = low + (up - low) / 2;
            mergeSortCountInversion(numsIndex, low, mid, ans);
            mergeSortCountInversion(numsIndex, mid + 1, up, ans);
            merge(numsIndex, low, mid, up, ans);
        }
    }

    void smallerCount(vector<pair<int, int>>& numsIndex, int low, int mid, int up, vector<int>& ans) {
        int j = mid + 1; // 'j' points to the first element on the right side

        for (int i = low; i <= mid; i++) {
            while (j <= up && numsIndex[i].first > numsIndex[j].first) {
                j++;
            }
            int ind = numsIndex[i].second;
            ans[ind] += j - (mid + 1); // Count elements smaller than index 'ind' on right
        }
    }

    void merge(vector<pair<int, int>>& arr, int low, int mid, int up, vector<int>& ans) {
        smallerCount(arr, low, mid, up, ans);

        int low1 = low, up1 = mid, low2 = mid + 1, up2 = up;
        vector<pair<int, int>> temp;

        while (low1 <= up1 && low2 <= up2) {
            if (arr[low1].first <= arr[low2].first) {
                temp.push_back(arr[low1]);
                low1++;
            } else {
                temp.push_back(arr[low2]);
                low2++;
            }
        }

        while (low1 <= up1) {
            temp.push_back(arr[low1++]);
        }
        while (low2 <= up2) {
            temp.push_back(arr[low2++]);
        }

        for (int i = low, k = 0; i <= up; i++, k++) {
            arr[i] = temp[k];
        }
    }
};
//Method 2

#include <vector>

using namespace std;

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<pair<int, int>> numsIndex;
        vector<int> ans(n, 0);

        for (int i = 0; i < n; i++) {
            numsIndex.emplace_back(nums[i], i); // Storing values with indices
        }

        mergeSortCountInversion(numsIndex, 0, n - 1, ans);
        return ans;
    }

private:
    void mergeSortCountInversion(vector<pair<int, int>>& numsIndex, int low, int up, vector<int>& ans) {
        if (low < up) { // Check if more than one element exists
            int mid = low + (up - low) / 2;
            mergeSortCountInversion(numsIndex, low, mid, ans);
            mergeSortCountInversion(numsIndex, mid + 1, up, ans);
            merge(numsIndex, low, mid, up, ans);
        }
    }

    void merge(vector<pair<int, int>>& arr, int low, int mid, int up, vector<int>& ans) {
        int low1 = low, up1 = mid, low2 = mid + 1, up2 = up;
        int numElemsRightArrayLessThanLeftArray = 0; // Tracks count of smaller elements in right array
        vector<pair<int, int>> temp;

        while (low1 <= up1 && low2 <= up2) {
            if (arr[low1].first <= arr[low2].first) {
                int ind = arr[low1].second;
                ans[ind] += numElemsRightArrayLessThanLeftArray;
                temp.push_back(arr[low1]);
                low1++;
            } else {
                numElemsRightArrayLessThanLeftArray++;
                temp.push_back(arr[low2]);
                low2++;
            }
        }

        while (low1 <= up1) {
            int ind = arr[low1].second;
            ans[ind] += numElemsRightArrayLessThanLeftArray;
            temp.push_back(arr[low1++]);
        }

        while (low2 <= up2) {
            temp.push_back(arr[low2++]);
        }

        for (int i = low, k = 0; i <= up; i++, k++) {
            arr[i] = temp[k];
        }
    }
};
"""

# Very nicee explanation
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/solutions/445769/merge-sort-clear-simple-explanation-with-examples-o-n-lg-n/


# Later do by segment tree, BST, and BIT