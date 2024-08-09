# Logic: We don't need to take space of size '2050' because year is varying from 1950 to 2050.
# So space of size '101' will be fine.


# java
"""
class Solution {
    public int maximumPopulation(int[][] logs) {
        int[] year = new int[101];
		// O(n) -> n is log.length

        for(int[] log : logs){
            year[log[0] - 1950]++;
            year[log[1] - 1950]--;
        }
        
        int maxNum = year[0], maxYear = 1950;

        for(int i = 1; i < year.length; i++){
            year[i] += year[i - 1];  // Generating Prefix Sum
            if(year[i] > maxNum){
                maxNum = year[i];
                maxYear = i + 1950;
            }
        }
        return maxYear;
        
    }
}
"""

# Related Q:
# 1) 2848. Points That Intersect With Cars
# just apply same logic and add count of point whose value > 0.

# 2) 