# Brute Force: 

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n, m, o= len(s) , len(a), len(b)
        indexes_i, indexes_j = [], []
        for i in range(n):
            if s[i : i + m] == a:
                indexes_i.append(i)
            if s[i : i + o] == b:
                indexes_j.append(i)
        ans = []
        for i in indexes_i:
            for j in indexes_j:
                if abs(i - j) <= k:
                    ans.append(i)
                    break    # No need to check further for current index 'i'.
        return sorted(ans)
        # return ans.sort()   # this will give wrong ans.
            
# Method 2: Optimisation

# Just extension of '28. Find the Index of the First Occurrence in a String'.

# steps:
# 1) Store indices of all occurence of a in s in array say 'indexes_i'.
# 2) Store indices of all occurence of b in s in array say 'indexes_j'.

# Indices we can find with the help of 'Z-Algo'.

# 3) Now problem reduces to "For each element of indexes_i, 
# find if any index exist in indexes_j such that their absolute difference is at most k".

# This we do by either : a) Two Pointer or 2) Binary Search

# Later do by binary search also.

# Time: O(len(s) + len(a) + len(b))

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        def Z_Algo(s, a):
            m , n = len(s) , len(a)
            s1 = a + '$' + s   
            z = [0] * (m + n + 1)
            total = m + n + 1
            l , r = 0, 0
            for i in range(1, total):
                if i < r:
                    z[i] = min(r -i , z[i - l])
                while i + z[i] < total and s1[z[i]] == s1[i + z[i]]:
                    z[i] += 1
                if i + z[i] > r:
                    l , r = i, i + z[i]
            indexes = []
            for i in range(n + 1, total):  
                if z[i] == n: 
                    indexes.append(i - n -1)
            return indexes

        indexes_i = Z_Algo(s, a)
        indexes_j = Z_Algo(s, b)
                
        ans = []
        i , j = 0, 0
        # abs(i - j) <= k means (i - j) <= k or (j - i) <= k.
        # Check violation of these two condition.
        while i < len(indexes_i) and j < len(indexes_j):
            # 1)  (i - j) > k . So increase 'j' to reduce the diff.
            if indexes_i[i] - indexes_j[j] > k :
                j += 1
            # 2) (j -i ) > k . so increase 'i' to reduce the diff.
            elif indexes_j[j] - indexes_i[i] > k :
                i += 1
            else:
                # means abs(i - j) <= k . so add 'i' in ans.
                ans.append(indexes_i[i])
                i += 1
        return ans

# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    public List<Integer> beautifulIndices(String s, String a, String b, int k) {
        int n = s.length(), m = a.length(), o = b.length();
        List<Integer> indexes_i = new ArrayList<>();
        List<Integer> indexes_j = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (s.substring(i, Math.min(i + m, n)).equals(a)) {
                indexes_i.add(i);
            }
            if (s.substring(i, Math.min(i + o, n)).equals(b)) {
                indexes_j.add(i);
            }
        }

        List<Integer> ans = new ArrayList<>();
        for (int i : indexes_i) {
            for (int j : indexes_j) {
                if (Math.abs(i - j) <= k) {
                    ans.add(i);
                    break; // No need to check further for current index 'i'.
                }
            }
        }
        Collections.sort(ans);
        return ans;
    }
}
//Method 2
import java.util.*;

class Solution {
    private List<Integer> Z_Algo(String s, String a) {
        int m = s.length(), n = a.length();
        String s1 = a + "$" + s;
        int total = m + n + 1;
        int[] z = new int[total];
        int l = 0, r = 0;

        for (int i = 1; i < total; i++) {
            if (i < r) {
                z[i] = Math.min(r - i, z[i - l]);
            }
            while (i + z[i] < total && s1.charAt(z[i]) == s1.charAt(i + z[i])) {
                z[i]++;
            }
            if (i + z[i] > r) {
                l = i;
                r = i + z[i];
            }
        }

        List<Integer> indexes = new ArrayList<>();
        for (int i = n + 1; i < total; i++) {
            if (z[i] == n) {
                indexes.add(i - n - 1);
            }
        }
        return indexes;
    }

    public List<Integer> beautifulIndices(String s, String a, String b, int k) {
        List<Integer> indexes_i = Z_Algo(s, a);
        List<Integer> indexes_j = Z_Algo(s, b);

        List<Integer> ans = new ArrayList<>();
        int i = 0, j = 0;

        while (i < indexes_i.size() && j < indexes_j.size()) {
            if (indexes_i.get(i) - indexes_j.get(j) > k) {
                j++;
            } else if (indexes_j.get(j) - indexes_i.get(i) > k) {
                i++;
            } else {
                ans.add(indexes_i.get(i));
                i++;
            }
        }
        return ans;
    }
}
"""

# C++ Code 
"""
//Method 1
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> beautifulIndices(string s, string a, string b, int k) {
        int n = s.size(), m = a.size(), o = b.size();
        vector<int> indexes_i, indexes_j;

        for (int i = 0; i < n; i++) {
            if (s.substr(i, m) == a) {
                indexes_i.push_back(i);
            }
            if (s.substr(i, o) == b) {
                indexes_j.push_back(i);
            }
        }

        vector<int> ans;
        for (int i : indexes_i) {
            for (int j : indexes_j) {
                if (abs(i - j) <= k) {
                    ans.push_back(i);
                    break; // No need to check further for current index 'i'.
                }
            }
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};
//Method 2
class Solution {
public:
    vector<int> Z_Algo(string s, string a) {
        int m = s.size(), n = a.size();
        string s1 = a + "$" + s;
        int total = m + n + 1;
        vector<int> z(total, 0);
        int l = 0, r = 0;

        for (int i = 1; i < total; i++) {
            if (i < r) {
                z[i] = min(r - i, z[i - l]);
            }
            while (i + z[i] < total && s1[z[i]] == s1[i + z[i]]) {
                z[i]++;
            }
            if (i + z[i] > r) {
                l = i;
                r = i + z[i];
            }
        }

        vector<int> indexes;
        for (int i = n + 1; i < total; i++) {
            if (z[i] == n) {
                indexes.push_back(i - n - 1);
            }
        }
        return indexes;
    }

    vector<int> beautifulIndices(string s, string a, string b, int k) {
        vector<int> indexes_i = Z_Algo(s, a);
        vector<int> indexes_j = Z_Algo(s, b);

        vector<int> ans;
        int i = 0, j = 0;

        while (i < indexes_i.size() && j < indexes_j.size()) {
            if (indexes_i[i] - indexes_j[j] > k) {
                j++;
            } else if (indexes_j[j] - indexes_i[i] > k) {
                i++;
            } else {
                ans.push_back(indexes_i[i]);
                i++;
            }
        }
        return ans;
    }
};
"""

