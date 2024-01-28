# logic for changing node or swapping node- phla: ek dummy node lena h corner case ko dekhte huye
#  jis node ko attach karna h wahan pe pointer chahiye and jis node se attach akrna h wahan pe pointer chahiye
# ye tmko lana h and then uske bad pointer change kar dena h

# note: nodes ko initialise us node se karo jahan tak wo worst case me sbse kam ja sake


class Node:
    # function(constructor) to initilaise Node object
    def __init__(self,data,next=None):
        self.data= data  # assign the data
        self.next= None  # Initialize next as null 


# swapping kth and (k+1)th node from end of the link list by swapping the data
# count will give the total no of nodes-1
# method 1:
def swap_two_node_last_values(self,k):
    first,second,third= self.head, self.head,self.head
    # now second will point to the kth element from the last
    # third will point to (k+1)th node from the end i.e one ele before 'second' from start
    count= 0   # count will give the total no of nodes-1
    while first.next:
        count+= 1
        first= first.next
        if count>=k:
            third= second
            second= second.next
    if count < k:  # value of k should be less than the no of elements in the list
        print("swapping not possible in this case")
    else:
        second.data,third.data= third.data, second.data


# method 2:
def swap_two_node_last_links(self,k):
    first,curr_x,pre_y, curr_y= self.head,self.head,None,None
    count= 0
    while first.next:
        first= first.next
        count+= 1
        if count>=k:
            pre_y= curr_y
            curr_y= curr_x
            curr_x= curr_x.next
    # now curr_x will point to the kth element from the last
    # curr_y  will point to (k+1)th node from the end
    # pre_y will point to the (k+2)th node from the end
    
    # if k >= no of elements 
    if count <k:
        print("swapping not possible in this case")
    # else update the pointers
    # case 1: there exist only two elements and (k+1)th= curr_y 
    # is a head node and kth is a last node
    elif curr_y== self.head and curr_x.next==None:
        self.head= curr_x
        curr_x.next= curr_y
        curr_y.next= None
    #case 2: when kth is a last node having elemenst greater than 2
    elif curr_x.next== None:
        curr_x.next= curr_y
        pre_y.next= curr_x
        curr_y.next= None
    # case 3: when (k+1)th node is first node(head) and kth node is 
    # not the last node(an internal node)
    elif curr_y== self.head and curr_x.next!= None:
        temp= curr_x.next
        curr_x.next= self.head
        curr_y.next= temp
        self.head= curr_x
    # case 4: when both are internal nodes
    else:
        temp= curr_x.next
        curr_x.next= curr_y
        curr_y.next= temp
        pre_y.next= curr_x


# method 2(best one):
# swapping kth and (k+1)th node from end of the linklist list by changing the links not by changing the data
# logic: create a dummy node to handle the corner cases like above one

def swap_two_node_last_links(self,k):
    dummy= Node(0)
    dummy.next= self.head
    first,second,pre_sec= dummy, dummy,dummy
    # second will point to (k+1)th ele from last and pre_sec will point to one node before second 
    count= 0  # no of nodes
    for i in range(k):
        first= first.next
        count+= 1
    while first.next:
        pre_sec= second
        second= second.next
        first= first.next
        count+= 1
    
    if count<= k:
        print("can't possible ")
        return
    # now swap the nodes 
    temp= second.next
    second.next= second.next.next
    temp.next= second
    pre_sec.next= temp
    
    # for printing
    llstr = ''
    current= dummy.next
    while current:
        llstr+= str(current.data) + "-->"
        current= current.next
    print(llstr)
