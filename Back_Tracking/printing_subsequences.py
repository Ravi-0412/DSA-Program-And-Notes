# Method 1: 

# subsequences is same as subset except subset doesn't maintain the relative order
# but for subset also ans will be same only as (1,3) and (3,1) can't be in the subset as same time
# because subset doesn't allow duplicates
# subset: basically means taking any no of elements in any order

# time complexity= O(2^n *n), 2^n; total no of subsequences and for each we traversing nearly the whole array
# space complexity= O(n), maximum recursion depth
# expanation in note, page no: 24

# this will print alll subset inside a list separately
# all subsequence are subset but reverse is not true
def PrintSubsequence(ind,arr,ans,n):
    if ind>= n:  # means we have found one of the ans.
        print(ans)
        return
    # if we include the current ele
    ans.append(arr[ind])
    PrintSubsequence(ind+1,arr,ans,n)

    # if we don't include the current ele then,we have to first remove the current ele
    #  as we have already added above and then call the function for next index
    ans.pop()
    PrintSubsequence(ind+1,arr,ans,n)

arr= [1,2,3]
ans= []
print("possible subsequences or subset is: ")
PrintSubsequence(0,arr,ans,3)

# Java Code 
"""
import java.util.*;

public class Solution {

    public static void printSubsequence(int ind, int[] arr, List<Integer> ans, int n) {
        if (ind >= n) {  // means we have found one of the ans.
            System.out.println(ans);
            return;
        }

        // if we include the current ele
        ans.add(arr[ind]);
        printSubsequence(ind + 1, arr, ans, n);

        // if we don't include the current ele then,we have to first remove the current ele
        // as we have already added above and then call the function for next index
        ans.remove(ans.size() - 1);
        printSubsequence(ind + 1, arr, ans, n);
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3};
        List<Integer> ans = new ArrayList<>();
        System.out.println("possible subsequences or subset is: ");
        printSubsequence(0, arr, ans, 3);
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
using namespace std;

void printSubsequence(int ind, vector<int>& arr, vector<int>& ans, int n) {
    if (ind >= n) {  // means we have found one of the ans.
        for (int num : ans) cout << num << " ";
        cout << endl;
        return;
    }

    // if we include the current ele
    ans.push_back(arr[ind]);
    printSubsequence(ind + 1, arr, ans, n);

    // if we don't include the current ele then,we have to first remove the current ele
    // as we have already added above and then call the function for next index
    ans.pop_back();
    printSubsequence(ind + 1, arr, ans, n);
}

int main() {
    vector<int> arr = {1, 2, 3};
    vector<int> ans;
    cout << "possible subsequences or subset is: " << endl;
    printSubsequence(0, arr, ans, 3);
    return 0;
}
"""
# Method 2: 
# here we are modifying the 'ans' array using '+' that's why no need to pop() like above one. (just same as string).
# Note: modifying array by '+' doesn't change the curr array, just change the array in calling function position just like 
# we do 'append' and 'pop' while traversing back.

# if you modify by append then you have to pop first then call the fn otherwise, you will get incorrect ans.

def PrintSubsequence1(ind,arr,ans,n):
    if ind>= n:
        print(ans)
        return
    # if we include the current ele, then add arr[ind] into the ans
    
    # PrintSubsequence1(ind+1,arr,ans.append(arr[ind]),n)    # will give error as it will return the value of append which is None
    PrintSubsequence1(ind+1,arr,ans+ [arr[ind]],n)
    # if we don't include the current ele 
    PrintSubsequence1(ind+1,arr,ans,n)

arr= [1,2,3]
ans= []
# print("possible subsequences or subset is: ")
# PrintSubsequence1(0,arr,ans,3)

# Java Code 
"""
import java.util.*;

public class Solution {

    public static void printSubsequence(int ind, int[] arr, List<Integer> ans, int n) {
        if (ind >= n) {
            System.out.println(ans);
            return;
        }

        // if we include the current ele, then add arr[ind] into the ans
        List<Integer> included = new ArrayList<>(ans);
        included.add(arr[ind]);
        printSubsequence(ind + 1, arr, included, n);

        // if we don't include the current ele
        printSubsequence(ind + 1, arr, ans, n);
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3};
        List<Integer> ans = new ArrayList<>();
        printSubsequence(0, arr, ans, 3);
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
using namespace std;

void printSubsequence(int ind, const vector<int>& arr, vector<int> ans, int n) {
    if (ind >= n) {
        for (int val : ans) cout << val << " ";
        cout << endl;
        return;
    }

    // if we include the current ele, then add arr[ind] into the ans
    vector<int> included = ans;
    included.push_back(arr[ind]);
    printSubsequence(ind + 1, arr, included, n);

    // if we don't include the current ele
    printSubsequence(ind + 1, arr, ans, n);
}

int main() {
    vector<int> arr = {1, 2, 3};
    vector<int> ans;
    printSubsequence(0, arr, ans, 3);
    return 0;
}
"""

# Method 3: 
# another way of writing the Method 3
def PrintSubsequence2(arr,ans):
    if not arr:
        print(ans)
        return
    # if we include the current ele, then add arr[ind] into the ans
    PrintSubsequence2(arr[1:],ans+ [arr[0]])
    # if we don't include the current ele 
    PrintSubsequence2(arr[1:],ans)

arr= [1,2,1]
# print("possible subsequences or subset is: ")
# PrintSubsequence2(arr,[])

# Java Code 
"""
import java.util.*;

public class SubsequencePrinter {

    // if we include the current ele, then add arr[ind] into the ans
    // if we don't include the current ele 
    public static void PrintSubsequence2(int[] arr, List<Integer> ans, int index) {
        if (index == arr.length) {
            System.out.println(ans);
            return;
        }

        List<Integer> newList = new ArrayList<>(ans);
        newList.add(arr[index]);
        PrintSubsequence2(arr, newList, index + 1);  // include

        PrintSubsequence2(arr, ans, index + 1);      // exclude
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 1};
        // print("possible subsequences or subset is: ")
        // PrintSubsequence2(arr, [])
        PrintSubsequence2(arr, new ArrayList<>(), 0);
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
using namespace std;

void printSubsequences(vector<int> arr, vector<int> ans) {
    if (arr.empty()) {
        // print(ans)
        cout << "[";
        for (size_t i = 0; i < ans.size(); ++i) {
            cout << ans[i];
            if (i + 1 < ans.size()) cout << ", ";
        }
        cout << "]" << endl;
        return;
    }

    // if we include the current ele, then add arr[ind] into the ans
    vector<int> include = ans;
    include.push_back(arr[0]);
    vector<int> next(arr.begin() + 1, arr.end());
    printSubsequences(next, include);

    // if we don't include the current ele
    printSubsequences(next, ans);
}

int main() {
    vector<int> arr = {1, 2, 1};
    vector<int> ans;
    printSubsequences(arr, ans);
}
"""

# Extension: 

# Note vvi: This method is very very useful and widely used.
# A lot of problems can be solved easily using above method only.

# Where to use this?
# Ans: when you have to get the ans with the numbers(all or some) given in Q or their combinations in our ans then we can use this logic.
# I.e when our given array/string will become empty(means we have used all the numbers) then, we will get one of the ans.

# Some Q where we can use this : "78. Subsets", "17. Letter Combinations of a Phone Number", "No of ways to get  sum '4' from a dice ". 