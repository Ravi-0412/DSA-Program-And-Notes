# my thought processs.
# 1st thought to use set.
# Using set we can do 'insert', 'remove' in O(1) but for getting random everytime we 
# will have to convert into list because 'random function only works with set/tuple'.
# so 'getting random' will go in O(n).

# 2nd i thought using set only and for getting random just return the first element
# by traversing set i.e 
"""
for num in self.randomSet:
    return num
"""
# But this will not ensure equal probability of all element.
# Becuase when we traverse set , we see element in way they get inserted into hashmap.


# Note: So we are sure that for getting random we will have to use 'list'.
# But when we will use list only then 'remove' will take 'O(n)' as we have to shift elements
# from index where 'removing_ele' is present to last to fill the removed space.

# so it will go in O(n).

# Also we need to check if 'any element is present or not' while inserting & 
# removing and in list it will take O(n).

# So avoid this O(n), we will use list (for getting random) in O(1) and
# hashmap for doing other two operations in O(1).

# Note vvi: The follow-up: allowing duplications.
# For example, after insert(1), insert(1), insert(2), getRandom() should have 2/3 chance return 1 and 1/3 chance return 2.
# Then, remove(1), 1 and 2 should have an equal chance of being selected by getRandom().

# The idea is to add a set to the hashMap to remember all the locations of a duplicated number.

# Note: wrote solution for follow up below

class RandomizedSet:
    
    def __init__(self):
        self.randomList = []
        self.numToIndex = {}

    def insert(self, val: int) -> bool:
        if val in self.numToIndex:
            return False
        # first map val: index_in_list
        self.numToIndex[val] = len(self.randomList)
        # Then add in list
        self.randomList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numToIndex:
            return False
        
        last_elem_in_list = self.randomList[-1]
        index_of_elem_to_remove = self.numToIndex[val]

        # swap the last ele with element that we want to remove.
        # Then element that we want to remove will go at last.
        self.randomList[-1], self.randomList[index_of_elem_to_remove] = val, self.randomList[-1]

        # update the index of last element(now will be at 'index_of_elem_to_remove')
        self.numToIndex[last_elem_in_list] = index_of_elem_to_remove

        # Then pop to remove this element. O(1) because removing from last
        self.randomList.pop()

        # delete the element from map
        del self.numToIndex[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.randomList)


# java
"""
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

class RandomizedSet {

    private ArrayList<Integer> randomList;
    private HashMap<Integer, Integer> numToIndex;
    private Random rand;

    public RandomizedSet() {
        randomList = new ArrayList<>();
        numToIndex = new HashMap<>();
        rand = new Random();
    }

    public boolean insert(int val) {
        if (numToIndex.containsKey(val)) {
            return false;
        }
        numToIndex.put(val, randomList.size());
        randomList.add(val);
        return true;
    }

    public boolean remove(int val) {
        if (!numToIndex.containsKey(val)) {
            return false;
        }

        int lastElem = randomList.get(randomList.size() - 1);
        int index = numToIndex.get(val);

        // Swap the element to be removed with the last element
        randomList.set(index, lastElem);
        numToIndex.put(lastElem, index);

        // Remove the last element
        randomList.remove(randomList.size() - 1);
        numToIndex.remove(val);
        return true;
    }

    public int getRandom() {
        return randomList.get(rand.nextInt(randomList.size()));
    }
}
"""

# follow up: with duplicates

import random

class RandomizedSet:

    def __init__(self):
        self.randomList = []
        self.numToIndex = {}

    def insert(self, val: int) -> bool:
        if val not in self.numToIndex:
            self.numToIndex[val] = set()
        self.numToIndex[val].add(len(self.randomList))
        self.randomList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numToIndex or not self.numToIndex[val]:
            return False

        index_to_remove = self.numToIndex[val].pop()   # getting last index of 'val'
        last_elem = self.randomList[-1]

        if index_to_remove != len(self.randomList) - 1:
            # Bring at last that we have to remove by swapping
            self.randomList[index_to_remove] = last_elem
            self.numToIndex[last_elem].remove(len(self.randomList) - 1)
            self.numToIndex[last_elem].add(index_to_remove)

        self.randomList.pop()

        if not self.numToIndex[val]:
            del self.numToIndex[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.randomList)

"""
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Random;

class RandomizedSet {

    private ArrayList<Integer> randomList;
    private HashMap<Integer, HashSet<Integer>> numToIndices;
    private Random rand;

    public RandomizedSet() {
        randomList = new ArrayList<>();
        numToIndices = new HashMap<>();
        rand = new Random();
    }

    public boolean insert(int val) {
        if (!numToIndices.containsKey(val)) {
            numToIndices.put(val, new HashSet<>());
        }
        numToIndices.get(val).add(randomList.size());
        randomList.add(val);
        return true;
    }

    public boolean remove(int val) {
        if (!numToIndices.containsKey(val) || numToIndices.get(val).isEmpty()) {
            return false;
        }

        int indexToRemove = numToIndices.get(val).iterator().next();   // getting the 1st index for 'val'
        numToIndices.get(val).remove(indexToRemove);

        int lastElem = randomList.get(randomList.size() - 1);
        if (indexToRemove != randomList.size() - 1) {
            randomList.set(indexToRemove, lastElem);
            numToIndices.get(lastElem).remove(randomList.size() - 1);
            numToIndices.get(lastElem).add(indexToRemove);
        }

        randomList.remove(randomList.size() - 1);
        if (numToIndices.get(val).isEmpty()) {
            numToIndices.remove(val);
        }
        return true;
    }

    public int getRandom() {
        return randomList.get(rand.nextInt(randomList.size()));
    }
}

"""

# Related Q:
# 1) 519. Random Flip Matrix
