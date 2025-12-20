# Basic

# First part solution where len(word) <= 26 and all characters are different.

# Logic : we have '8' keys (2- 9) and on these '8' keys, we can place 26 characters i.e 
# '3' char on 6 keys and 4 character on '2' keys.


# Time: O(1)
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8:
            # we can place all char at 1st position for all 'n' keys.
            return n
        if n <= 16 :
            # we can place '8' char at 1st position for all '8' keys.
            # And remaining char at 2nd position.
            return 8 + (n - 8) *2
        if n <= 24:
            # we can place '8' char at 1st position for all '8' keys.
            # Next '8' char at 2nd position for all '8' keys 
            # And remaining char at 3rd position.
            return 8 + 8*2 + (n- 16) * 3
        if n == 25:
            # we can place '8' char at 1st position for all '8' keys.
            # Next '8' char at 2nd position for all '8' keys
            # Next '8' char at 3rd position for all '8' keys.
            # And remaining '1' char at 4th position at any key.  
            return 8 + 8*2 + 8 * 3 + 1 * 4
        # if n == 26:
        # we can place '8' char at 1st position for all '8' keys.
        # Next '8' char at 2nd position for all '8' keys
        # Next '8' char at 3rd position for all '8' keys.
        # And remaining '1' char at 4th position at any key. 
        return 8 + 8*2 + 8 * 3 + 2 * 4

# Above code without comment
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        # print(n, "length")
        if n <= 8:
            return n
        if n <= 16 :
            return 8 + (n - 8) *2
        if n <= 24:
            return 8 + 8*2 + (n- 16) * 3
        return 8 + 8*2 + 8 * 3 + (n - 24) * 4     
                                    # (n - 24): we will have to type '4' times and number of such char will be either 1 or 2
        

# Actual question

# Method 1:
    
"""
Just same way as above with just one modification.
Just add the push count(1, 2, ,3, 4) with frequency in above same logic.
i.e character having highest 8th frequency we will have to push 'one' time, and so on.
""" 


# Logic: First we will try to put character having maximum freq at 1st position
# to minimise the push.
    
# Time = space = O(n)

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        ans = 0
        cnt = 0  # think count as 'length n' of part1.
        for f in sorted(freq.values(), reverse = True):
            cnt += 1
            if cnt <= 8:
                ans += f
            elif cnt <= 16:
                ans += f *2
            elif cnt <= 24 :
                ans += f *3
            elif cnt == 25 or cnt == 26:
                ans += f *4
        return ans
            
# Java Code 
"""
import java.util.*;

class Solution {
    public int minimumPushes(String word) {
        int n = word.length();

        if (n <= 8) return n;
        if (n <= 16) return 8 + (n - 8) * 2;
        if (n <= 24) return 8 + 8 * 2 + (n - 16) * 3;
        return 8 + 8 * 2 + 8 * 3 + (n - 24) * 4; 
    }
}

// Optimized approach with frequency-based calculation
class Solution {
    public int minimumPushes(String word) {
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : word.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        List<Integer> freqs = new ArrayList<>(freq.values());
        freqs.sort(Collections.reverseOrder());

        int ans = 0, cnt = 0;
        for (int f : freqs) {
            cnt++;
            if (cnt <= 8) ans += f;
            else if (cnt <= 16) ans += f * 2;
            else if (cnt <= 24) ans += f * 3;
            else ans += f * 4;
        }
        return ans;
    }
}
"""

# C++ Code 
"""
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minimumPushes(string word) {
        int n = word.size();

        if (n <= 8) return n;
        if (n <= 16) return 8 + (n - 8) * 2;
        if (n <= 24) return 8 + 8 * 2 + (n - 16) * 3;
        return 8 + 8 * 2 + 8 * 3 + (n - 24) * 4; 
    }
};

// Optimized approach with frequency-based calculation
class Solution {
public:
    int minimumPushes(string word) {
        unordered_map<char, int> freq;
        for (char c : word) freq[c]++;

        vector<int> freqs;
        for (auto& [ch, f] : freq) {
            freqs.push_back(f);
        }

        sort(freqs.begin(), freqs.end(), greater<int>());
        
        int ans = 0, cnt = 0;
        for (int f : freqs) {
            cnt++;
            if (cnt <= 8) ans += f;
            else if (cnt <= 16) ans += f * 2;
            else if (cnt <= 24) ans += f * 3;
            else ans += f * 4;
        }
        return ans;
    }
};
"""

# Method 2:
# Just shortcut of method 1
# Time = O(26*log26) , space : O(26)

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        ans = 0
        cnt = 0  # think count as 'length n' of part1.
        for i, f in enumerate(sorted(freq.values(), reverse = True)):
            position = i // 8 + 1      # where that letter will be placed
            ans += f * position
        return ans

# java
"""
import java.util.*;

class Solution {
    public int minimumPushes(String word) {
        // Count frequency
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : word.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        // Extract and sort frequencies in descending order
        List<Integer> values = new ArrayList<>(freq.values());
        values.sort(Collections.reverseOrder());

        int ans = 0;

        for (int i = 0; i < values.size(); i++) {
            int position = i / 8 + 1;  
            ans += values.get(i) * position;
        }

        return ans;
    }
}
"""

# C++ 
"""
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumPushes(string word) {
        unordered_map<char, int> freq;
        for (char c : word) {
            freq[c]++;
        }

        vector<int> values;
        for (auto &p : freq) {
            values.push_back(p.second);
        }

        sort(values.begin(), values.end(), greater<int>());

        int ans = 0;
        for (int i = 0; i < values.size(); i++) {
            int position = i / 8 + 1;   
            ans += values[i] * position;
        }

        return ans;
    }
};
"""
