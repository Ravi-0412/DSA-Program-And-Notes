# Method 1: 
# very simple and easy. Just same as we do on pen and paper by taking choices for each boxes.
# logic: hmko 'len(arr)' no of boxes fill karna jo array me h wahi sb ele se.
#  remaining position ke liye koi bhi ele le sakte h and kisi ele ko choose karne ke bad
# usko aage nhi le sakte remaining boxes ko fill karne ke liye.
# isi tarah mera smaller subproblem generate hoga.

# in short vvi: At any time remaining position to fill will be equal to len(arr) and
# we can fill those positions one by one using elements of array.

# time: O(n! * n)  # n! = no of permutation and n= copying each permuatation
# space: n!

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans= []
        def permutation(arr, per):
            if not arr: 
                # means we have found the ans. Filled all the req places.
                ans.append(per)
                return
            # we can choose any number to fill the next position from remaining arr
            for i in range(len(arr)):  
                # us ele ko lene ke bad usko aage me include nhi kar sakte. so removing the added ele from arr and adding that to our one of permutation.
                permutation(arr[: i] + arr[i+1: ], per + [arr[i]])   
        
        permutation(nums, [])
        return ans

# Java Code 
"""
import java.util.*;

public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        permutation(nums, new ArrayList<>(), ans);
        return ans;
    }

    public void permutation(int[] arr, List<Integer> per, List<List<Integer>> ans) {
        if (per.size() == arr.length) {
            // means we have found the ans. Filled all the req places.
            ans.add(new ArrayList<>(per));
            return;
        }

        // we can choose any number to fill the next position from remaining arr
        for (int i = 0; i < arr.length; i++) {
            if (per.contains(arr[i])) continue;  // us ele ko lene ke bad usko aage me include nhi kar sakte
            per.add(arr[i]);  // adding that to our one of permutation
            permutation(arr, per, ans);
            per.remove(per.size() - 1);  // backtracking
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {1, 2, 3};
        System.out.println(sol.permute(nums));
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
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> per;
        vector<bool> used(nums.size(), false);
        permutation(nums, per, used, ans);
        return ans;
    }

    void permutation(vector<int>& arr, vector<int>& per, vector<bool>& used, vector<vector<int>>& ans) {
        if (per.size() == arr.size()) {
            // means we have found the ans. Filled all the req places.
            ans.push_back(per);
            return;
        }

        // we can choose any number to fill the next position from remaining arr
        for (int i = 0; i < arr.size(); i++) {
            if (used[i]) continue;  // us ele ko lene ke bad usko aage me include nhi kar sakte
            used[i] = true;
            per.push_back(arr[i]);  // adding that to our one of permutation
            permutation(arr, per, used, ans);
            per.pop_back();  // backtracking
            used[i] = false;
        }
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = sol.permute(nums);

    for (const auto& v : result) {
        cout << "[";
        for (size_t i = 0; i < v.size(); ++i) {
            cout << v[i];
            if (i + 1 < v.size()) cout << ", ";
        }
        cout << "]\n";
    }
}
"""
# Method 2: 
# To avoid copying the array after excluding the current included ele we can use set to check whether that has been added to 'per' or not.
# trying to fill remaining with all the ele if that ele is not used yet in that permutation.
# Since only distinct ele it will work fine when we will check the ele value.

# This is the most optimised among all because all other methods involve slicing.

# Not evvi: This logic will help in avoiding duplicate also i.e Q: "47. Permutations II".


# My initial misatke

# Note vvi: Pushing and poping in separate line in 'per' is making ans = []
# Reason: removing element from 'per' while backtrack is also removing ele from 'ans' and finally
# answer is getting = [].

# note vvi: 1) So avoid adding / poping in separate line in python specially with lists.
# Just add while calling function, it will get automatically get poped while backtrack and won't modify any related data structure.

# 2) or while adding into ans , add copy to avoid this scenario.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def permutation(per):
            if len(per) == len(nums):
                # ans.append(per)   # this will give empty ans
                ans.append(per.copy())   # this will give correct ans
                return
            for i in range(len(nums)):
                if nums[i] not in included:
                    included.add(nums[i])   
                    per.append(nums[i])   # this one 
                    permutation(per)
                    # while backtracking remove arr[i]
                    included.remove(nums[i])   # and this one
                    per.remove(nums[i])    

        n = len(nums)   
        ans = []
        included = set()
        permutation([])
        return ans
    
# Correct code 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def permutation(per):
            if len(per) == len(nums):
                ans.append(per)
                return
            for i in range(len(nums)):
                if nums[i] not in included:
                    included.add(nums[i])
                    permutation(per + [nums[i]])
                    included.remove(nums[i]) 

        n = len(nums)   
        ans = []
        included = set()
        permutation([])
        return ans

