# Method 1:

# here we are greedy about finding the 1st ele of group.
# and first ele must be minimum only and for this we will use minHeap

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n= len(hand)
        if n % groupSize!= 0:
            return False
        if groupSize== 1:
            return True
        cnt= collections.defaultdict(int)
        for num in hand:
            cnt[num]+= 1
        heapq.heapify(hand)    # since we want minimum each time for a group
        for i in range(n//groupSize):
            # finding the 1st ele of group
            first_ele= heapq.heappop(hand)
            # check if this ele has already occured to it's frequency and find the ele with atleast one freq remaining.
            while cnt[first_ele]== 0:
                first_ele = heapq.heappop(hand)
            
            # now find all the elements of the group, we have got the starting ele of gr in 'start'
            # other remaining number must be consecutive to that.
            for i in range(groupSize):
                cnt[first_ele]-= 1
                if cnt[first_ele] < 0:  # means this no is not available or it has been used equal to no of times of it's frequency.
                    return False
                first_ele+= 1
        return True


# Method 2: No need of heap, we can sort and use pointer
"""
The initial thoughts after reading this problem is, we can group the elements only if n % len(group) == 0.
Also, if group size is 1, we can immediately return True.

Now, we can start by sorting the array and then try to group the elements.
This thought of sorting came because, we are asked to group only the consecutive elements.

We can start iterating through the sorted array and each time go 'size' times forward to check if that element is present in array and simultaneously remove it from the array.
As, removal takes 0(n) time, we will use a hashmap to store the elements and their counts.

Like, this traversal keeps going on. 
At any point, if we find that the element is not present in the hashmap, we can return False.

Also, each time we remove a element we keep a count of the removed elements , and at the last check if this count is equal to the length of the array, we can return True.
Else, we can return False.

# TIME COMPLEXITY :

'''
sorting the array = O(n log n)
iterating through the array = O(n * size)
overall time complexity = O(n log n + n * size) = O(n log n) (as size is constant)

# SPACE COMPLEXITY :

O(n) for the hashmap to store the elements and their counts.
O(1) for the variables used.
overall space complexity = O(n)
'''

"""

# PYTHON : 
from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], size : int) -> bool:
        n = len(hand)
        hand.sort()
        mpp = defaultdict(int)
        for ele in hand :
            mpp[ele] += 1 
        cnt = 0
        for i in range(n):
            if mpp[hand[i]]:
                # If the element is already used, we skip it
                temp = hand[i]
                for _ in range(size):
                    # Go size times forward to check if the element is present
                    cnt += 1
                    if not mpp[temp]:
                        return False
                    mpp[temp] -= 1 
                    if mpp[temp] == 0 :
                        del mpp[temp]
                    temp += 1 
        return cnt == n
    

# JAVA : 

'''
class Solution {
    public boolean isNStraightHand(int[] hand, int size) {
        int n = hand.length;
        Arrays.sort(hand);
        TreeMap<Integer, Integer> map = new TreeMap<>();
        for (int num : hand) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (map.containsKey(hand[i])) {
                int temp = hand[i];
                for (int j = 0; j < size; j++) {
                    cnt++;
                    if (!map.containsKey(temp)) return false;
                    map.put(temp, map.get(temp) - 1);
                    if (map.get(temp) == 0) map.remove(temp);
                    temp++;
                }
            }
        }
        return cnt == n;
    }
}
'''

# C++ : 

'''
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int size) {
        int n = hand.size();
        sort(hand.begin(), hand.end());
        map<int, int> mpp;
        for (int num : hand) {
            mpp[num]++;
        }
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (mpp[hand[i]]) {
                int temp = hand[i];
                for (int j = 0; j < size; j++) {
                    cnt++;
                    if (mpp[temp] == 0) return false;
                    mpp[temp]--;
                    if (mpp[temp] == 0) mpp.erase(temp);
                    temp++;
                }
            }
        }
        return cnt == n;
    }
};
'''
    