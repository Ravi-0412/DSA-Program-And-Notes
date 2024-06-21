# Logic: same as 'Aggressive cows'

# Time = O(n*log(max(arr) - min(arr)))

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        minimum = min(position)
        maximum = max(position)
        start = 1
        end = maximum - minimum
        
        while start <= end:
            mid = start + (end - start) // 2
            if self.isPossible(position, mid, m):
                start = mid + 1
            else:
                end = mid - 1
        
        return end
    
    def isPossible(self, arr: List[int], mid: int, m: int) -> bool:
        balls = 1
        prev = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - prev >= mid:
                balls += 1
                prev = arr[i]
        
        return balls >= m


# java
"""
class Solution {
    public int maxDistance(int[] position, int m) {
        Arrays.sort(position);

        int minimum = Arrays.stream(position).min().getAsInt();
        int maximum   = Arrays.stream(position).max().getAsInt();
        int start = 1 , end = maximum - minimum ;
        while(start <= end) {
            int mid = start + (end - start) /2 ;
            if(isPossible(position, mid, m))
                start = mid + 1 ;
            else
                end = mid - 1 ;
        }
        return end ;
    }

    public boolean isPossible(int[] arr, int mid, int m) {
        int balls = 1;
        int prev = arr[0] ;
        for(int i = 1; i < arr.length; i ++) {
            if(arr[i] - prev >= mid) {
                balls += 1 ;
                prev = arr[i] ;
            }
        }
        return balls >= m ;
    }
}
"""