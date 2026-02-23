# Method 1: 

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
# Java Code 
"""
import java.util.*;

class Solution {
    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        int[][] numsIndex = new int[n][2];  // we need index also to update ans
        for (int i = 0; i < n; i++) {
            numsIndex[i][0] = nums[i];
            numsIndex[i][1] = i;
        }
        Integer[] ans = new Integer[n];
        Arrays.fill(ans, 0);
        merge_sort_count_inversion(numsIndex, 0, n - 1, ans);
        return Arrays.asList(ans);
    }

    private void merge_sort_count_inversion(int[][] numsIndex, int low, int up, Integer[] ans) {
        if (low < up) {  // to check if there is more than one element.
            int mid = low + (up - low) / 2;
            merge_sort_count_inversion(numsIndex, low, mid, ans);
            merge_sort_count_inversion(numsIndex, mid + 1, up, ans);
            merge(numsIndex, low, mid, up, ans);
        }
    }

    private void smaller_count(int[][] numsIndex, int low, int mid, int up, Integer[] ans) {
        int j = mid + 1;  // 'j' point to the 1st ele on right
        // we have to count pair for each ele on left side
        for (int i = low; i <= mid; i++) {
            while (j <= up && numsIndex[i][0] > numsIndex[j][0]) {
                j++;
            }
            int ind = numsIndex[i][1];
            // just subtract the 1st index of right side to get no of element smaller than 'ind' on right.
            ans[ind] += j - (mid + 1);  // Adding the no of element smaller than index 'ind' on right.
        }
    }

    private void merge(int[][] arr, int low, int mid, int up, Integer[] ans) {
        smaller_count(arr, low, mid, up, ans);

        int low1 = low, up1 = mid, low2 = mid + 1, up2 = up;
        List<int[]> b = new ArrayList<>();

        while (low1 <= up1 && low2 <= up2) {
            if (arr[low1][0] <= arr[low2][0]) {
                b.add(arr[low1]);
                low1++;
            } else {
                b.add(arr[low2]);
                low2++;
            }
        }

        while (low1 <= up1) {
            b.add(arr[low1]);
            low1++;
        }
        while (low2 <= up2) {
            b.add(arr[low2]);
            low2++;
        }

        for (int j = low, k = 0; j <= up; j++, k++) {
            arr[j] = b.get(k);
        }
    }
}

"""

# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<pair<int, int>> numsIndex(n);  // we need index also to update ans
        for (int i = 0; i < n; ++i) {
            numsIndex[i] = {nums[i], i};
        }
        vector<int> ans(n, 0);
        merge_sort_count_inversion(numsIndex, 0, n - 1, ans);
        return ans;
    }

private:
    void merge_sort_count_inversion(vector<pair<int, int>>& numsIndex, int low, int up, vector<int>& ans) {
        if (low < up) {  // to check if there is more than one element.
            int mid = low + (up - low) / 2;
            merge_sort_count_inversion(numsIndex, low, mid, ans);
            merge_sort_count_inversion(numsIndex, mid + 1, up, ans);
            merge(numsIndex, low, mid, up, ans);
        }
    }

    void smaller_count(vector<pair<int, int>>& numsIndex, int low, int mid, int up, vector<int>& ans) {
        int j = mid + 1;  // 'j' point to the 1st ele on right
        // we have to count pair for each ele on left side
        for (int i = low; i <= mid; ++i) {
            while (j <= up && numsIndex[i].first > numsIndex[j].first) {
                ++j;
            }
            int ind = numsIndex[i].second;
            // just subtract the 1st index of right side to get no of element smaller than 'ind' on right.
            ans[ind] += j - (mid + 1);  // Adding the no of element smaller than index 'ind' on right.
        }
    }

    void merge(vector<pair<int, int>>& arr, int low, int mid, int up, vector<int>& ans) {
        smaller_count(arr, low, mid, up, ans);

        int low1 = low, up1 = mid, low2 = mid + 1, up2 = up;
        vector<pair<int, int>> b;

        while (low1 <= up1 && low2 <= up2) {
            if (arr[low1].first <= arr[low2].first) {
                b.push_back(arr[low1++]);
            } else {
                b.push_back(arr[low2++]);
            }
        }

        while (low1 <= up1) {
            b.push_back(arr[low1++]);
        }
        while (low2 <= up2) {
            b.push_back(arr[low2++]);
        }

        for (int j = low, k = 0; j <= up; ++j, ++k) {
            arr[j] = b[k];
        }
    }
};

