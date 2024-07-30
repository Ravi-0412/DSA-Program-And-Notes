# idea
# Given 2 nums 'a' and 'b':
# If a % k == x and b % k == k - x 
# then (a + b) is divisible by k

# proof: 
#  a % k == x
#  b % k == k - x
#  (a + b) % k = ((a + b)%k)%k = (a%k + b%k)%k = (x + k - x)%k = k%k = 0 
#  Hence, (a + b) % k == 0 and (a + b) is divisible by k.

# OR
# a%k = x             =>       a = nk+x
# b%k = k-x           =>       b = mk+k-x
# a+b = nk+mk+k+x-x   =>       a+b = (m+n+1)k    => (a+b) % k = 0

# Approach :
# i) Keep count of remainders of all elements of arr
# ii) frequency[0] keeps all elements divisible by k, and a divisible of k can only
# form a group with other divisible of k. Hence, total number of such divisibles must be even.
# iii) for every element with remainder of i (i != 0) there should be a element with remainder k-i.
# iv) Hence, frequency[i] should be equal to frequency[k-i]

# Just do dry and run for : arr = [-1,1,-2,2,-3,3,-4,4], k= 3 . Ans = True

# Note: in python '-2 % 5' will = 3 (kitna add kare 2 me ki 5 se divisible ho jaye) but in 
# Java '-2 % 5' will = -2 only .
# so in java if 'remainder' is negative make it +ve like pythob by adding 'k'.

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        frequency = defaultdict(int)
        
        for num in arr:
            num %= k
            frequency[num] += 1
        
        if frequency[0] % 2 != 0:
            return False
        
        for i in range(1, k // 2 + 1):
            if frequency[i] != frequency[k - i]:
                return False
        
        return True


# Java
"""
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean canArrange(int[] arr, int k) {
        Map<Integer, Integer> frequency = new HashMap<>();
        
        for (int num : arr) {
            num %= k;
            if (num < 0) num += k;
            frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        }
        
        if (frequency.getOrDefault(0, 0) % 2 != 0) return false;
        
        for (int i = 1; i <= k / 2; i++) {
            if (!frequency.getOrDefault(i, 0).equals(frequency.getOrDefault(k - i, 0))) return false;
        }
        
        return true;
    }
}

"""

# easier and shorter using 'array' instead of map in java.
"""
class Solution {
    public boolean canArrange(int[] arr, int k) {
        int[] frequency = new int[k];
        for(int num : arr){
            num %= k;
            if(num < 0) num += k;
            frequency[num]++;
        }
        if(frequency[0]%2 != 0) return false;
        
        for(int i = 1; i <= k/2; i++)
            if(frequency[i] != frequency[k-i]) return false;
			
        return true;
    }
}
"""