# Note: in Binary search mid will give the ans always. so for making any decision or condition in 'if' or 'while' loop, 
# just think from 'mid' i.e if it is not equal to mid then where to move for this 'if' condition.

# Note: for initialising 'low' and 'up' just find the range in which we can get the ans.
# and initialise 'low'= min range value and 'up'= maximum range value.
# After this use template 1 or template 2 or template 4 according to the Q.
# Note: Using above three template you can solve almost all Q of binary search, just think which template we can use here analysing the Q.

# 'up' hmesha '>=' or '>' target' me update hoga and low '<=' or '<' target me update hoga, 
# kyonki hmlog ko size hmesha decrease karna h.
# (Question ka meaning bhi thoda dhyan me rakhna h). Opposite fashion me bhi kam kar sakta h.
# e.g: "1283. Find the Smallest Divisor Given a Threshold".

# Template 1:
# Note: use this template in case if elements are not present then  we have to return some valid number, and
# if present  then simply we will get the ans inside the while loop.
# e.g: Q like: 1) find ceil and floor of a number in sorted array  2) find square root of a number  
# 3) Find 1st bad version 4) 744. Find Smallest Letter Greater Than Target 5) 35. Search Insert Position

# here while loop will only break when low>up then 'low' will give the ceil value(just greater than key) and 
# 'high' will give the floor value(just less than key) since 
# after while loop low will become '1' greater than 'high'.

# in case of duplicate ele it will give any index where it will find the ans first.
def binary_search(arr,key):
    n= len(arr)
    low=0
    up= n-1
    while(low<= up):
        mid= low+ (up-low)//2
        if arr[mid]== key:
            return mid
        elif(arr[mid]> key):  # mid ans deta but mid hi bda h to ab kahan 'key' hmko mil sakta h. mid se phle
            up= mid-1
        elif(arr[mid]<key):
            low= mid+1
    return -1

# arr= [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
# key= 1
# print(binary_search(arr, key))


# Template 2:  most important and most powerful template
# Note vvi: we use when we have to find the smallest amomg all possible ans.

# here after while loop will break then 'low' and 'high' will become equal.
# so any one of them will point to 'key' if key is present. After while loop both will point to the same thing.

# use this template when we are asked to return ans if present else simply return '-1'
# (or something fixed value given to return in case if not present) or given ans exist for sure.
# here we make decision after while loop only i.e what to return as final ans.
# e.g: search for an element in an array.

# Note: in case of duplicate elements, it will give the 1st index where ele is present.
# because even after finding the ans(>=), we are continuing our checking and shrinking the mid(decreasing the up).

# agar ans mil bhi gya ho(>=) to or range shrink karke(up ko decr karke) even or chota dhundho.

# here after while loop will break then 'low' and 'high' will become equal.
# so any one of them will point to 'key' if key is present.

# Note: low/high will give first element >= key.
# Note: And in case key > max(arr) then it will give last index.
# in this case to make low point beyond than 'n-1' , make up = n
# e.g: 2602. Minimum Operations to Make All Array Elements Equal.

def binary_search(arr,key):
    n= len(arr)
    low=0
    up= n-1
    while low < up:
        mid= low+ (up-low)//2
        if(arr[mid]>= key):    
            up= mid         # agar hmko target ele hi find karna h kisi smaller index pe then do this
        else:
            low= mid+1
    return low if arr[low]== key else -1
    
arr= [10, 10,20, 30, 50, 60, 80, 110, 110, 130, 140, 170]
key= 10
print(binary_search(arr, key))


# another form of template 2.
# note: use this when we have to work on <= condition and (mid and condition is acting in opposite fashion), 
# like incr mid will decrease the condition statement value and vice versa.
# used in Q "1283. Find the Smallest Divisor Given a Threshold".
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def isSum(mid):
            sum= 0
            for n in nums:
                sum+= math.ceil(n/mid)
            return sum

        start, end= 1, max(nums)
        while start < end:
            mid= start + (end - start)//2
            if isSum(mid) <= threshold:  # max we need to search till here only. search for even more less
                end= mid
            else:  # if isSum(mid) > threshold  => then we need to increase our 'mid' since we have to decr the total sum. And incr the mid will lower the sum and vice versa.
                start= mid + 1
        return start


# Note: Most of the binary search problem can be solved using these two(1 and 2) template with exact one or with slight modification 
# in while loop condidtion or in 'if' condition or both.
# after each Q, find out which template we can use and what modification we have to make acc to the Q.


