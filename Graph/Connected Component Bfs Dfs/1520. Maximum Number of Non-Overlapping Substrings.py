# intuition first, code next and time and space complexities at the last. 

# INTUITION :

'''

We need to find overlapping intervals -- and also there is a procedure to return them, which is If there are multiple solutions with the same number of substrings, return the one with minimum total length.

The initial thought is do a 0(n**2) looping and find out the maximum number no if intervals we can form starting from that index. 
This would give TLE as the constraints are 10^5. 

Now, whenever we have a string problem think about the fact that we have only 26 alphabets and 0(26*n) == 0(n).
This plays a key role here.

We record the starting and ending positions of each letter in the string, which is super efficient since there are only 26 possible lowercase letters.
This gives us a starting point to find valid substrings. 
For each letter, we take its range [start[c], end[c]] and try to make it a valid substring by including all occurrences of every letter that appears within that range. 

If a letter inside the range has occurrences outside it, we expand the range to cover them and keep checking until the range stops growing or we find it’s invalid.
This keeps the process fast since we’re only dealing with at most 26 letters.

Once we have all valid intervals, we sort them by their end points. 
Why? Because picking intervals with earlier end points lets us fit more non-overlapping intervals afterward, maximizing the number of substrings. We greedily select intervals where each one starts after the previous one ends. 
If there are multiple solutions with the same number of substrings, we pick the one with the smallest total length (sum of substring lengths) to satisfy the problem’s tiebreaker rule.

This approach is efficient because the small alphabet size (26) limits the number of intervals, and expanding each interval is bounded by the string length. The greedy selection ensures we get the maximum number of non-overlapping substrings without needing to check every possible combination.

'''
# TIME COMPLEXITY ANALYSIS: 

'''
O(26*n) for scanning string and intervals (≤26 letters), sorting O(n log n), greedy selection O(n).
    
TOTAL : 0(N log N)
'''

# SPACE COMPLEXITY = 0(n)

# CODE:


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        start, end = {}, {}
        # Step 1: Get first and last positions of each letter
        for i in range(n):
            if s[i] not in start:
                start[s[i]] = i
            end[s[i]] = i
        
        # Step 2: Compute valid intervals by expanding
        def helper(ele):
            si, e = start[ele], end[ele]
            i = si
            while i <= e:
                c = s[i]
                # Expand to include all occurrences of letter c
                if start[c] < si or end[c] > e:
                    if start[c] < si:
                        si = start[c]
                    if end[c] > e:
                        e = end[c]
                        i = si  # Restart if we expand
                        continue
                i += 1
            # Check if interval is valid
            for i in range(si, e + 1):
                if start[s[i]] < si or end[s[i]] > e:
                    return -1, -1
            return si, e
        
        # Step 3: Collect valid intervals
        intervals = []
        for ele in start.keys():
            a, b = helper(ele)
            if a != -1:
                intervals.append((a, b))
        
        # Step 4: Sort by end point for greedy picking
        intervals.sort(key=lambda x: x[1])
        
        # Step 5: Greedy selection with tiebreaker for min total length
        results = []
        max_count = 0
        for i in range(len(intervals)):
            curr = []
            last_end = -1
            for si, e in intervals[i:]:
                if si > last_end:
                    curr.append((si, e))
                    last_end = e
            if len(curr) > max_count:
                results = [curr]
                max_count = len(curr)
            elif len(curr) == max_count:
                results.append(curr)
        
        # Step 6: Pick the result with minimum total length
        min_length = float('inf')
        best = []
        for res in results:
            total = sum(b - a + 1 for a, b in res)
            if total < min_length:
                min_length = total
                best = res
        
        # Step 7: Convert intervals to substrings
        def helpme(arr):
            return [s[a:b + 1] for a, b in arr]
        
        return helpme(best)

