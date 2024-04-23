# Method 1:
# just traverse the 1st linklist and store its address in hashmap with val =1(just any value)
# after that traverse the other linklist and check whether that node was in hashmap1
# it basically checking the address of the node, if equal then intesection point exist at that node
# other don't exist

# But it will take extra O(N) space
def getIntersectionNode(self, headA, headB) ->:
        curr1,curr2,hashmap1= headA, headB,{}
        while curr1:
            hashmap1[curr1]= 1
            curr1= curr1.next
        while curr2:
            if curr2 in hashmap1: 
                return curr2
            curr2= curr2.next
        return None

# find the diff in the length of linked list
# now move the linklist with greater length equal to the len_diff 
# now start moving the both linked list simultaneously and keep checking
# whether they point to the same Node
# if no common point exist then intersection point doesn't exist
# basically comapring the address of the nodes
# time: O(m+n)

class Solution:
    def getIntersectionNode(self, headA, headB):
        curr1,curr2, length1,length2= headA, headB, 0,0
        # find length of linklist1
        while curr1:
            length1,curr1= length1+ 1, curr1.next
        # find length of linklist2
        while curr2:
            length2,curr2= length2+ 1, curr2.next
        # find the diff and according call the function
        if length1>length2:
            d= length1-length2
            return self.IntersectionNode(d,headA,headB)  
        else:
            d= length2-length1
            return self.IntersectionNode(d,headB, headA)
    
    def IntersectionNode(self,d,head1,head2):
        curr1,curr2= head1,head2
        for i in range(d):
            curr1= curr1.next
        while curr1 and curr2:
            if curr1== curr2:  # if linklist from curr1 and curr2 is same
                               # in python all variable address will same if they point to the same data
                               # e.g:
                                    # a= 5
                                    # x=y=a
                                    # print(id(x),id(y))  # addres of both x and y will be same
                # print(id(curr1),id(curr2))  # here address of both will be same as they will be pointing to the same data like above
                return curr1
            curr1,curr2= curr1.next, curr2.next
        return None


# Try by this method also later
# https://leetcode.com/problems/intersection-of-two-linked-lists/solutions/49785/java-solution-without-knowing-the-difference-in-len/


