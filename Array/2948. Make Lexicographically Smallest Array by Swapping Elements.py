# Logic:
"""
The key insight is that:

i)  Sorting the array by values ensures we have the lexicographical order.
ii) By grouping elements based on the maxDifference constraint, we can limit swaps to valid elements.
iii)Extracting elements in the order of their indices while respecting group priorities guarantees the smallest lexicographical result.


e.g: arr = [5, 3, 9, 1, 2], threshold = 3
1) Step 1: Create Value-Index Pairs
value_index_pairs = [(5, 0), (3, 1), (9, 2), (1, 3), (2, 4)]
2) Step 2: Sort the Pairs by Value
value_index_pairs = [(1, 3), (2, 4), (3, 1), (5, 0), (9, 2)]
3) Step 3: Group Pairs Based on Threshold
grouped_pairs = [
    [(1, 3), (2, 4), (3, 1), (5, 0)],  # Group 1
    [(9, 2)]                           # Group 2
]

Explanation after group formation, like how element will be added to the index.
4) Step 4: Sort Indices in Each Group
For each group, extract the indices and sort them. This ensures that the smallest values are placed in the smallest indices.

For Group 1:

Indices: [3, 4, 1, 0]

Sorted indices: [0, 1, 3, 4]

For Group 2:

Indices: [2]

Sorted indices: [2]

5) Step 5: Assign Values Back to the Original Array
For each group, assign the values to the sorted indices in the original array.

For Group 1:

Sorted indices: [0, 1, 3, 4]

Values: [1, 2, 3, 5]

Assign:
arr[0] = 1, arr[1] = 2, arr[3] = 3, arr[4] = 5

For Group 2:

Sorted indices: [2]

Values: [9]

Assign: arr[2] = 9

6) Final Array: arr = [1, 2, 9, 3, 5]
"""

# Time = O(n*logn), space = O(n)

class Solution:
    def lexicographicallySmallestArray(self, arr: List[int], threshold: int) -> List[int]:
        size = len(arr)
        value_index_pairs = [(arr[i], i) for i in range(size)]  # we will need index also while swapping

        # Sort based on the value beacuse we will combine elements who difference in value will <= threshold
        value_index_pairs.sort(key=lambda x: x[0]) 

        # Now make groups with adjacent ele if difference in value is <= threshold
        grouped_pairs = []
        current_group = [value_index_pairs[0]]

        for i in range(1, size):
            if value_index_pairs[i][0] - value_index_pairs[i - 1][0] <= threshold:
                # means 'i' element is part of current group only
                current_group.append(value_index_pairs[i])
            else: # start a new group from here
                # i) Add current group into groups_pair
                grouped_pairs.append(current_group) 
                # ii) Start a new group from 'i' element
                current_group = [value_index_pairs[i]]
        grouped_pairs.append(current_group)

      # we can exchange all elements of same group with each other but for 'lexicographically smallest array' we will try to 
      # put smaller element at smaller index in respective group.
        for group in grouped_pairs:
            indices = [pair[1] for pair in group]
            indices.sort()

            for i in range(len(indices)):
                arr[indices[i]] = group[i][0]

        return arr

# java
"""
import java.util.*;

class Solution {
    public int[] lexicographicallySmallestArray(int[] arr, int threshold) {
        int size = arr.length;
        List<Pair<Integer, Integer>> valueIndexPairs = new ArrayList<>();

        for (int i = 0; i < size; ++i) {
            valueIndexPairs.add(new Pair<>(arr[i], i));
        }

        // Sort based on the value
        valueIndexPairs.sort(Comparator.comparingInt(Pair::getKey));

        List<List<Pair<Integer, Integer>>> groupedPairs = new ArrayList<>();
        groupedPairs.add(new ArrayList<>());
        groupedPairs.get(0).add(valueIndexPairs.get(0));

        for (int i = 1; i < size; ++i) {
            if (valueIndexPairs.get(i).getKey() - valueIndexPairs.get(i - 1).getKey() <= threshold) {
                groupedPairs.get(groupedPairs.size() - 1).add(valueIndexPairs.get(i));
            } else {
                List<Pair<Integer, Integer>> newGroup = new ArrayList<>();
                newGroup.add(valueIndexPairs.get(i));
                groupedPairs.add(newGroup);
            }
        }

        for (List<Pair<Integer, Integer>> group : groupedPairs) {
            List<Integer> indices = new ArrayList<>();
            for (Pair<Integer, Integer> pair : group) {
                indices.add(pair.getValue());
            }

            Collections.sort(indices);

            for (int i = 0; i < indices.size(); ++i) {
                arr[indices.get(i)] = group.get(i).getKey();
            }
        }

        return arr;
    }

    // Helper class to represent a pair of values
    static class Pair<K, V> {
        private final K key;
        private final V value;

        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }
    }
}
"""

# short version
class Solution:
    def lexicographicallySmallestArray(self, a: List[int], k: int) -> List[int]:
        b = []
        n = len(a)
        for i in range(n):
            b.append((a[i],i))
        b = sorted(b,key=lambda x: x[0])
        
        c = [[b[0]]]   # c[0]: one group , c[1]: another group
        for i in range(1,n):
            if b[i][0]-b[i-1][0] <= k:
                c[-1].append(b[i])
            else:
                c.append([b[i]])
        for t in c:
            ind = []
            for x,y in t:
                ind.append(y)
            ind.sort()
            for i in range(len(ind)):
                a[ind[i]] = t[i][0]
        return a

# Later try by union-find