# Java Code 
"""
import java.util.*;

public class Solution {

    List<List<Integer>> ans = new ArrayList<>();
    Set<Integer> included = new HashSet<>();
    int[] nums;

    public List<List<Integer>> permute(int[] nums) {
        this.nums = nums;
        permutation(new ArrayList<>());
        return ans;
    }

    public void permutation(List<Integer> per) {
        if (per.size() == nums.length) {
            // ans.add(per);   // this will give shallow copy issues
            ans.add(new ArrayList<>(per));   // this will give correct ans
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (!included.contains(nums[i])) {
                included.add(nums[i]);
                per.add(nums[i]);   // this one
                permutation(per);
                // while backtracking remove arr[i]
                included.remove(nums[i]);   // and this one
                per.remove(per.size() - 1);
            }
        }
    }
}
"""
# C++ Code 
"""
import java.util.*;

public class Solution {

    List<List<Integer>> ans = new ArrayList<>();
    Set<Integer> included = new HashSet<>();
    int[] nums;

    public List<List<Integer>> permute(int[] nums) {
        this.nums = nums;
        permutation(new ArrayList<>());
        return ans;
    }

    public void permutation(List<Integer> per) {
        if (per.size() == nums.length) {
            ans.add(per);  // safe here since per is new in each call
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (!included.contains(nums[i])) {
                included.add(nums[i]);
                List<Integer> newPer = new ArrayList<>(per);
                newPer.add(nums[i]);
                permutation(newPer);
                included.remove(nums[i]);
            }
        }
    }
}
"""

# method 3:

# logic: just we are putting the upcoming letter(1st letter in remaining array) at all the gap formed by
# the already stored letter in answer.
# if there is say 'n' letter in ans then there will be 'n+1' gaps to fill the upcoming letter.
# and 1st gap will start from before zero itself and last gap will be at last.

# time and space same as above

# this will not remove duplicates as we are not checking 
# anything before filling we are just filling all the possible gaps

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def permutation(given , per):
            if not given: # if given string is empty 
                ans.append(per)
                return
            ch = given[0]   # upcoming char i.e 1st letter of remaining array
            # run a loop to call function again and again to put at diff positions
            for i in range(len(per)+1):    # filling the cur ele at 'i'th space.
                left = per[0:i]           # after this substring will put the 'ch'
                right = per[i:]           # and before this
                # after putting that char at one possible gap, call the function to fill the next char at new available position
                permutation(given[1:], left + [ch] + right)

        ans = []
        permutation(nums, [])
        return ans

# Java Code 
"""
import java.util.*;

public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        permutation(toList(nums), new ArrayList<>(), ans);
        return ans;
    }

    public void permutation(List<Integer> given, List<Integer> per, List<List<Integer>> ans) {
        if (given.isEmpty()) { // if given string is empty
            ans.add(new ArrayList<>(per));
            return;
        }

        int ch = given.get(0);   // upcoming char i.e 1st letter of remaining array

        // run a loop to call function again and again to put at diff positions
        for (int i = 0; i <= per.size(); i++) {    // filling the cur ele at 'i'th space
            List<Integer> left = new ArrayList<>(per.subList(0, i));  // after this substring will put the 'ch'
            List<Integer> right = new ArrayList<>(per.subList(i, per.size()));  // and before this

            List<Integer> combined = new ArrayList<>();
            combined.addAll(left);
            combined.add(ch);
            combined.addAll(right);

            // after putting that char at one possible gap, call the function to fill the next char at new available position
            permutation(given.subList(1, given.size()), combined, ans);
        }
    }

    private List<Integer> toList(int[] nums) {
        List<Integer> list = new ArrayList<>();
        for (int n : nums) list.add(n);
        return list;
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
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> given = nums;
        permutation(given, {}, ans);
        return ans;
    }

    void permutation(vector<int> given, vector<int> per, vector<vector<int>>& ans) {
        if (given.empty()) { // if given string is empty
            ans.push_back(per);
            return;
        }

        int ch = given[0];  // upcoming char i.e 1st letter of remaining array
        given.erase(given.begin());

        // run a loop to call function again and again to put at diff positions
        for (int i = 0; i <= per.size(); ++i) { // filling the cur ele at 'i'th space
            vector<int> left(per.begin(), per.begin() + i);   // after this substring will put the 'ch'
            vector<int> right(per.begin() + i, per.end());    // and before this

            vector<int> combined;
            combined.insert(combined.end(), left.begin(), left.end());
            combined.push_back(ch);
            combined.insert(combined.end(), right.begin(), right.end());

            // after putting that char at one possible gap, call the function to fill the next char at new available position
            permutation(given, combined, ans);
        }
    }
};
"""

