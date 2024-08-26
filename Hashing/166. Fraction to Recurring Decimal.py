# The important thing is to consider all edge cases while thinking this problem,
# including: negative integer, possible overflow, etc.

# Use HashMap to store a remainder and its associated index while doing the division so 
# that whenever a same remainder comes up, we know there is a repeating fractional part.

# How to detect and handle repitition.
# i) Detecting Repetition:
# After appending each digit to res, the method checks if num (the current remainder) already exists in map.
# If map.containsKey(num) is true, it means that num has been seen before, 
# indicating the start of a repeating sequence of decimals.

# ii) Handling Repetition:
# When repetition is detected, the method retrieves the index from map where num was first encountered.
# It then inserts "(" at that index in res to mark the beginning of the repeating sequence and can return the ans from here only.

# Time: 

# java
"""
class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
    if (numerator == 0) {
        return "0";
    }
    
    StringBuilder res = new StringBuilder();
    
    // Determine sign. if result will be negative then append '-' at start.
    // if combination is '+ -' or '- +' then we will get negative result.
    // shortcut of checking this using 'xor'.
    if ((numerator > 0) ^ (denominator > 0)) {
        res.append("-");
    }
    
    long num = Math.abs((long)numerator);
    long den = Math.abs((long)denominator);
    
    // Integral part
    res.append(num / den);
    num %= den;
    
    if (num == 0) {
        return res.toString();
    }
    
    // Fractional part
    res.append(".");
    HashMap<Long, Integer> map = new HashMap<>();  // will store the first index of 'num'(remainder in fraction part)
    map.put(num, res.length());   # this num has been seen at this index at first
    
    while (num != 0) {
        num *= 10;
        res.append(num / den);   # get the remainder in fraction part
        num %= den;
        
        if (map.containsKey(num)) {
            // means recurring so add '(' when this number has occured first time
            int index = map.get(num);
            res.insert(index, "(");     
            res.append(")");  // add ')' at last and break
            break;
        } else {
            map.put(num, res.length());
        }
    }
    
    return res.toString();
}

}
"""

# Python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res = []
        
        # Determine sign
        if (numerator > 0) ^ (denominator > 0):
            res.append("-")
        
        num = abs(numerator)
        den = abs(denominator)
        
        # Integral part
        res.append(str(num // den))
        num %= den
        
        if num == 0:
            return "".join(res)
        
        # Fractional part
        res.append(".")
        map = {}
        map[num] = len(res)
        
        while num != 0:
            num *= 10
            res.append(str(num // den))
            num %= den
            
            if num in map:
                index = map[num]
                res.insert(index, "(")
                res.append(")")
                break
            else:
                map[num] = len(res)
        
        return "".join(res)
