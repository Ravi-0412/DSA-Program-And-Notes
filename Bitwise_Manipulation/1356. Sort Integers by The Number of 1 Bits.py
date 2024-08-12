class Solution:
    def countBits(num):
        count = 0
        
        while num > 0:
            count += 1
            num &= (num - 1)  # Clear the least significant set bit.
        
        return count

    def sortByBits(self, arr):
        arr.sort(key = lambda num: (Solution.countBits(num), num))
        return arr


# java
"""
class Solution {
    public int[] sortByBits(int[] arr) {
        // Convert the input integer array to Integer objects for sorting
        Integer[] integerArr = Arrays.stream(arr).boxed().toArray(Integer[]::new);

        // Create a custom comparator to sort by bit count and then numerically
        // Comparator<Integer> comparator = new BitCountComparator();

        // Sort the array using the custom comparator
        Arrays.sort(integerArr, new BitCountComparator());

        // Convert the sorted array back to primitive integers
        int[] sortedArr = Arrays.stream(integerArr).mapToInt(Integer::intValue).toArray();

        return sortedArr;
    }
}

class BitCountComparator implements Comparator<Integer> {
    private int findBitCount(int num) {
        // Count the number of set bits (1s) in the binary representation of num
        int count  = 0;

        while (num > 0) {
            count ++;
            num &= (num - 1);
        }

        return count ;
    }

    @Override
    public int compare(Integer a, Integer b) {
        int bitCountA = findBitCount(a);
        int bitCountB = findBitCount(b);

        if (bitCountA == bitCountB) {
            return a - b; // If bit counts are the same, compare numerically.
        }

        return bitCountA - bitCountB; // Sort by the bit count in ascending order.
    }
}
"""