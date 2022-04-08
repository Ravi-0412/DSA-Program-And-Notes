# method 1
# using double pointer slow and fast(submitted on leetcode)
# slow will incr by one and fast will incr by two step 
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast will point to last node or none after the loop will break
        # slow will point to middle node and in case of even no of node
        # slow will point to next middle
        fast, slow= head, head
        # if no of elements in the list is even
        while fast:
            if fast.next: # internal stopping condition if no of elements 
                fast= fast.next.next      # is evenfast= fast.next.next
                slow= slow.next
            else:
                return slow            
        return slow
        # # if no of elements is odd
        # while first.next:
        #     slow= slow.next
        #     fast= fast.next.next


# method 2: by storing node in the array
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # just traverse the list and go on keeping the node in the array till arr[-1].next is not None
        # after that just return the middle ele of array 
        # since in array we can retrieve each node by index
        arr= [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr)//2]


# concise way of method 1:(best solution) 
# just combine the while and if loop of method 1
# same logic we do to check loop or not
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast= head, head
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        return slow

