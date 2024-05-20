# Method1:
# We need maximum ele one by one. But we also need to keep track of their index.
# For keeping track of index 1st enumerate then sort in reverse order according to value.

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(enumerate(score), key = lambda x : x[1], reverse = True)
        for i in range(len(score)):
            ind , num = sorted_score[i]
            if i == 0:
                score[ind] = "Gold Medal"
            elif i == 1:
                score[ind] = "Silver Medal"
            elif i == 2:
                score[ind] = "Bronze Medal"
            else:
                score[ind] = str(i + 1)
        return score

# Method 2:
# Can use max heap for getting maximum one by one


# Java
"""
# Method 1:
public class Solution {
    public String[] findRelativeRanks(int[] nums) {
        int[][] pair = new int[nums.length][2];
        
        for (int i = 0; i < nums.length; i++) {
            pair[i][0] = nums[i];
            pair[i][1] = i;
        }
        
        Arrays.sort(pair, (a, b) -> (b[0] - a[0]));
        
        String[] result = new String[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                result[pair[i][1]] = "Gold Medal";
            }
            else if (i == 1) {
                result[pair[i][1]] = "Silver Medal";
            }
            else if (i == 2) {
                result[pair[i][1]] = "Bronze Medal";
            }
            else {
                result[pair[i][1]] = (i + 1) + "";
            }
        }

        return result;
    }
}

# method 2: Using Heap
class Solution {
    public String[] findRelativeRanks(int[] score) {
        
        int n = score.length;
        String[] res = new String[n];
        
        PriorityQueue<Integer> pq = 
            new PriorityQueue<>((a,b)->score[b]-score[a]);
        
        for(int i=0;i<n;i++){
            pq.add(i);
        }
        int i=1;
        while(!pq.isEmpty()){
            
            int idx = pq.poll();
            
            if(i>3){
                res[idx] = Integer.toString(i);
            }else if(i==1){
                res[idx] = "Gold Medal";
            }else if(i==2){
                res[idx] = "Silver Medal";
            }else if(i==3){
                res[idx] = "Bronze Medal";
            }
            i++;
        }
        
        return res;
        
    }
}

"""