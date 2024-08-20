# Logic: 
"""
Keep track of numerator and denominator using two variables because we want these in ans.
suppose ans till now is : numerator = A , denominator = B & 
for next fraction numerator = a, denominator = b
then after doing operation(sum) with next fraction sum is (Ab + aB) / Bb (but cancel their greatest common divisor).
For this update A = Ab + aB , B = B * b then divide both 'A' and 'B' by gcd to get irreducible fraction till now.
"""

class Solution:
    def fractionAddition(self, expression: str) -> str:

        def hcf(a,b):
            if a == 0:
                return b
            return hcf((b%a),a)
        # for getting each fraction add space before '+' and '-' 
        lst = expression.replace("+", " +").replace("-", " -").split()
        # e.g: "-1/2+1/2" , lst = ['-1/2', '+1/2']
        A, B = 0, 1
        for num in lst:
            # now get the numerator and denominator of 1st split by splitting at '/'
            a, b = num.split("/")  # this will give 'a' and 'b' with sign.
            # convert into integer from string
            a, b = int(a), int(b)
            A = A*b+B*a
            B *= b
            divisor = gcd(abs(A), B)   # without 'abs' also it will work.
            A //= divisor    # we want integer in ans
            B //= divisor
        return str(A) + "/" + str(B)

# java
"""
import java.util.*;

public class Solution {

    // Helper function to compute the greatest common divisor
    private static int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    public String fractionAddition(String expression) {
        // Initialize the result as [numerator, denominator]
        int A = 0;
        int B = 1;
        
        // Add spaces before '+' and '-' to split the fractions easily
        String[] parts = expression.replace("+", " +").replace("-", " -").split(" ");
        for (String part : parts) {
            if (part.isEmpty()) continue;   // If the parts array contained an empty string due to extra spaces or incorrect processing.
            
            // Parse each fraction
            String[] fraction = part.split("/");
            int numerator = Integer.parseInt(fraction[0]);
            int denominator = Integer.parseInt(fraction[1]);
            
            // Update the result
            A = A * denominator + B * numerator;
            B *= denominator;
            
            // Simplify the fraction
            int divisor = gcd(Math.abs(A), Math.abs(B));
            A /= divisor;
            B /= divisor;
        }
        
        return A + "/" + B;
    }
}
"""