class Node:
    def __init__(self,data,next= None):
        self.data= data
        self.next= next

class CircularQ:
    def __init__(self):
        self.front= None
        self.rear= None

    def Enqueue(self, data):
        node= Node(data)
        # check if empty
        if self.rear== None:
            self.front= node
            self.rear= node
            return
        else:
            self.rear.next= node
            self.rear= node
    
    def Dequeue(self):
        # check if empty
        if self.rear== None:
            print("queue is empty")
            return
        # check if only one ele is present
        if self.front.next== None:
            self.rear= None
            self.front= None
        # else just delete from first
        else:
            temp= self.front 
            self.front= self.front.next
    
    def show(self):
        # check if empty
        if self.rear== None:
            print("queue is empty")
            return
        else:
            curr= self.front
            print("elements present is: ", end=" ")
            while curr:
                print(curr.data, end=" ")
                curr= curr.next

Q= CircularQ()
Q.Enqueue(1)
Q.Enqueue(2)
Q.Enqueue(3)
Q.Enqueue(4)
Q.Dequeue()
# Q.Dequeue()
# Q.Dequeue()
# Q.Dequeue()
print()
Q.show()


        
