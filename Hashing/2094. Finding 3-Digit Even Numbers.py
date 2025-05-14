"""
Logic: 
Try to check for all the possible 3 digit numbers by using 3 loops i, j and k where
i : Hundreds digit
j : Tens digit
k : Units digit (only evens)
"""

# Time: O(9*10*10) , space: O(10)

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        digits_freq = Counter(digits)  # Count frequency of each digit
        for i in range(1, 10):  # First digit can't be 0
            if digits_freq[i] == 0:
                continue
            digits_freq[i] -= 1  # Use one instance of digit i
            for j in range(0, 10):  # Second digit
                if digits_freq[j] == 0:
                    continue
                digits_freq[j] -= 1  # Use one instance of digit j
                for k in range(0, 10, 2):  # Third digit must be even
                    if digits_freq[k] == 0:
                        continue
                    # Form valid 3-digit even number and add to result
                    ans.append(i*100 + j*10 + k)
                digits_freq[j] += 1  # Restore digit j
            digits_freq[i] += 1  # Restore digit i
        return ans

# Java
"""
import java.util.*;

class Solution {
    public List<Integer> findEvenNumbers(int[] digits) {
        List<Integer> ans = new ArrayList<>();
        int[] freq = new int[10];

        // Count frequency of each digit
        for (int d : digits) {
            freq[d]++;
        }

        // Try all combinations: i (hundreds), j (tens), k (units, must be even)
        for (int i = 1; i <= 9; i++) {
            if (freq[i] == 0) continue;
            freq[i]--;

            for (int j = 0; j <= 9; j++) {
                if (freq[j] == 0) continue;
                freq[j]--;

                for (int k = 0; k <= 9; k += 2) {  // Only even numbers
                    if (freq[k] == 0) continue;
                    int num = i * 100 + j * 10 + k;
                    ans.add(num);
                }

                freq[j]++; // Restore count for j
            }

            freq[i]++; // Restore count for i
        }

        return ans;
    }
}
"""
