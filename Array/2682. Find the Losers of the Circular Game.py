# Just Brtute force

# Constraint is very small , so we can use array to store the count.
# Or can use 'set'.

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        i= 1  # turn
        count= [0]* (n + 1)   # to check where we reach '2' time. 1-based indexing.
        count[1]= 1     # starting from person '1'
        curNum= 1
        while True:
            # next person
            curNum= (curNum + i*k) % n 
            # using 1-based indexing but doing modulus with 'n'. so '0' will mean 'n' only.
            # Since doing % with 'n' so if we have to check whether we reach 'n' separately
            # otherwise we won't get n'
            if curNum== 0:
                curNum= n
            count[curNum]+= 1
            if count[curNum]== 2:
                break
            i+= 1
            
        ans= []
        for i, cnt in enumerate(count):
            if i != 0 and cnt== 0:
                ans.append(i)
        return ans

# java
"""
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] circularGameLosers(int n, int k) {
        int i = 1; // turn
        int[] count = new int[n + 1]; // to check where we reach 2 times (1-based indexing)
        count[1] = 1; // starting from person '1'
        int curNum = 1;
        
        while (true) {
            // next person
            curNum = (curNum + i * k) % n;
            // using 1-based indexing, but modulus with 'n' means '0' should mean 'n'
            if (curNum == 0) {
                curNum = n;
            }
            count[curNum]++;
            if (count[curNum] == 2) {
                break;
            }
            i++;
        }
        
        List<Integer> temp = new ArrayList<>();
        for (int j = 1; j <= n; j++) {
            if (count[j] == 0) {
                temp.add(j);
            }
        }
        
        // Convert List<Integer> to int[]
        int[] ans = new int[temp.size()];
        for (int j = 0; j < temp.size(); j++) {
            ans[j] = temp.get(j);
        }
        
        return ans;
    }
}

"""
