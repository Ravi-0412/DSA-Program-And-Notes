# this giving time out , have to look once again or ask someone
# on gfg
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        current= head
        while current!= None and current.next!= None:
            current1= current
            while current1.next!= None:
                if current.data== current1.next.data:
                    current1.next= current.next.next
                else:
                    current1= current1.next
            current= current.next
        return head


# using dictionary