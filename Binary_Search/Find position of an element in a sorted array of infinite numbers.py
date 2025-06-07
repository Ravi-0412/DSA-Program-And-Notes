# since we dont know the size so using binary search after finding length is not a good approach.
# but if we can find that target ele exist bw any two index
# then we can apply binary search bw those index.
# so,now problem reduces to find the range in which the target ele exist
# for finding the range we can move in chunk like first size of 2
# then 4, then 8 ....

import math
def FindRange(arr,target):
    i= 0
    while arr[2**(i+1)] < target: # means target not lie in this range
                             # so now incr the range in pow of tw
        i+= 1
    # when while loop will fail means we have found the range
    # so now apply binary search in this range to find the position
    position= BinarySearch(arr, target, 2**i -1, 2**(i+1))   # start= 2**i -1 to handle the case when ele is present at zero index.
    return position

def BinarySearch(arr,key,start,end):
    low= start
    up= end
    while low<= up:
        mid= (low+up)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            up = mid-1
        else:
            low= mid+1
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
print(FindRange(arr,5))


# Similar Q:
# 1) Find the index of first 1 in an infinite sorted array of 0s and 1s

# Java Code 
"""
import java.util.*;

class Solution {
    private int binarySearch(int[] arr, int key, int start, int end) {
        int low = start, up = end;
        while (low <= up) {
            int mid = (low + up) / 2;
            if (arr[mid] == key) {
                return mid;
            } else if (arr[mid] > key) {
                up = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }

    public int findRange(int[] arr, int target) {
        int i = 0;
        while (Math.pow(2, i + 1) < arr.length && arr[(int)Math.pow(2, i + 1)] < target) {
            i++;
        }
        int start = (int)Math.pow(2, i) - 1;
        int end = Math.min((int)Math.pow(2, i + 1), arr.length - 1);
        return binarySearch(arr, target, start, end);
    }

    public static void main(String[] args) {
        int[] arr = {3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170};
        Solution sol = new Solution();
        System.out.println(sol.findRange(arr, 5));
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
            if (arr[mid] == key) {
                return mid;
            } else if (arr[mid] > key) {
                up = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }

    int findRange(vector<int>& arr, int target) {
        int i = 0;
        while (pow(2, i + 1) < arr.size() && arr[pow(2, i + 1)] < target) {
            i++;
        }
        int start = pow(2, i) - 1;
        int end = min((int)pow(2, i + 1), (int)arr.size() - 1);
        return binarySearch(arr, target, start, end);
    }
};

int main() {
    vector<int> arr = {3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170};
    Solution sol;
    cout << sol.findRange(arr, 5) << endl;
    return 0;
}
"""
