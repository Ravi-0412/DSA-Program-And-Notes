# count the freq of each ele in Arr1.
# then traverse arr2, and append the cur ele of arr2 in ans no of times= frequency.
# and make freq of these ele= 0

# for remaining ele which is not in arr2, we have to simply add in sorted order.
# for this store all keys in a list, sort the list.
# then traverse the list, and if its freq is != zero, then add that num to ans, no of times= frequency.

# time: O(n + n*logn)= O(nlogn), space ; O(n)

from collections import Counter
class Solution:
    
    def relativeSort (self,A1, N, A2, M):
        freq= Counter(A1)
        ans= []
        for n in A2:
            ans.extend([n]*freq[n])  # add manullay 'n' for 'freq[n]' no of times.
            freq[n]= 0
        keysList= list(freq.keys())
        keysList.sort()
        for n in keysList:
            if freq[n]!= 0:
                ans.extend([n]*freq[n])
        return ans
# Java
"""
class Solution {

    public int[] sortA1ByA2(int[] A1, int N, int[] A2, int M) {
        // Frequency map to count occurrences in A1
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : A1) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        
        List<Integer> result = new ArrayList<>();
        
        // Add elements from A2 in the order they appear
        for (int num : A2) {
            if (freq.containsKey(num)) {
                int count = freq.get(num);
                for (int i = 0; i < count; i++) {
                    result.add(num);
                }
                freq.remove(num); // Remove after adding
            }
        }
        
        // Collect remaining elements and sort them
        List<Integer> remaining = new ArrayList<>(freq.keySet());
        Collections.sort(remaining);
        
        for (int num : remaining) {
            int count = freq.get(num);
            for (int i = 0; i < count; i++) {
                result.add(num);
            }
        }
        
        // Convert result list to an array
        int[] ans = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            ans[i] = result.get(i);
        }
        
        return ans;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> relativeSort(vector<int>& A1, int N, vector<int>& A2, int M) {
        unordered_map<int, int> freq;
        vector<int> ans;

        // Count frequency of elements in A1
        for (int num : A1) {
            freq[num]++;
        }

        // Add elements of A2 in order to the result
        for (int num : A2) {
            ans.insert(ans.end(), freq[num], num);  // Add manually 'num' for 'freq[num]' times
            freq[num] = 0;
        }

        // Get remaining elements from A1, sort them
        vector<int> remainingKeys;
        for (auto& entry : freq) {
            if (entry.second > 0) {
                remainingKeys.push_back(entry.first);
            }
        }
        sort(remainingKeys.begin(), remainingKeys.end());

        // Add remaining elements to the result
        for (int num : remainingKeys) {
            ans.insert(ans.end(), freq[num], num);
        }

        return ans;
    }
};
"""