# Method 4: 
# taking the ans list inside the function only.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums,[])
        
    def helper(self, nums, per):   
        ans= []
        if not nums:
            ans.append(per)
            return ans
        ch= [nums[0]]    
        for i in range(len(per)+1):
            left,right= per[:i], per[i:]
            ans += self.helper(nums[1:], left + ch+ right)   
        return ans

# Java Code 
"""
import java.util.*;

public class Solution {

    public List<List<Integer>> permute(int[] nums) {
        return helper(toList(nums), new ArrayList<>());
    }

    public List<List<Integer>> helper(List<Integer> nums, List<Integer> per) {
        List<List<Integer>> ans = new ArrayList<>();

        if (nums.isEmpty()) {
            ans.add(per);
            return ans;
        }

        List<Integer> ch = Arrays.asList(nums.get(0));
        for (int i = 0; i <= per.size(); i++) {
            List<Integer> left = per.subList(0, i);
            List<Integer> right = per.subList(i, per.size());

            List<Integer> combined = new ArrayList<>();
            combined.addAll(left);
            combined.addAll(ch);
            combined.addAll(right);

            ans.addAll(helper(nums.subList(1, nums.size()), combined));
        }
        return ans;
    }

    private List<Integer> toList(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int n : arr) list.add(n);
        return list;
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
    vector<vector<int>> permute(vector<int>& nums) {
        return helper(nums, {});
    }

    vector<vector<int>> helper(vector<int> nums, vector<int> per) {
        vector<vector<int>> ans;

        if (nums.empty()) {
            ans.push_back(per);
            return ans;
        }

        int ch = nums[0];
        nums.erase(nums.begin());

        for (int i = 0; i <= per.size(); ++i) {
            vector<int> left(per.begin(), per.begin() + i);
            vector<int> right(per.begin() + i, per.end());

            vector<int> combined;
            combined.insert(combined.end(), left.begin(), left.end());
            combined.push_back(ch);
            combined.insert(combined.end(), right.begin(), right.end());

            vector<vector<int>> sub = helper(nums, combined);
            ans.insert(ans.end(), sub.begin(), sub.end());
        }
        return ans;
    }
};

"""

# Extesnion: 

# count the no of total possible permutations
# just same as above ,only return count instead of returning 'ans'

def permutations(given, ans):
    count= 0
    if not given: # if given string is empty, then only we get one of the ans so incr count
        return 1     # simplest way of all the above three lines
    ch= given[0]   # pick char one by one from gievn string and put at diff possible positions
    # run a loop to call function again and again to put at diff positions
    for i in range(len(ans)+1):    # if there is say 'n' letter in ans then
                                    # there will be 'n+1' gaps to fill the upcoming letter
                                    # and 1st gap will start from before zero itself 
        left= ans[0:i]           # after this substring will put the 'ch'
        right= ans[i:len(ans)]    # and before this
        # res+= permutations(given[1:], left + ch + right)  # immediate parent node of the recursion call
                                                          # will keep on adding all the local 'ans'
        count+= permutations(given[1:], left + ch + right)        
    return count

# print(permutations("abc", "")) 
# print(permutations("abcd", "")) 
# print(permutations("aba", ""))  

# Java Code 
"""
public class Solution {

    public int permutations(String given, String ans) {
        int count = 0;

        if (given.isEmpty()) { // if given string is empty, then only we get one of the ans so incr count
            return 1;  // simplest way of all the above three lines
        }

        char ch = given.charAt(0);  // pick char one by one from given string and put at diff possible positions

        // run a loop to call function again and again to put at diff positions
        for (int i = 0; i <= ans.length(); i++) {
            // if there is say 'n' letter in ans then
            // there will be 'n+1' gaps to fill the upcoming letter
            // and 1st gap will start from before zero itself

            String left = ans.substring(0, i);   // after this substring will put the 'ch'
            String right = ans.substring(i);     // and before this

            // res += permutations(given.substring(1), left + ch + right);  // immediate parent node of the recursion call
            // will keep on adding all the local 'ans'
            count += permutations(given.substring(1), left + ch + right);
        }

        return count;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <string>
using namespace std;

int permutations(string given, string ans) {
    int count = 0;

    if (given.empty()) { // if given string is empty, then only we get one of the ans so incr count
        return 1;  // simplest way of all the above three lines
    }

    char ch = given[0];  // pick char one by one from given string and put at diff possible positions

    // run a loop to call function again and again to put at diff positions
    for (int i = 0; i <= ans.length(); ++i) {
        // if there is say 'n' letter in ans then
        // there will be 'n+1' gaps to fill the upcoming letter
        // and 1st gap will start from before zero itself

        string left = ans.substr(0, i);   // after this substring will put the 'ch'
        string right = ans.substr(i);     // and before this

        // res += permutations(given.substr(1), left + ch + right);  // immediate parent node of the recursion call
        // will keep on adding all the local 'ans'
        count += permutations(given.substr(1), left + ch + right);
    }

    return count;
}
"""