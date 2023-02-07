
class Node:
    def __init__(self,data, pre= None, next= None):
        # when we dont pass any of the para it will take the default value
        self.pre= pre
        self.data= data
        self.next= next

class LinkList:
    def __init__(self):
        self.head= None

    def isEmpty(self):
        if self.head==None:
            return True
        return False

    def Insert_Beginning(self,data):
        node= Node(data)
        if self.head== None:
            self.head= node
        else:
            node.next= self.head
            self.head.pre= node
            self.head= node
    
    def Insert_Last(self, data):
        node= Node(data)
        if self.head== None:
            self.head= node
        else:
            current= self.head
            while current.next:
                current= current.next
            node.pre= current
            current.next= node

    def Delete_Node(self,key):
        if self.head== None:  # id linklist is empty
            print("Linklist empty you can't delete")
        elif self.head.data== key: # only one node is present and you want to delete that
            self.head= None
            return
        elif self.head.data== key:  # when you want to delete the 1st node and multiple nodes are present

            self.head= self.head.next
            self.head.pre= None
            return
        else: # means atleast two ele are there
            current= self.head
            while current.data!= key:
                current= current.next
                if current== None: # means key is not present
                    print("element not found") 
                    return                                       
            if current.next== None:   # if deleting last node
                current.pre.next= None
                current.pre= None
                return
            else:  # if neither last nor 1st(deleting node in between)
                current.pre.next= current.next
                current.next.pre= current.pre
                current.pre= None
                current.next= None
                return

    def show(self):
        if self.head== None:
            print("linklist in empty")
            return
        else:
            current= self.head
            ans= ''
            while current:
                ans+= '<-' + str(current.data) + '->'
                current= current.next
        print(ans)
   
first= LinkList()
first.Insert_Beginning(10)
first.Insert_Beginning(15)
first.Insert_Beginning(20)
first.Insert_Beginning(25)
first.Insert_Last(35)
first.Insert_Last(40)
first.Insert_Last(45)
# first.Delete_Node(45)
# first.Delete_Node(25)
# first.Delete_Node(40)
# first.Delete_Node(20)
first.Delete_Node(48)
first.show()