# Logic: Similar as 1-d array, just try to convert into 1-d array and solve.
"""
Here we are modeling the matrix as a 1d array with initial size of row*cols.
For each flip, randomly pick an index from 0 to size-1 and flip it.
int r = rand.nextInt(total--);
Then swap that flipped element with the tail element (index: size-1), 
store that mapping info (key: origin index, value: index of the tail) into a Map and decrease the size.
map.put(r, map.getOrDefault(total, total));

Next time when we randomly pick a same index we can go to the map and find the actual element stores in that index
int x = map.getOrDefault(r, r);
"""

# Note: Reset is O(n) because of map.clear()
# java
"""
class Solution 
{
    private Map<Integer, Integer> map;
    private int rows, cols, total;
    private Random rand;
    
    public Solution(int n_rows, int n_cols) 
	{
        map = new HashMap<>();
        rand = new Random();
        rows = n_rows; 
        cols = n_cols; 
        total = rows * cols;
    }
    
    public int[] flip() 
	{
        // generate index, decrease total number of values
        int r = rand.nextInt(total--); 
		
        // check if we have already put something at this index
        // if already choosed then we will take value at 'x'(swapped one) else 'x'.
        int x = map.getOrDefault(r, r); 
		
        // swap - put total at index that we generated
        map.put(r, map.getOrDefault(total, total)); 
		
        return new int[]{x / cols, x % cols}; 
    }
    
    public void reset() 
	{
        map.clear();
        total = rows * cols;   # and again make 'total = rows * cols'
    }
}
"""

# Python
import random

class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.map = {}
        self.rows = n_rows
        self.cols = n_cols
        self.total = self.rows * self.cols
        self.rand = random.Random()

    def flip(self):
        r = self.rand.randint(0, self.total - 1)
        self.total -= 1
        
        x = self.map.get(r, r)
        self.map[r] = self.map.get(self.total, self.total)
        
        return [x // self.cols, x % self.cols]

    def reset(self):
        self.map.clear()
        self.total = self.rows * self.cols