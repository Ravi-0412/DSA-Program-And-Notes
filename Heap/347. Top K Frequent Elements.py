# method 1: Sort based on frequency
# time: O(n*logn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        # hashmap will map each ele with their respective frequency
        for num in nums:
            hashmap[num]= 1 + hashmap.get(num, 0)
        arr= sorted(hashmap, key= hashmap.get, reverse= True) 
                                # will sort the hashmap based on freq(value of hashmap) i.e key that we had provided 
                                # and will store the key wrt each value
        return arr[:k]

# just make min heap with fre of each ele
# time: O(nlogk)
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap, heap= {}, []
        # hashmap will map each ele with their respective frequency
        for num in nums:
            hashmap[num]= 1 + hashmap.get(num, 0)
            
        # now make a min heap with freq as first ele and key of dict as second ele
        # when we push more than one ele in heap, it create the min/max heap acc to the 1st ele(1st pushed ele)
        for ele in hashmap:
            heapq.heappush(heap, (hashmap[ele],ele))  # value and key is pushed
            if len(heap)>k:
                heapq.heappop(heap)
                
        # now you will be left with fre of k top ele with their key
        # now print the key of each remaining ele in heap
        ans= []
        for num in heap:
            ans.append(num[1])
        return ans

        # for printing the ele with most fre first
        # ans=[]
        # for i in range(len(heap)):
        #     temp= heapq.heappop(heap)
        #     ans.append(temp[1])      # will store the ele with least fre among k top frequent first
        # # print(ans)
        # return ans[::-1]    # now return the reverse of ans


# method 2: using bucket sort(better one)
# just create the freq matrix for maximum no of count and that can be len(arr)
# time: O(n), space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= {}   # to store the count of each element
        for num in nums:
            count[num]= 1+ count.get(num, 0)   # if num is already present then incr the val by '1'
                                               # else incr the value by zero
                
        freq= [[] for i in range(len(nums)+1)]    # will contain the array of ele for a given frequency
                                                 # since freq can be equal to n so we are taking the row equal to n+1
            
        # now store the array of ele with for a given fre
        # like at index 1: will contain array of ele whose fre is 1 and so on till n
        for n,c in count.items():
            freq[c].append(n)
            
        # now traverse the freq from right to left 
        # as most freq ele will be at higher index
        # and store the ele into ans and when you have stored 'k' ele just return the ans
        ans= []
        for i in range((len(freq)-1),0,-1):
            for n in freq[i]:
                ans.append(n)
                if len(ans)==k:
                    return ans



# Java
# Link: https://leetcode.com/problems/top-k-frequent-elements/solutions/1927648/one-of-the-best-explanation/
""""
# Method 1: minHeap
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int num: nums){
            map.put(num, map.getOrDefault(num, 0) + 1) ;
        }
        PriorityQueue<Map.Entry<Integer, Integer>> minHeap = new PriorityQueue<>((a, b) -> a.getValue() - b.getValue()) ;
        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            minHeap.add(entry);
            if(minHeap.size() > k)
                minHeap.poll();
        }
        int res[] = new int[k];
        for(int i = 0; i < k; i++){
            res[i] = minHeap.poll();
        }
        return res;
    }
}


# Method 2: Bucket Sort

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i : nums){
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        
        List<Integer> bucket[] = new ArrayList[nums.length + 1];
        
        for(int key : map.keySet()){
            int freq = map.get(key);
            if(bucket[freq] == null){
                bucket[freq] = new ArrayList<>();
            }
            bucket[freq].add(key);
        }
        
        int res[] = new int[k];
        int index = 0;
        for(int i = bucket.length - 1; i >= 0; i--){
            if(bucket[i] != null){
                for(int val : bucket[i]){
                    res[index++] = val;
                    if(index == k) return res;
                }
            }
        }
        return res;
    }
}

"""