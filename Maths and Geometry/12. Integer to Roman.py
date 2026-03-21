# Method 1:
"""
By sorting the Roman numeral symbols from largest to smallest, 
you ensure that you always use the largest possible symbol first, which is exactly how Roman numerals are constructed.

Time: O(n)
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        # We pair Roman symbols with their values, including "subtraction cases" (like IV or CM).
        # These are ordered from largest (M) to smallest (I).
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        ans = ""  
        i = 0  # Pointer to track which symbol/value pair we are currently checking

        # Continue until the number is fully converted to Roman symbols
        while num > 0:
            # If the current value fits into our number (e.g., if num is 2500, 1000 fits)
            while num >= values[i]:
                ans += roman[i]   # Append the symbol to our result string
                num -= values[i]  # Subtract that value from our remaining total
            
            # Once we can't fit any more of the current symbol, move to the next smaller one
            i += 1  
        
        return ans

# Java
"""
class Solution {
    public String intToRoman(int num) {
        StringBuilder result = new StringBuilder();
	
        String[] roman = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
        
        int i = 0;
                //iterate until the number becomes zero, NO NEED to go until the last element in roman array
        while (num >0) {
            while ( num >= values[i]) {
                num -= values[i];
                result.append(roman[i]);
            }
            i++;
        }
        return result.toString();
            
        }
}
"""

# Method 2: 
# Time: O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        # ones array represents: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        # tens array represents: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        
        # hundreds array represents: [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        
        # thousands array represents: [0, 1000, 2000, 3000]
        thousands = ["", "M", "MM", "MMM"]
        
        # Convert the number to Roman numeral by combining values from the arrays
        return thousands[num // 1000] + hundreds[(num % 1000) // 100] + tens[(num % 100) // 10] + ones[num % 10]


# java
"""
class Solution {
    public String intToRoman(int num) {
        // ones array represents: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        String ones[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        
        // tens array represents: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        String tens[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        
        // hundreds array represents: [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
        String hundreds[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        
        // thousands array represents: [0, 1000, 2000, 3000]
        String thousands[] = {"", "M", "MM", "MMM"};
        
        // Convert the number to Roman numeral by combining values from the arrays
        return thousands[num / 1000] + hundreds[(num % 1000) / 100] + tens[(num % 100) / 10] + ones[num % 10];
    }
}
"""
