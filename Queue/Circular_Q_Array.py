class CircularQ:
    def __init__(self,size):
        self.front= -1
        self.rear= -1
        self.size= size
        self.arr= [None for i in range(size)]
    
    def Enqueue(self,data):
        # check if full
        if self.front== (self.rear +1)% self.size:
            print("queue is full")
        elif self.front== -1:   # if empty  OR self.front== self.rear== -1
            self.front, self.rear= 0,0   # make both '0'
            self.arr[self.rear]= data
        else:
            self.rear= (self.rear+1)%self.size   # to handle the case when rear is pointing to last index and we have space at starting indices
            self.arr[self.rear]= data
    
    def Dequeue(self):
        # check if empty
        if self.front== -1:
            print("empty Queue")
        # check if there is only one ele present
        elif self.front== self.rear:
            temp= self.arr[self.front]
            self.arr[self.front]= None
            self.front= -1
            self.rear= -1
            print("element deleted is: ",temp)
        else:
            temp= self.arr[self.front]
            self.arr[self.front]= None
            self.front= (self.front+1)%self.size  # to handle the case when front is pointing to last index and rear to starting indices
            print("element deleted is: ",temp)

    def show(self):
        if self.front== -1:
            print("empty Queue")
            return
        print("elements present is:", end= " ")
        # we have to show from index of 'front' to index of 'rear'
        if self.front<= self.rear:  # means rear on right side of front
                                    # so simply print from front till rear
            for i in range(self.front, self.rear+1):
                print(self.arr[i], end=" ")
        
        else: # means front is greater than rear
              # rear lies left of front
            # first print till end of the arr from front
            for i in range(self.front, self.size):
                print(self.arr[i], end=" ")
            # then print from index zero to rear
            for i in range(0,self.rear+1):
                print(self.arr[i], end=" ")

    
    def getSize(self):
        count= 0
        for num in self.arr:
            if num!= None:
                count+= 1
        print("no of ele present is: ", count)
    
Q= CircularQ(6)
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
print()
Q.getSize()



            

