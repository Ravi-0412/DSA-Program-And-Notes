# Note: In linklist, if you want to break the link between any two node OR
# if you want to connect any two node that can be done by using 'ptr.next' only (next must be there with pointer name)

# Note: every pointer stores the address of the pointing node(reference creation) so, if you change the address of any pointer pointing to the same node using 'ptr.next'
# then next node pointed by all the pointers to that node will change because you are changing the address


class Node:
    # function(constructor) to initilaise Node object
    def __init__(self,data,next=None):
        self.data= data  # assign the data
        self.next= None  # Initialize next as null 

class LinkedList:
    # function(constructor) to initilaise LinkedList object
    def __init__(self):
        self.head= None  # initialsing LinkedList object 'head' to None intially
                         # 'head' will always point to the first node
    def isempty(self):
        if self.head== None:
            return True
        return False                     

    def insert_at_begining(self,data):
        # node= Node(data,self.head)  # 'next' value of the inserting node
                                    # will be your current head if you will
                                    # pass 'self.head' as parameter then
        # node.next= self.head         # when passing 'self.head' as parameter then
                                     # then no need of writing this line
        node= Node(data)
        node.next= self.head  #'next' value of the inserting node
                              # will be your current head
        self.head= node              #'head' will now point to the inserting node
    
    def insert_last(self,data):
        node= Node(data)
        current= self.head
        if self.head is None:
            self.head= node
            node.next= None
        else:
            while current.next:
                current= current.next
            current.next= node
            node.next= None

    # to insert a list of values after wiping all the current values
    def insert_values(self,data_list):
        self.head= None  # this will wipe out all the current values
        n= len(data_list)
        for num in data_list:
            self.insert_last(num)

    def show(self):
        if self.head is None:
            print("linked list is empty")
            return
        current= self.head
        llstr= ''
        while current:
            llstr+= str(current.data) + '-->'
            current= current.next
        print(llstr)
    def get_length(self):
        current= self.head
        count= 0
        while current:
            count+= 1
            current= current.next
        print("no of elements in linked list is: ", count)

    # # removing the elements at given index
    def remove_at(self,index):
        current,pre= self.head, None
        # current will point to the index that we have to delete at final
        # pre will point one location before the index
        for i in range(index):
            pre= current 
            current= current.next
        pre.next= current.next # make next of pre point to next node after index value
        # current.next= None  # make the next of index as ' None'    # no need to even write this

    
    # swapping kth and (k+1)th node from end of the link list by swapping the data
    # count will give the total no of nodes-1
    # def swap_two_node_last_values(self,k):
    #     first,second,third= self.head, self.head,self.head
    #     count= 0   # count will give the total no of nodes-1
    #     while first.next:
    #         count+= 1
    #         first= first.next
    #         if count>=k:
    #             third= second
    #             second= second.next
    #     # now second will point to the kth element from the last
    #     # third will point to (k+1)th node from the end i.e one ele before 'second' from start
    #     # after this swap the data of both
    #     if count <k:
    #         print("swapping not possible in this case")
    #     else:
    #         second.data,third.data= third.data, second.data


    # #swapping kth and (k+1)th node from end of the linklist list by changing the links not by changing the data
    # #same logic can be applied to swapping any two given nodes of at any position
    # #just first find the position of nodes and update the pointers 
    # #accordinbg to the cases
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
# case 1, case 2, case 3
#     def swap_two_node_last_links1(self,k):
#         dummy= Node(0)
#         dummy.next= self.head
#         first,curr_x,pre_y, curr_y= self.head,self.head,dummy,dummy
#         count= 0
#         while first.next:
#             first= first.next
#             count+= 1
#             if count>=k:
#                 pre_y= curr_y
#                 curr_y= curr_x
#                 curr_x= curr_x.next
#         if count <k:
#             print("swapping not possible in this case")
#         else:
#             pre_y.next= curr_x
#             curr_y.next= curr_x.next
#             curr_x.next= curr_y

#         # for getting the actual link list after swap
#         # start printing from dummy.next beacuse in this 
#         # approach we are not changing the head
#         llstr = ''
#         current= dummy.next
#         while current:
#             llstr+= current.data + "-->"
#             current= current.next
#         print(llstr)






if __name__ == "__main__":
    l1= LinkedList()
    # l1.insert_at_begining(5)
    # l1.insert_at_begining(85)
    # l1.insert_last(67)
    # l1.insert_last(23)
    # test cases for swapping function
    # arr= ['mango','apple','banana','grapes','orange','pineapple','potato','onion']
    arr= [1,2,3,4,5]
    # arr= [1,2]
    # arr= [1,2,3]
    l1.insert_values(arr)
    l1.show()
    # l1.swap_two_node_last_values(2)
    # l1.show()
    l1.swap_two_node_last_links(2)
    l1.show()
    # l1.swap_two_node_last_links1(7)
    l1.remove_at(2)
    l1.show()
    # l1.get_length()







    

