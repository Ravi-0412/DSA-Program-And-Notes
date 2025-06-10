# Just little extension of Q :"169. Majority Element".
# Think in same way like 'majority ele'. (Last method).

# There can be maximum two ele in our ans.

# logic: Think in election, you have to find the two condidate who secured more than n//3 votes.
# so first find the two condidates who secured highest votes amon all.
# After that check if there vote count is > n//3.

# Note: Har ele ke pass '3 choice h either condidate1 ho, condidate2 ho ya different ele ho.

# Time: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2= 0, 0
        condidate1, condidate2= None, None
        for n in nums:
            if n== condidate1:
                # vote of condidate1 will increase
                count1+= 1
            elif n== condidate2:
                # vote of condidate2 will increase
                count2+= 1
                
            # agar na hi condidate1 h na hi condidate2 h then 
            # cur ele kuch bhi ho sakte h depending upon value of count1 and count2.
            elif count1== 0:
                # cur ele will become the 1st condidate(one of possible condidate)
                condidate1, count1= n, 1
            elif count2== 0:
                # cur ele will become the 2nd condidate(one of possible condidate)
                condidate2, count2= n, 1
            else:   # count1 > 0 and count 2> 0
                # third condidate came other than one and two.
                # so will minimise the vote of both.
                count1, count2= count1 -1, count2 -1
        return [n for n in (condidate1, condidate2) if nums.count(n) > len(nums) // 3]   # shortcut of above lines.

# Java
"""
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int count1 = 0, count2 = 0;
        Integer candidate1 = null, candidate2 = null;

        // Step 1: Find the two candidates
        for (int n : nums) {
            if (candidate1 != null && n == candidate1) {
                count1++;
            } else if (candidate2 != null && n == candidate2) {
                count2++;
            } else if (count1 == 0) {
                candidate1 = n;
                count1 = 1;
            } else if (count2 == 0) {
                candidate2 = n;
                count2 = 1;
            } else {
                count1--;
                count2--;
            }
        }

        // Step 2: Verify if the candidates appear more than n/3 times
        List<Integer> result = new ArrayList<>();
        int threshold = nums.length / 3;
        count1 = 0;
        count2 = 0;

        for (int n : nums) {
            if (candidate1 != null && n == candidate1) count1++;
            if (candidate2 != null && n == candidate2) count2++;
        }

        if (count1 > threshold) result.add(candidate1);
        if (count2 > threshold) result.add(candidate2);

        return result;
    }
}
"""

# C++ Code 
"""
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int count1 = 0, count2 = 0, candidate1 = -1, candidate2 = -1;

        // Phase 1: Finding two possible majority candidates
        for (int n : nums) {
            if (n == candidate1) {
                count1++;
            } else if (n == candidate2) {
                count2++;
            } else if (count1 == 0) {
                candidate1 = n;
                count1 = 1;
            } else if (count2 == 0) {
                candidate2 = n;
                count2 = 1;
            } else {
                count1--;
                count2--;
            }
        }

        // Phase 2: Validating the candidates
        vector<int> result;
        int threshold = nums.size() / 3;
        int freq1 = 0, freq2 = 0;

        for (int n : nums) {
            if (n == candidate1) freq1++;
            else if (n == candidate2) freq2++;
        }

        if (freq1 > threshold) result.push_back(candidate1);
        if (freq2 > threshold) result.push_back(candidate2);

        return result;
    }
};
"""