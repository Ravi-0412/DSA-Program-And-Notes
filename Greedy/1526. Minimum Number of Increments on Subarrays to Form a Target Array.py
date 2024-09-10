# Logic: 
"""
Note: number of operations to construct target array from zero array = number of operations to reduce target array to zero array.

i) Start with first position a[0]. We know that it will take overall a[0] operations to reach a[0] from 0.

ii) Now, 2 things can happen from here:

a) We encounter a number less than a[0] (a[1] < a[0]): In this case we can simply reuse the same operations that we did for a[0]. 
i.e If array was (3, 2), we can first perform 3 operations and then use 2 of the same operations in next term. 
However, going forward, we will only have a[1] operations available for reuse.
b) We encounter a number greater than a[0] (a[1] > a[0]): In this case we can simply reuse the same operations that we did for a[0]. 
And additionally, we will perform a[1] - a[0] more operation to reach a[1]. Again, going forward, we will have a[1] operations available for reuse.

"""
                                                                                                                                        
# Java
"""                                                                                                                                       
class Solution {
    public int minNumberOperations(int[] target) {
        int n = target.length;
        int ans = target[0];
        for(int i = 1;i < n;i++){
            if(target[i] > target[i-1]){
                ans += target[i] - target[i-1];

            }
        }
        return ans;
    }
}
"""
