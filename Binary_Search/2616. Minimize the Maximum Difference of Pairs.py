# method 1: 

# What we have find indirectly:
# Find the smallest difference say 'diff' such that we can find 'p' pairs having difference between them is <= 'diff'.
# Just like we find the 1st index.

# Note vvi: wo 'min_diff' between two pair find karna h jiske niche hmko 'p' pairs nhi mile jiska 'pair_diff',  'min_diff se <= ho.
# Finally wahi 'min_diff' mera ans hoga.(minimum maximum difference among all p pairs)


# Note: Since given "no index can appear more than once amongst the p pairs".
# so it will better to check with adjacent pair only for any ele for each index because 
# when we will check with any other element then difference will be even more.

# if pair_diff <= given_diff then we will increase the index by '2' else by '1' so that no index used more than one time.

# vvi: pointer ko jb update karenge tb mere ans minimise hoga and jb 'while' loop break hoga tb required and milega i.e : 'min(max)'.

# time: O(n*(log(A))), A= max(nums)- min(nums)

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        def isPossible(diff):  # At least 'p' pair available h kya with absolute diff between pair <= 'diff'?
            count= 0
            i= 1  # start checking between index '1' and index '0'.
            while i < n:
                if nums[i]- nums[i-1] <= diff:  # sirf adjacent ke saath hi mil sakta h kyonki aage or bda diff hota jayega. && hmko same pair index ko exclude bhi karna h..
                    count+= 1
                    i+= 1  # is pair ka koi bhi index kisi or pair me nhi hona chahiye. isliye next time 'i+2' se check karenge.
                i+= 1
            return count>= p     
        
        nums.sort()  # for chekcing the diff easily 
        n= len(nums)
        start, end= 0, nums[-1] - nums[0]
        while start < end:
            mid= start + (end- start)//2
            if isPossible(mid):  # or chota diff khojo khojo.
                end= mid
            else:
                start= mid +1
        return start

# Java Code 
"""
public class Solution {
    private int[] nums;
    private int n, p;

    public int minimizeMax(int[] nums, int p) {
        this.nums = nums;
        this.p = p;
        this.n = nums.length;

        // for checking the diff easily
        Arrays.sort(nums);

        int start = 0, end = nums[n - 1] - nums[0];
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (isPossible(mid)) {  // or chota diff khojo khojo
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }

    // At least 'p' pair available h kya with absolute diff between pair <= 'diff'?
    private boolean isPossible(int diff) {
        int count = 0;
        int i = 1;  // start checking between index '1' and index '0'
        while (i < n) {
            // sirf adjacent ke saath hi mil sakta h kyonki aage or bda diff hota jayega. && hmko same pair index ko exclude bhi karna h..
            if (nums[i] - nums[i - 1] <= diff) {
                count++;
                i++;  // is pair ka koi bhi index kisi or pair me nhi hona chahiye
            }
            i++;
        }
        return count >= p;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        this->nums = nums;
        this->n = nums.size();
        this->p = p;

        // for checking the diff easily
        sort(nums.begin(), nums.end());

        int start = 0, end = nums[n - 1] - nums[0];
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (isPossible(mid)) {  // or chota diff khojo khojo
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }

private:
    vector<int> nums;
    int n, p;

    // At least 'p' pair available h kya with absolute diff between pair <= 'diff'?
    bool isPossible(int diff) {
        int count = 0;
        int i = 1;  // start checking between index '1' and index '0'
        while (i < n) {
            // sirf adjacent ke saath hi mil sakta h kyonki aage or bda diff hota jayega. && hmko same pair index ko exclude bhi karna h..
            if (nums[i] - nums[i - 1] <= diff) {
                count++;
                i++;  // is pair ka koi bhi index kisi or pair me nhi hona chahiye
            }
            i++;
        }
        return count >= p;
    }
};
"""

# Extension: 

# Note vvvi: Every sub-function we are calling can be asked as a separate problem in interview 
# # so keep those function pattern also in mind like when to use.
# Like: 1) " Count the no of pairs <= given_num such that no index appear more than once amongst those pairs".
# Solution above

# 2) vvi : count no of subarray having pair wise difference between any two ele in that subarray is  <= given_diff.
# Don't know this is correct or not. Have to ask someone
def countPair(diff, nums):
    n= len(nums)
    cnt = 0
    i, j = 0, 1
    while j < n:
        while nums[j] - nums[i] > diff:
            i += 1
        l = j - i + 1  if i != j else 0 #  length_valid_subarray. same ele can't form pair with himself
        cnt += l
        j += 1
        return cnt


# Java Code 
"""
public class Solution {
    public int countPair(int diff, int[] nums) {
        int n = nums.length;
        int cnt = 0;
        int i = 0, j = 1;

        while (j < n) {
            while (nums[j] - nums[i] > diff) {
                i += 1;
            }
            // length_valid_subarray. same ele can't form pair with himself
            int l = (i != j) ? (j - i + 1) : 0;
            cnt += l;
            j += 1;
        }
        return cnt;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int countPair(int diff, const std::vector<int>& nums) {
        int n = nums.size();
        int cnt = 0;
        int i = 0, j = 1;

        while (j < n) {
            while (nums[j] - nums[i] > diff) {
                i += 1;
            }
            // length_valid_subarray. same ele can't form pair with himself
            int l = (i != j) ? (j - i + 1) : 0;
            cnt += l;
            j += 1;
        }
        return cnt;
    }
};
"""