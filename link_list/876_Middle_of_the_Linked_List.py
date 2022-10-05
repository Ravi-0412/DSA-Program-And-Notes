# method 1: find the length and again traverse till middle

# method 2: better than all
# using double pointer slow and fast(submitted on leetcode)
# slow will incr by one and fast will incr by two step 
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast will point to last node or none after the loop will break
        # slow will point to middle node and in case of even no of node
        # slow will point to next middle
        fast, slow= head, head
        # if no of elements in the list is even
        while fast and fast.next: # if fast== None it means 'even' no of elements and if fast.next== None it means 'even' no of elements
            fast= fast.next.next      # is evenfast= fast.next.next
            slow= slow.next           
        return slow


# method 3: by storing node in the array
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # just traverse the list and go on keeping the node in the array till arr[-1].next is not None
        # after that just return the middle ele of array 
        # since in array we can retrieve each node by index
        arr= [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr)//2]




