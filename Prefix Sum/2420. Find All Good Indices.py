# Logic: Computing increasing and decreasing length for every index in optimal way.

# Note: 
# Whenever precomputation i.e some parameter calculation is required till every index,
# then we should think of Dynamic Programming(Prefix / Suffix).

class Solution:
    def goodIndices(self, a: List[int], k: int) -> List[int]:
        n, ans= len(a) ,[]
        dp1 , dp2= [1]*(n+1), [1]*(n+1)
        for i in range(1,n):
            if a[i-1]>=a[i]:  dp1[i]= dp1[i-1]+1
        
        for i in range(n-2,-1,-1):
            if a[i]<=a[i+1]:  dp2[i]= dp2[i+1]+1
        
        for i in range(k,n-k):
            if dp1[i-1]>=k and dp2[i+1]>=k: ans+= [i]
        return ans

# java
"""
class Solution {
    public List<Integer> goodIndices(int[] a, int k) {
        int n= a.length;
        int[] dp1= new int[n+1];  Arrays.fill(dp1,1);
        int[] dp2= new int[n+1];  Arrays.fill(dp2,1);   
        List<Integer> ans= new ArrayList<>();
        
        for(int i=1;i<n;i++)  
            if(a[i-1]>=a[i]) dp1[i]= dp1[i-1]+1;
        
        for(int i=n-2;i>=0;i--)
            if(a[i]<=a[i+1]) dp2[i]= dp2[i+1]+1;
        
        for(int i=k;i<n-k;i++)
            if(dp1[i-1]>=k && dp2[i+1]>=k) ans.add(i);
        return ans;
    }
}
"""

# Related q to do later:
# 1) 2100. Find Good Days to Rob the Bank
# 2) 1800. Maximum Ascending Subarray Sum