# here after while loop will break then 'low' and 'high' will become equal.
# so any one of them will point to 'key' if key is present.

# Template 3:  same as Template 2()
# note: don't use this template. try to solve Q using template 1 and template 2 and template 4 only.
# will give TLE in many cases.


# Note vvi: in case of duplicate elements, it will give the last index where ele is present.
# because even after finding the ans, we are continuing our checking and increasing the mid(increasing the low).
# but doesn't work always to get the last index. may get TLE also . e.g" [10,10], key= 10
# so avoid this template to find the last index. 


def binary_search(arr,key):
    n= len(arr)
    low=0
    up= n-1
    while low < up:
        mid= low+ (up-low)//2
        if(arr[mid] <= key):    
            low= mid
        else:
            up= mid-1
    return low if arr[low]== key else -1
    
arr= [10, 10,20, 30, 50, 60, 80, 110, 110, 130, 140, 170]
key= 10
# print(binary_search(arr, key))


# to find the last index. basic one.
# template 1 only :

# Note VVI: agar hmko or bda khojna ho to yhi template use karo "while start<= end" and 
#  ek 'ans' variable leke update karte raho possible ans me and last me 'ans' ko return kar do.
# "while low<up" galat  ans de deta h, mostly case me.

# NOte VVI: agar or chota hi khojna ho to template 2 lagao aankh moon ke. kabhi fail nhi hoga.
def binary_search(nums,target):
    ans= -1
    start= 0
    end= len(nums)-1
    while start<= end:
        mid= start+ (end-start)//2
        # updaet ans and incr the start
        if nums[mid]== target:
            ans= mid  
            start= mid+1  # for finding larger index. means we have to find beyond mid
        elif nums[mid]> target:
            end= mid-1
        else:
            start= mid+1
    return ans

arr= [10, 10,20,20,20,20]
key= 20
print(binary_search(arr, key))

# Template 4: to find the last index       # most powerful after template 2.
#  Just consice way of above method(merge two if into one if).
# agar mil bhi jaye to 'low' ko aage badhate rhna h . isliye start wale condition me equal to lga do.
# template 1 only. yhi template ko use karna h ans milne ke bad bhi or bhi bda answer khojne ke liye.
# vvi: This template used in Q like: "Aggressive cows", ""

# Note: after while loop, end will point to the last index of target.
# as before while loop exit start had last index value since equal to(<=) condition with 'start') and
    # 'start' will point to the first greater ele than the 'target'.

# Note: end will give first element >= target.
# Note: And in case target > max(arr) then end = n.

def binary_search(nums,target):
    start= 0
    end= len(nums)-1
    while start<= end:
        mid= start+ (end-start)//2
        if nums[mid] <= target:   # isPossible(mid): 
            start= mid+1  # for finding larger index. means we have to find beyond mid
        else:
            end= mid-1

    return end  

arr= [10, 10, 10,10,20,20,20,20,20]
key= 10
print(binary_search(arr, key))

# Template 5
# Q: To find the 1st index of any target element
# agar mil bhi jaye to 'up' ko  ghatate(decrease) karte rhna h . isliye start wale condition me equal to lga do.

# Note: low will give first element <= target.
# Note: And in case key < min(arr) then low = 0.

def binary_search(arr,key):
    n= len(arr)
    low=0
    up= n-1
    while low<= up:
        mid= low+ (up-low)//2
        if(arr[mid]>= key):    
            up= mid-1        # agar hmko target ele hi find karna h kisi smaller index pe then do this
        else:
            low= mid+1
    # after while loop, low will point to the 1st index as before while loop exit 'up' was pointing 
    # to the required ans(due to '>=' condition with up).
    # 'up' will point to the greatest number smaller than the target.
    return low


# Note VVI: Array sorted ho ya unsorted ho, agar tm dekh pa rhe ki ans is given range me lie karega and 
# condition check karke agar decide kar pa rhe ho ki kon sa side move karna h.
# then apply Binary Search, no matter array is sorted or not.

# like agar ye condition agar follow kar rha then is side check karna h agar nhi kar rha to dusre side check karna h..
# then must apply Binary Search.

# Note Latest: Template1, template4, Template5 is enough to solve all the questions.
# So replace answers of all questions slowly slowly using these three templates only.
