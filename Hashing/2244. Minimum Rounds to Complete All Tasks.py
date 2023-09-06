# Logic: Just find the freq of task for each level(store in hashmap).
# Then traverse the hashmap, if val < 2 then not possible so return -1.
# else minimum no of rounds needed to complete those taks at same level = ceil(val / 3) . dividing by '3' for minimum round.

# Time = space = O(n)

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks)
        ans = 0
        for key, val in freq.items():
            if val < 2 :
                return -1
            ans += ceil(val / 3)
        return ans