# Logic:
"""
We map an index to a number, and a number to all its indexes (we use a set so indexes are sorted).

For change, we use the first map to get the previous number for the index.

Then, we remove that index from the second map for the previous number.

Time of change() and find(): O(logn)
"""

from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.num_to_indices = defaultdict(SortedList)
        self.index_to_num = {}

    def change(self, index: int, number: int) -> None: 
        if index in self.index_to_num:
            old = self.index_to_num[index]
            self.num_to_indices[old].discard(index)
            if not self.num_to_indices[old]:
                del self.num_to_indices[old]
        self.num_to_indices[number].add(index)
        self.index_to_num[index] = number
            

    def find(self, number: int) -> int:
        if number in self.num_to_indices:
            return self.num_to_indices[number][0]
        return -1

  # Java
  """
  import java.util.*;

public class NumberContainers {
    // Map to store number to set of indices mapping
    private Map<Integer, TreeSet<Integer>> numToIndices;
    // Map to store index to number mapping
    private Map<Integer, Integer> indexToNum;

    public NumberContainers() {
        numToIndices = new HashMap<>();
        indexToNum = new HashMap<>();
    }

    // Change the number associated with an index
    public void change(int index, int number) {
        // If the index already has a number associated with it, remove it from the old number's set
        if (indexToNum.containsKey(index)) {
            int old = indexToNum.get(index);
            numToIndices.get(old).remove(index);
            // If no indices remain for the old number, remove the number entry from the map
            if (numToIndices.get(old).isEmpty()) {
                numToIndices.remove(old);
            }
        }

        // Add the index to the set of indices for the new number
        numToIndices.putIfAbsent(number, new TreeSet<>());
        numToIndices.get(number).add(index);

        // Update the index to number mapping
        indexToNum.put(index, number);
    }

    // Find the smallest index associated with a number
    public int find(int number) {
        // Check if the number exists in the map and has associated indices
        if (numToIndices.containsKey(number) && !numToIndices.get(number).isEmpty()) {
            // Return the smallest index (which is the first element in the TreeSet)
            return numToIndices.get(number).first();
        }
        return -1; // Return -1 if the number is not found
    }
}
  """
