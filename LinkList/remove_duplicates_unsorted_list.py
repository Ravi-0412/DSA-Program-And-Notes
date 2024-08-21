# this giving time out(on gfg) ,but correct only
# time: O(n^2)
# logic: Just take each element one by one and search for its duplicates in the remaining list, just like we do for array(brute force)

# method 1: 
class Solution:
    def removeDuplicates(self, head):
        current= head
        while current and current.next: # have to check till 'n-1'
            current1= current
            while current1.next:  # this will go till end
                if current.data== current1.next.data:
                    current1.next= current1.next.next   # assuming the next node after that we checked may be distinct
                else:
                    # here current1 already be pointing to the distinct node than 'current' so simply we have to current1 one step ahead
                    current1 = current1.next
            # now current.next will point to the next distinct ele 
            current = current.next
        return head


# my mistakes for same approach above
class Solution:
    def removeDuplicates(self, head):
        current= head
        while current and current.next: 
            current1= current.next
            while current1:  
                if current.data== current1.data:
                    current1.next= current1.next.next   # this will give error like 'None type object has no attribute next'
                                                        # as we are blindly pointing to 'next.next' 
                                                        # we can blindly only point to one node ahead from the node we are sure
                                                        # so to avoid this use the above logic (method 1)
                else:
                    current1= current1.next
            # now current.next will point to the next distinct ele 
            current= current.next
        return head

# method 2:
# sort the list and apply the concept of removing duplicates from the sorted list
# time: O(nlogn)


# method 3:
# store the visited ele in set and for each ele whether that is present in set or not
# time: O(n), space: O(n)

def removeDuplicates(self, head):
        # Base case of empty list or
        # list with only one element
        if self.head is None or self.head.next is None:
            return head
        # Hash to store seen values
        hash = set()
        current = head
        hash.add(self.head.data)
        while current.next is not None:

            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next

        return head