"""

# Method 2:
# best one 

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
                    ans[ind] += numElemsRightArrayLessThanLeftArray  # is 'ind' ke liye itna hi element answer me ho sakta h max. 
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

# Java Code 
"""
import java.util.*;

class Solution {
    private int[] ans;

    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        int[][] numsIndex = new int[n][2];  // we need index also to update ans
        ans = new int[n];

        for (int i = 0; i < n; i++) {
            numsIndex[i][0] = nums[i];
            numsIndex[i][1] = i;
        }

        merge_sort_count_inversion(numsIndex, 0, n - 1);
        return Arrays.stream(ans).boxed().toList();
    }

    private void merge_sort_count_inversion(int[][] numsIndex, int low, int up) {
        if (low < up) {  // to check if there is more than one element.
            int mid = low + (up - low) / 2;
            merge_sort_count_inversion(numsIndex, low, mid);
            merge_sort_count_inversion(numsIndex, mid + 1, up);
            merge(numsIndex, low, mid, up);
        }
    }

    private void merge(int[][] arr, int low, int mid, int up) {
        int low1 = low, up1 = mid, low2 = mid + 1, up2 = up;
        int numElemsRightArrayLessThanLeftArray = 0;  // will store count of ele from right array
                                                      // that moved to merged array 'b'.
        List<int[]> b = new ArrayList<>();

        while (low1 <= up1 && low2 <= up2) {
            if (arr[low1][0] <= arr[low2][0]) {
                int ind = arr[low1][1];
                ans[ind] += numElemsRightArrayLessThanLeftArray;
                b.add(arr[low1]);
                low1++;
            } else {
                numElemsRightArrayLessThanLeftArray++;
                b.add(arr[low2]);
                low2++;
            }
        }

        while (low1 <= up1) {
            int ind = arr[low1][1];
            ans[ind] += numElemsRightArrayLessThanLeftArray;
            b.add(arr[low1]);
            low1++;
        }

        while (low2 <= up2) {
            b.add(arr[low2]);
            low2++;
        }

        for (int j = low, k = 0; j <= up; j++, k++) {
            arr[j] = b.get(k);
        }
    }
}

"""

# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
private:
    vector<int> ans;

public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<pair<int, int>> numsIndex(n);  // we need index also to update ans
        ans.assign(n, 0);

        for (int i = 0; i < n; ++i) {
            numsIndex[i] = {nums[i], i};
        }

        merge_sort_count_inversion(numsIndex, 0, n - 1);
        return ans;
    }

private:
    void merge_sort_count_inversion(vector<pair<int, int>>& numsIndex, int low, int up) {
        if (low < up) {  // to check if there is more than one element.
            int mid = low + (up - low) / 2;
            merge_sort_count_inversion(numsIndex, low, mid);
            merge_sort_count_inversion(numsIndex, mid + 1, up);
            merge(numsIndex, low, mid, up);
        }
    }

    void merge(vector<pair<int, int>>& arr, int low, int mid, int up) {
        int low1 = low, up1 = mid, low2 = mid + 1, up2 = up;
        int numElemsRightArrayLessThanLeftArray = 0;  // will store count of ele from right array
                                                      // that moved to merged array 'b'.
        vector<pair<int, int>> b;

        while (low1 <= up1 && low2 <= up2) {
            if (arr[low1].first <= arr[low2].first) {
                int ind = arr[low1].second;
                ans[ind] += numElemsRightArrayLessThanLeftArray;
                b.push_back(arr[low1++]);
            } else {
                numElemsRightArrayLessThanLeftArray++;
                b.push_back(arr[low2++]);
            }
        }

        while (low1 <= up1) {
            int ind = arr[low1].second;
            ans[ind] += numElemsRightArrayLessThanLeftArray;
            b.push_back(arr[low1++]);
        }

        while (low2 <= up2) {
            b.push_back(arr[low2++]);
        }

        for (int j = low, k = 0; j <= up; ++j, ++k) {
            arr[j] = b[k];
        }
    }
};

"""
