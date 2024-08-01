# Logic: 1)For each spell, we need to find the number of potions that can form a successful pair with it.
# 2) For this for each spell , find the smallest number from potions which can form successful pair with current spell.

# How to do?
# Just sort the potions and apply binary search to find the '2' point say 'left'
# then all numbers from  to 'left' to 'len(potions)' will form a successful pair with current spell i.e
# count = len(potions) - left

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        n = len(spells)
        m = len(potions)
        pairs = [0] * n
        potions.sort()
        for i in range(n):
            # now find the 1st element from potions which can form a successful pair with this spells[i]
            # just same as we find the 1st index of an element
            spell = spells[i]
            left = 0
            right = m - 1
            while left <= right:
                mid = left + (right - left) // 2
                product = spell * potions[mid]
                if product >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            pairs[i] = m - left
        return pairs
    
# java
"""
class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.length;
        int m = potions.length;
        int[] pairs = new int[n];
        Arrays.sort(potions);
        for (int i = 0; i < n; i++) {
            int spell = spells[i];
            int left = 0;
            int right = m - 1;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                long product = (long) spell * potions[mid];
                if (product >= success) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            pairs[i] = m - left;
        }
        return pairs;
    }
}
"""