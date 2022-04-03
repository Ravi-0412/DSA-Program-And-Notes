# stack_right and tack_left is not modifying when passing yto other function
# have to look later very important concept of python
class Solution:
    stack_right, stack_left= [], []
    def largestRectangleArea(self, heights: List[int]) -> int:
        # first finding the next smaller right
        global stack_right
        global stack_left
        print(stack_right)
        area= 1
        for i in range(len(heights)):
            right= self.nextSmallerRight(heights, stack_right, i)
            left=  self.nextSmallerLeft(heights,stack_left, i)
            print(stack_left)
            print(stack_right)
            print("right= ", right)
            print(" left=", left)
            
    def nextSmallerRight(self,arr,stack_right, index):
        # this function needs some modification, we will do after passing function will work
        if index== len(arr)-1:
            return len(arr)
        for i in range(len(arr)-1,index,-1):
            while stack_right and stack_right[-1]>=arr[i]:
                stack_right.pop()
            if stack_right== []:  # no next smaller right exist
                return len(arr)  # means that height can go till 'len(arr)-1' on right side
                stack_right.append(arr[i])
            else:
                return arr.index(stack_right[-1])     # means on left side it can go before this index val 
                stack_right.append(arr[i])
    
    def nextSmallerLeft(self,arr,stack_left, index):
        if index==0:
            return -1
        for i in range(index):
            while stack_left and stack_left[-1]>=arr[i]:
                stack_left.pop()
            if stack_left== []:  # no next smaller left ele exist
                return -1        # means it can go till 'index=0' on left side 
                stack_left.append(arr[i])
            else:  # means we have got the next smaller left
                return arr.index(stack_left[-1])   # means on left side it can go before this index val
                stack_left.append(arr[i])

# this also not working
# have to look later
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_smaller= self.nextSmallerLeft(heights)     # will conatin the indices of next smaller left for each ele
        right_smaller= self.nextSmallerRight(heights)   # will conatin the indices of next smaller right for each ele
        # indices in above array will denote that before that index 
        # the given ele can expand in right and left side 
        print(left_smaller)
        print(right_smaller)
        area= 0
        # now find the area for each height from the above range you got
        for i in range(len(heights)):
            width= right_smaller[i]- left_smaller[i]- 1 
            area= max(area, width*heights[i])
        return area
    
    def nextSmallerLeft(self,arr):
        # at last while returning the values retrun the indices
        # ans will store here the indices
        stack= []
        ans= []
        for i in range(len(arr)):
            count= 1
            while stack and stack[-1]>=arr[i]:
                stack.pop()
                count+= 1
            if stack== []:
                ans.append(-1)  #
                stack.append(arr[i])
            else:
                # ans.append(arr.index(stack[-1]))   # this will give the index from start
                                                   # but we need the index of the next smaller left in case of duplicates
                ans.append(i-count)    # above one was not working so took count and did like this
                stack.append(arr[i])
        return ans
            
    def nextSmallerRight(self,arr):
        stack= []
        ans= []
        for i in range(len(arr)-1,-1,-1):
            count= 1
            while stack and stack[-1]>=arr[i]:
                stack.pop()
                count+= 1
            if stack== []:
                ans.append(len(arr))
                stack.append(arr[i])
            else:
                # ans.append(arr.index(stack[-1]))    # not woking same reason as above
                ans.append(i+count)
                stack.append(arr[i])
        result= ans[::-1]
        return result    



# correct one but by bruite force so all test cases not running
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area= 0
        for i in range(len(heights)):
            left_smaller= self.nextSmallerLeft(heights, i)     
            right_smaller= self.nextSmallerRight(heights, i)
            width= right_smaller- left_smaller- 1 
            area= max(area, width*heights[i])
        return area
    
    def nextSmallerLeft(self,arr, index):
        j= index - 1
        while j>= 0 and arr[j]>= arr[index]:
            j-= 1
        return j
    def nextSmallerRight(self,arr, index):
        j= index + 1
        while j<len(arr) and arr[j]>= arr[index]:
            j+= 1
        return j



# this i solved after a lot of time after seeing videos 2-3 times
# jb koi bda ele dikhega index pe on comparison to heights[top of stack] tb 
# ele ko pop karte rhna h stack se  and poped ele ke liye area calculate karte rhna h 
# jb tak koi chota ele index wale se na mil jata ho 
# agar pop karne ke bad stack empty ho jaye matlab stack[poped one] curr index tak ja sakta h(right side me)
# means ye poped ele abhi tak ka sbse chota ele tha stack me(index wale ko chod ke)
# isliye is case me direct index se multiply karna h. It also means that all the pre bars in 
# the stack was greater than the curr index bar

# agar poped karne ke bad bhi ele rhta h iska matlab ki top of stack jo hoga
# poped ele ka left margin hoga(matlab iske phle left me poped wala ja sakta h)
# actually stack me insert hi next smaller left ho rha har ele se phle 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:        
        maxArea, stack, index= 0, [], 0
        while(index < len(heights)):
            if not stack or heights[index] >= heights[stack[-1]]:   # just push index in the stack and incr the index
                stack.append(index)
                index+= 1
            else:   # if heights[index] < heights[stack[-1]]  means right marging mil gya poped ele ka..
                    # right side me iske phle tak ja sakta h 
                topOfStack= stack.pop()
                currArea= heights[topOfStack] *((index- stack[-1]-1) if stack else index)  
                maxArea= max(currArea, maxArea)
        while stack:
            topOfStack= stack.pop()
            currArea= heights[topOfStack] *((index- stack[-1]-1) if stack else index)
            maxArea= max(currArea, maxArea)
        return maxArea


# very concise and good one
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/995249/Python-increasing-stack-explained
# whenever you see any ele greater than equal on the stack to the current index
# then just calculate the area like above method 
# it just finding the next smaller and stopping there
def largestRectangleArea(self, heights):        
    stack, area= [], 0
    for i ,h in enumerate(heights+ [0]): # to evaluate the last ele, just append with smallest ele
        while stack and heights[stack[-1]]>= h:
            # h= heights[stack.pop()]             # will give the wrong result as h you are using for iterating also
                                                # this mistake i was making and got after a long time
            H= heights[stack.pop()] 
            W= i if not stack else i-stack[-1]-1
            area= max(area, H*W)
        stack.append(i)
    return area