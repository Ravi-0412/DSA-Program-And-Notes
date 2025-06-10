# Logic:
"""
We map an index to a number, and a number to all its indexes (we use a set so indexes are sorted).

For change, we use the first map to get the previous number for the index.

Then, we remove that index from the second map for the previous number.

Q) Why 'if not self.num_to_indices[old]:
                del self.num_to_indices[old]' is needed?
Ans: If there is no index associated with this number and, if we call the 'find()' then,
it will give 'list index out of range' because 'self.num_to_indices[number] == null  and you are returning self.num_to_indices[number][0]'.

Time of change() and find(): O(logn)
"""

from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.num_to_indices = defaultdict(SortedList) # dictionary that stores a mapping from numbers to the indices (positions) where those numbers are located.
        self.index_to_num = {}

    def change(self, index: int, number: int) -> None: 
        if index in self.index_to_num:
            # then remove this index from 'indices of current number which is at current index'
            old = self.index_to_num[index]   # get the number
            self.num_to_indices[old].discard(index)  # remove this index from indices of 'old'numner
            if not self.num_to_indices[old]:
                del self.num_to_indices[old]
        self.num_to_indices[number].add(index)
        self.index_to_num[index] = number
            

    def find(self, number: int) -> int:
        if number in self.num_to_indices:
            return self.num_to_indices[number][0]
        return -1

  # Java Code
"""
import java.util.*;

class NumberContainers {
    private Map<Integer, TreeSet<Integer>> numToIndices; // Maps numbers to sorted index positions
    private Map<Integer, Integer> indexToNum; // Maps index positions to their respective numbers

    public NumberContainers() {
        numToIndices = new HashMap<>();
        indexToNum = new HashMap<>();
    }

    public void change(int index, int number) {
        if (indexToNum.containsKey(index)) {
            int old = indexToNum.get(index); // Get the previous number
            numToIndices.get(old).remove(index); // Remove index from old number's indices
            if (numToIndices.get(old).isEmpty()) {
                numToIndices.remove(old);
            }
        }
        numToIndices.computeIfAbsent(number, k -> new TreeSet<>()).add(index);
        indexToNum.put(index, number);
    }

    public int find(int number) {
        if (numToIndices.containsKey(number) && !numToIndices.get(number).isEmpty()) {
            return numToIndices.get(number).first();
        }
        return -1;
    }
}
"""

# C++ Code 
"""
#include <map>
#include <set>
using namespace std;

class NumberContainers {
private:
    map<int, set<int>> num_to_indices; // Maps numbers to sorted index positions
    map<int, int> index_to_num; // Maps index positions to their respective numbers

public:
    void change(int index, int number) {
        if (index_to_num.find(index) != index_to_num.end()) {
            int old = index_to_num[index]; // Get the previous number
            num_to_indices[old].erase(index); // Remove index from old number's indices
            if (num_to_indices[old].empty()) {
                num_to_indices.erase(old);
            }
        }
        num_to_indices[number].insert(index);
        index_to_num[index] = number;
    }

    int find(int number) {
        if (num_to_indices.find(number) != num_to_indices.end() && !num_to_indices[number].empty()) {
            return *num_to_indices[number].begin();
        }
        return -1;
    }
};
"""