# Java Code 
"""
class Solution {
    public List<String> maxNumOfSubstrings(String s) {
        int n = s.length();
        Map<Character, Integer> start = new HashMap<>();
        Map<Character, Integer> end = new HashMap<>();

        // Step 1: Get first and last positions of each letter
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            start.putIfAbsent(c, i);
            end.put(c, i);
        }

        // Step 2: Compute valid intervals by expanding
        int[] helper(char ele, String s, Map<Character, Integer> start, Map<Character, Integer> end) {
            int si = start.get(ele);
            int e = end.get(ele);
            int i = si;

            while (i <= e) {
                char c = s.charAt(i);
                if (start.get(c) < si || end.get(c) > e) {
                    if (start.get(c) < si) si = start.get(c);
                    if (end.get(c) > e) {
                        e = end.get(c);
                        i = si;
                        continue;
                    }
                }
                i++;
            }

            // Check if interval is valid
            for (i = si; i <= e; i++) {
                char c = s.charAt(i);
                if (start.get(c) < si || end.get(c) > e) return new int[]{-1, -1};
            }
            return new int[]{si, e};
        }

        // Step 3: Collect valid intervals
        List<int[]> intervals = new ArrayList<>();
        for (char ele : start.keySet()) {
            int[] pair = helper(ele, s, start, end);
            if (pair[0] != -1) intervals.add(pair);
        }

        // Step 4: Sort by end point for greedy picking
        intervals.sort(Comparator.comparingInt(a -> a[1]));

        // Step 5: Greedy selection with tiebreaker for min total length
        List<List<int[]>> results = new ArrayList<>();
        int maxCount = 0;

        for (int i = 0; i < intervals.size(); i++) {
            List<int[]> curr = new ArrayList<>();
            int lastEnd = -1;

            for (int j = i; j < intervals.size(); j++) {
                int si = intervals.get(j)[0];
                int e = intervals.get(j)[1];
                if (si > lastEnd) {
                    curr.add(new int[]{si, e});
                    lastEnd = e;
                }
            }

            if (curr.size() > maxCount) {
                results = new ArrayList<>();
                results.add(curr);
                maxCount = curr.size();
            } else if (curr.size() == maxCount) {
                results.add(curr);
            }
        }

        // Step 6: Pick the result with minimum total length
        int minLength = Integer.MAX_VALUE;
        List<int[]> best = new ArrayList<>();
        for (List<int[]> res : results) {
            int total = 0;
            for (int[] p : res) total += p[1] - p[0] + 1;
            if (total < minLength) {
                minLength = total;
                best = res;
            }
        }

        // Step 7: Convert intervals to substrings
        List<String> output = new ArrayList<>();
        for (int[] pair : best) {
            output.add(s.substring(pair[0], pair[1] + 1));
        }
        return output;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    vector<string> maxNumOfSubstrings(string s) {
        int n = s.length();
        unordered_map<char, int> start, end;

        // Step 1: Get first and last positions of each letter
        for (int i = 0; i < n; ++i) {
            if (!start.count(s[i])) start[s[i]] = i;
            end[s[i]] = i;
        }

        // Step 2: Compute valid intervals by expanding
        pair<int, int> helper(char ele, const string &s, unordered_map<char, int> &start, unordered_map<char, int> &end) {
            int si = start[ele], e = end[ele];
            int i = si;

            while (i <= e) {
                char c = s[i];
                if (start[c] < si || end[c] > e) {
                    if (start[c] < si) si = start[c];
                    if (end[c] > e) {
                        e = end[c];
                        i = si;
                        continue;
                    }
                }
                i++;
            }

            // Check if interval is valid
            for (i = si; i <= e; ++i) {
                char c = s[i];
                if (start[c] < si || end[c] > e) return {-1, -1};
            }
            return {si, e};
        }

        // Step 3: Collect valid intervals
        vector<pair<int, int>> intervals;
        for (const auto &p : start) {
            auto res = helper(p.first, s, start, end);
            if (res.first != -1) intervals.push_back(res);
        }

        // Step 4: Sort by end point for greedy picking
        sort(intervals.begin(), intervals.end(), [](auto &a, auto &b) {
            return a.second < b.second;
        });

        // Step 5: Greedy selection with tiebreaker for min total length
        vector<vector<pair<int, int>>> results;
        int maxCount = 0;

        for (int i = 0; i < intervals.size(); ++i) {
            vector<pair<int, int>> curr;
            int lastEnd = -1;
            for (int j = i; j < intervals.size(); ++j) {
                int si = intervals[j].first, e = intervals[j].second;
                if (si > lastEnd) {
                    curr.push_back({si, e});
                    lastEnd = e;
                }
            }
            if (curr.size() > maxCount) {
                results = {curr};
                maxCount = curr.size();
            } else if (curr.size() == maxCount) {
                results.push_back(curr);
            }
        }

        // Step 6: Pick the result with minimum total length
        int minLength = INT_MAX;
        vector<pair<int, int>> best;
        for (auto &res : results) {
            int total = 0;
            for (auto &p : res) total += p.second - p.first + 1;
            if (total < minLength) {
                minLength = total;
                best = res;
            }
        }

        // Step 7: Convert intervals to substrings
        vector<string> output;
        for (auto &p : best) {
            output.push_back(s.substr(p.first, p.second - p.first + 1));
        }
        return output;
    }
};
"""