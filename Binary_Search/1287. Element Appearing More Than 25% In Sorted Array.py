# logic: traverse the array and we will find same ele at 'i+ n//4' index means that is our ans.
# since array is sorted so all will be continous only.

# time: O(n)
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n= len(arr)
        t= n//4
        for i in range(n-t):
            if arr[i]== arr[i + t]:
                return arr[i]
            

# method 2:
# our ans must be at any of the three index i.e at i) 'n//4': if 1st index of ans is at <= n//4
# or ii) '2*n//4' : if 1st index of ans is at <= 2*n//4 or iii) '3*n//4': if 1st index of ans is at <= 3*n//4
# So just find the first index of these ele and compare with '+ n//4' if equal then that will be our ans.
# time: O(3*logn)

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n= len(arr)
        for i in range(1, 4):
            indx= int((i* n/4 ))
            start= bisect.bisect_left(arr, arr[indx])
            if arr[start]== arr[start + n//4]:
                return arr[start]

# Method 3: 
# Just above logic only .
# Check 1st two possibility if our ans is not from 1st two then our ans = (3*n//4)
# time: O(2*logn)
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n= len(arr)
        for i in range(1, 3):
            indx= int((i* n/4 ))
            start= bisect.bisect_left(arr, arr[indx])
            if arr[start]== arr[start + n//4]:
                return arr[start]
        return arr[int(3*n//4)]    # if neither ele at 'n//4' or '2*n//4' is our ans then this will be our ans for sure.

# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    public int findSpecialInteger(int[] arr) {
        int n = arr.length;
        int t = n / 4;

        for (int i = 0; i < n - t; i++) {
            if (arr[i] == arr[i + t]) {
                return arr[i];
            }
        }
        return -1;
    }
}
//Method 2
import java.util.*;

class Solution {
    public int findSpecialInteger(int[] arr) {
        int n = arr.length;

        for (int i = 1; i < 4; i++) {
            int indx = (i * n / 4);
            int start = Arrays.binarySearch(arr, arr[indx]);

            if (start >= 0 && start + n / 4 < n && arr[start] == arr[start + n / 4]) {
                return arr[start];
            }
        }
        return -1;
    }
}
//Method 3
class Solution {
    public int findSpecialInteger(int[] arr) {
        int n = arr.length;

        for (int i = 1; i < 3; i++) {
            int indx = (i * n / 4);
            int start = Arrays.binarySearch(arr, arr[indx]);

            if (start >= 0 && start + n / 4 < n && arr[start] == arr[start + n / 4]) {
                return arr[start];
            }
        }
        return arr[(3 * n / 4)];
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
    int findSpecialInteger(vector<int>& arr) {
        int n = arr.size();
        int t = n / 4;

        for (int i = 0; i < n - t; i++) {
            if (arr[i] == arr[i + t]) {
                return arr[i];
            }
        }
        return -1;
    }
};
//Method 2
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int n = arr.size();

        for (int i = 1; i < 4; i++) {
            int indx = int((i * n / 4));
            auto start = lower_bound(arr.begin(), arr.end(), arr[indx]);

            if (start != arr.end() && (start + n / 4) < arr.end() && *start == *(start + n / 4)) {
                return *start;
            }
        }
        return -1;
    }
};
//Method 3
class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int n = arr.size();

        for (int i = 1; i < 3; i++) {
            int indx = int((i * n / 4));
            auto start = lower_bound(arr.begin(), arr.end(), arr[indx]);

            if (start != arr.end() && (start + n / 4) < arr.end() && *start == *(start + n / 4)) {
                return *start;
            }
        }
        return arr[int(3 * n / 4)];
    }
};
"""