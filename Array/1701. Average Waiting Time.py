# Logic: Bs har customer ke liye socho ki kb aaya wo and kb usko khana mila ,
# wahi us customer ka waiting time hoga.

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        total = 0  # total waiting time
        last_finishing_time = 0  # will denote last order finishing time
        
        for customer in customers:
            if last_finishing_time >= customer[0]:
                # in this case we will update like this
                last_finishing_time += customer[1]
                total += (last_finishing_time - customer[0])
            else:
                # in this case we will update like this
                last_finishing_time = customer[0] + customer[1]  # Not adding
                total += customer[1]
                
        return total / n

# Java
"""
class Solution {
    public double averageWaitingTime(int[][] customers) {
        long n = customers.length;
        long total = 0 ;   // total waiting time
        long lastFinishingTime = 0 ;  // will denote last order finishing time
        for(int[] customer: customers){
            if(lastFinishingTime >= customer[0]) {
                // in this case we will update like this
                lastFinishingTime += customer[1] ;
                total += (lastFinishingTime - customer[0]) ;
            }
            else {
                // in this case we will update like this
                lastFinishingTime = customer[0] + customer[1] ;  // Not adding
                total += customer[1] ;
            }
        }
        return (double) total / n;
        
    }
}
"""


# Method 2: Better one
# Logic: Bs har customer ke liye socho ki kb aaya wo and kb usko khana mila ,
# wahi us customer ka waiting time hoga.

class Solution {
    public double averageWaitingTime(int[][] customers) {
        long n = customers.length;
        long total = 0 ;   // total waiting time
        long lastFinishingTime = 0 ;  // will denote last order finishing time
        for(int[] customer: customers){
            long cook_start_time = Math.max(lastFinishingTime, customer[0]) ;
            lastFinishingTime = cook_start_time  + customer[1] ;
            // for each customer ans = (kb khana banna start hua + kitna time lga banne me) - wo customer kb aaya tha
            total += (cook_start_time + customer[1]) - customer[0];
        }
        return (double) total / n;
    }
}