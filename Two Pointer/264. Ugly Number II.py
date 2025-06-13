# Method 1: 

"""
maths + Two Pointer Approach & DP.
logic: the next number has to be the the smallest number among all the existing numbers
 multiplied by 2, 3,5 that isn't in the list already
i.e smallest jo pre se bda ho.

1) Essentially, we have to multiply the existed ugly numbers by 2, 3 and 5 to get a bigger ugly number,
however, if we blindly multiply all the existed numbers by 2, 3 and 5, then the number could grow much faster than needed.
2)  Hence, every time we only try to find the next smallest ugly number.
3) Also Note:  any existed number will be multiplied by 2, 3 and 5 once and only once, otherwise duplicate.
 we can use a pointer to keep track of where the 2, 3 and 5 are going to multiply in the next step.
4) Once, we find the next minimum, we can move on that corresponding pointer, 
otherwise it always stays at the already existed ugly number which would makes pointer useless.

Note: we will get the next ugly number only using the already ugly number in the list.
i.e mutiplying existing number either by '2', '3' or '5'.
It should be next smallest so will check every possiblity by multiplying by (2,3 or 5) using the next pointer value of (2,3 or 5).

for more clarity: Read solution link in sheet and read the comments by "Iemeore" and "Wuxb09" under that solution.

time = space = O(n)
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly= [1]  # first ugly number is '1' only.  # list will automatically get maintained in sorted order.
        p2, p3, p5= 0, 0, 0   # pointer to num 2,3,5. Number by which '2', 3 and 5 will get multiplied further.
        for i in range(2, n + 1):
            next= min(ugly[p2] * 2, ugly[p3]* 3, ugly[p5] *5)  # will auto give number which won't be in the list.
            ugly.append(next)
            # now check using which number we got the curr ugly number 'next'. And incr the pointer of those number. 
            # we may have to incr more than one pointer at once like in num '6', '10' etc..
            if ugly[-1]== ugly[p2] * 2: p2+= 1
            if ugly[-1]== ugly[p3] * 3: p3+= 1
            if ugly[-1]== ugly[p5] * 5: p5+= 1
        return ugly[n-1]  # ugly[-1]

# Java
"""
class Solution {
    public int nthUglyNumber(int n) {
        List<Integer> ugly = new ArrayList<>();
        ugly.add(1);  // first ugly number is '1' only.  // list will automatically get maintained in sorted order.
        int p2 = 0, p3 = 0, p5 = 0;   // pointer to num 2,3,5. Number by which '2', 3 and 5 will get multiplied further.
        
        for (int i = 2; i <= n; i++) {
            int next = Math.min(ugly.get(p2) * 2, Math.min(ugly.get(p3) * 3, ugly.get(p5) * 5));  // will auto give number which won't be in the list.
            ugly.add(next);
            // now check using which number we got the curr ugly number 'next'. And incr the pointer of those number. 
            // we may have to incr more than one pointer at once like in num '6', '10' etc..
            if (next == ugly.get(p2) * 2) p2++;
            if (next == ugly.get(p3) * 3) p3++;
            if (next == ugly.get(p5) * 5) p5++;
        }
        return ugly.get(n - 1);  // ugly[-1]
    }
}
"""

# C++
"""
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> ugly;
        ugly.push_back(1);  // first ugly number is '1' only.  // list will automatically get maintained in sorted order.
        int p2 = 0, p3 = 0, p5 = 0;   // pointer to num 2,3,5. Number by which '2', 3 and 5 will get multiplied further.
        
        for (int i = 2; i <= n; i++) {
            int next = min({ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5});  // will auto give number which won't be in the list.
            ugly.push_back(next);
            // now check using which number we got the curr ugly number 'next'. And incr the pointer of those number. 
            // we may have to incr more than one pointer at once like in num '6', '10' etc..
            if (next == ugly[p2] * 2) p2++;
            if (next == ugly[p3] * 3) p3++;
            if (next == ugly[p5] * 5) p5++;
        }
        return ugly[n - 1];  // ugly[-1]
    }
};
"""