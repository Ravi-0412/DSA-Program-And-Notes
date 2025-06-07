# Logic : 1st find the range in whcih '1' lies
# Then find the position of 1st one in that range.

def FindIndex(arr):
    i= 0
    while(arr[2**(i+1)]< 1): # means target not lie in this range
                             # so now incr the range in pow of tw
        i+= 1
    # when while loop will fail means we have found the range
    # so now apply binary search in this range to find the position
    position= BinarySearch(arr, 1, 2**i -1, 2**(i+1))   # start= 2**i -1 to handle the case when ele is present at zero index.
    return position


def BinarySearch(arr,key,start,end):
    low, up= start, end
    while low<= up:
        mid= (low+up)//2
        if arr[mid]>= key:
            up= mid-1
        else:
            low= mid+1
    return low

arr = [0, 0, 0, 0, 0,0,1,1,1,1]
arr=  [1, 1, 1, 1, 1, 1]
print(FindIndex(arr))
    

# Java Code 
"""
import java.util.*;

class Solution {
    private int binarySearch(int[] arr, int key, int start, int end) {
        int low = start, up = end;
        while (low <= up) {
            int mid = (low + up) / 2;
            if (arr[mid] >= key) {
                up = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    public int findIndex(int[] arr) {
        int i = 0;
        while (Math.pow(2, i + 1) < arr.length && arr[(int)Math.pow(2, i + 1)] < 1) {
            i++;
        }
        int start = (int)Math.pow(2, i) - 1;
        int end = Math.min((int)Math.pow(2, i + 1), arr.length - 1);
        return binarySearch(arr, 1, start, end);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] arr1 = {0, 0, 0, 0, 0, 0, 1, 1, 1, 1};
        System.out.println(sol.findIndex(arr1));

        int[] arr2 = {1, 1, 1, 1, 1, 1};
        System.out.println(sol.findIndex(arr2));
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int binarySearch(vector<int>& arr, int key, int start, int end) {
        int low = start, up = end;
        while (low <= up) {
            int mid = (low + up) / 2;
            if (arr[mid] >= key) {
                up = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    int findIndex(vector<int>& arr) {
        int i = 0;
        while (pow(2, i + 1) < arr.size() && arr[pow(2, i + 1)] < 1) {
            i++;
        }
        int start = pow(2, i) - 1;
        int end = min((int)pow(2, i + 1), (int)arr.size() - 1);
        return binarySearch(arr, 1, start, end);
    }
};

int main() {
    vector<int> arr = {0, 0, 0, 0, 0, 0, 1, 1, 1, 1};
    Solution sol;
    cout << sol.findIndex(arr) << endl;

    vector<int> arr2 = {1, 1, 1, 1, 1, 1};
    cout << sol.findIndex(arr2) << endl;
    
    return 0;
}
"""