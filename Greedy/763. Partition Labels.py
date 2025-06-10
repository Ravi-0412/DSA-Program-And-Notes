# time= space= O(n)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n= len(s)
        # form a hashmap which will store the last index of each char.
        last_index = {s[i]: i for i in range(n)}   # s[i]: key ans 'i': value
        start, ans= 0, []    # 'i' denotes the start of the partition
        while start < n:
            # minimum length will be equal to last index of 'start'.
            # but it can go beyond also if char before 'last_index[s[start]]' have last occurence beyond 'last_index[s[start]]'
            # so we need ti check that
            end, j= last_index[s[start]], start +1
            while j < end:
                if last_index[s[j]] > end:
                    end= last_index[s[j]]
                j+= 1
            # now we have go the 1st partition. end will denote the last index of partition.
            ans.append(end- start +1)
            start = end +1   # now we will search for next partition from this index
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public List<Integer> partitionLabels(String s) {
        int n = s.length();
        
        // form a hashmap which will store the last index of each char.
        Map<Character, Integer> lastIndex = new HashMap<>();
        for (int i = 0; i < n; i++) {
            lastIndex.put(s.charAt(i), i);  // s[i]: key and 'i': value
        }

        int start = 0;
        List<Integer> ans = new ArrayList<>();  // 'start' denotes the start of the partition

        while (start < n) {
            // minimum length will be equal to last index of 'start'.
            // but it can go beyond also if char before 'lastIndex.get(s[start])' 
            // have last occurrence beyond 'lastIndex.get(s[start])'
            // so we need to check that
            int end = lastIndex.get(s.charAt(start));
            int j = start + 1;
            while (j < end) {
                if (lastIndex.get(s.charAt(j)) > end) {
                    end = lastIndex.get(s.charAt(j));
                }
                j++;
            }

            // now we have got the 1st partition. 'end' will denote the last index of partition.
            ans.add(end - start + 1);
            start = end + 1;  // now we will search for next partition from this index
        }

        return ans;
    }
}

"""

# C++ Code 
"""
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> partitionLabels(string s) {
        int n = s.length();
        
        // form a hashmap which will store the last index of each char.
        unordered_map<char, int> lastIndex;
        for (int i = 0; i < n; i++) {
            lastIndex[s[i]] = i;  // s[i]: key and 'i': value
        }

        int start = 0;
        vector<int> ans;  // 'start' denotes the start of the partition

        while (start < n) {
            // minimum length will be equal to last index of 'start'.
            // but it can go beyond also if char before 'lastIndex[s[start]]' 
            // have last occurrence beyond 'lastIndex[s[start]]'
            // so we need to check that
            int end = lastIndex[s[start]];
            int j = start + 1;
            while (j < end) {
                if (lastIndex[s[j]] > end) {
                    end = lastIndex[s[j]];
                }
                j++;
            }

            // now we have got the 1st partition. 'end' will denote the last index of partition.
            ans.push_back(end - start + 1);
            start = end + 1;  // now we will search for next partition from this index
        }

        return ans;
    }
};

"""




