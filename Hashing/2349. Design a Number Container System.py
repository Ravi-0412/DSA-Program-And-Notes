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

  # Java
"""
Common Methods of TreeSet:
Method	Description
boolean add(E e)	Adds the specified element to the set if it is not already present.
boolean remove(Object o)	Removes the specified element from the set if it is present.
void clear()	Removes all elements from the set.
boolean contains(Object o)	Returns true if the set contains the specified element.
E first()	Returns the first (lowest) element in the set.
E last()	Returns the last (highest) element in the set.
E lower(E e)	Returns the greatest element less than the given element, or null.
E floor(E e)	Returns the greatest element less than or equal to the given element.
E higher(E e)	Returns the smallest element greater than the given element.
E ceiling(E e)	Returns the smallest element greater than or equal to the given element.
int size()	Returns the number of elements in the set.
boolean isEmpty()	Returns true if the set contains no elements.
Iterator<E> iterator()	Returns an iterator over the elements in ascending order.
Iterator<E> descendingIterator()	Returns an iterator over the elements in descending order.
SortedSet<E> headSet(E toElement)	Returns a view of the portion of the set whose elements are less than toElement.
SortedSet<E> tailSet(E fromElement)	Returns a view of the portion of the set whose elements are greater than or equal to fromElement.
SortedSet<E> subSet(E fromElement, E toElement)	Returns a view of the portion of the set whose elements range from fromElement (inclusive) to toElement (exclusive).
"""
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
