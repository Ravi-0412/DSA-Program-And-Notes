# We have to make ans in descending order taking num one by one.

# Logic: first convert nums values into string since we want number to be greater after string concatenation not by actual value.
# we will decide which will come 1st value after combining two string.
# e.g [3, 30] , ans = 330 not 303. so we have to comparer after concatenation.

# Note: Just you have to sort elements based on string concatenation.
# so you can use any sorting algorithm for this.

# Method 1:

# using python custom comparator
# Note: 'cmp_to_key' working is excatly same as 'compare()' method in java.

# How both works?  cmp_to_key(x, y) or compare(x, y)
# Note: ordering will depend on what we are return , not on the logic.
# so, you can write your own logic based on what ordering you want.
# how it order elements?
# i) if returning '1' then it means place 'y' before 'x'.
# ii) if returning '-1' then, it means place 'x' before 'y'.
# iii) if returning '0' then, ordeing doesn't matter.

# so for writing in single line(all three return statement), we can use:
# i) return x - y  => for sorting in ascending order.
# if x > y then it will return '1' place 'y' before 'x' because it means 'x' is bigger than 'y'.
# ans similar for other cases.
# ii) return y - x => for sorting in descending order

# Note: Here we want to sort in descending order after concatenating the string so 
# we will write according to 'y + x'.

# Read about 'cmp_to_key' from :
# link: https://www.geeksforgeeks.org/how-does-the-functools-cmp_to_key-function-works-in-python/

from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def cmp_func(x , y):
            # after concatenating two string, 1st = x, 2nd = y
            if y + x > x + y:
                # i) then 'y' should come before 'x'
                return 1
            if x == y:
                # order of x and y doesn't matter.
                return 0
            # else:  x should come before y.
            return -1

            # return (y + x) - (x + y)  # won't be valid because 'x' and 'y' is string , '-' is not supported between string.

        nums = [str(num) for num in nums]
        nums.sort(key = cmp_to_key(cmp_func))
        return str(int("".join(nums)))   # first convert into 'int' to avoid recurring '0' at start.
    
# Method 2: Insertion sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)

        # we have to sort in descending order
        def compare(n1, n2):
            return str(n1) + str(n2) < str(n2) + str(n1)

        for i in range(1, n):
            cur = nums[i]
            j = i - 1
            while j >= 0 and compare(nums[j] , cur):
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = cur
        return str(int("".join(map(str, nums))))

# Java
""""
// compareTo: compares both string and integer.
// Link: https://www.w3schools.com/java/ref_string_compareto.asp

public class Solution {
    public String largestNumber(int[] nums) {
        // Convert the array of integers to an array of strings
        String[] strs = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strs[i] = String.valueOf(nums[i]);
        }

        // Create a custom comparator
        Comparator<String> comparator = new Comparator<String>() {
            @Override
            public int compare(String x, String y) {
                // Concatenate both ways and compare
                String order1 = x + y;
                String order2 = y + x;
                return order2.compareTo(order1); // We want to sort in descending order so we have written 'order2' first.
            }
        };

        // Sort the array using the custom comparator
        Arrays.sort(strs, comparator);

        // Handle the case where the largest number is '0'
        if (strs[0].equals("0")) {
            return "0";
        }

        // Build the largest number from the sorted array
        StringBuilder largestNumber = new StringBuilder();
        for (String str : strs) {
            largestNumber.append(str);
        }

        return largestNumber.toString();
    }
}
"""