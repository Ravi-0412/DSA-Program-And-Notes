class MyCircularQueue:
    
    def __init__(self, size: int):
        self.front = -1  # will point to index of 1st element
        self.rear = -1   # will point to index of last element
        self.size = size
        self.arr = [None for i in range(size)]

    def enQueue(self, value: int) -> bool:
        # check if full
        if self.isFull():
            return False
        # if queue is empty(self.front == self.rear== -1), inserting 1st element
        elif self.front == -1:  
            self.front, self.rear = 0,0   # make both '0'
            self.arr[self.rear] = value
        else:
            # if queue is not empty then add at rear
            self.rear = (self.rear + 1) % self.size  # move 'rear'
            self.arr[self.rear] = value
        return True

    def deQueue(self) -> bool:
        # check if empty
        if self.isEmpty():
            return False
        # check if there is only one ele present
        elif self.front == self.rear:
            temp = self.arr[self.front]   # element that will get poped
            self.arr[self.front] = None
            # Make both pointer = -1 since queue will become empty now
            self.front, self.rear = -1, -1
        else:
            # remove from front
            temp = self.arr[self.front]    # element that will get poped
            self.arr[self.front] = None
            self.front = (self.front + 1) % self.size # move 'front'
        return True

    def Front(self) -> int:
        # check if empty
        if self.isEmpty():
            return -1
        return self.arr[self.front]
        
    def Rear(self) -> int:
        # check if empty
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1
        

    def isFull(self) -> bool:
        return self.front == (self.rear + 1) % self.size


# Did by 'linklist also'.
# see file 'Circular_Q_Lists'

# java
"""
public class MyCircularQueue {

    private int[] arr;
    private int front, rear, size;

    public MyCircularQueue(int size) {
        this.size = size;
        this.arr = new int[size];
        this.front = -1;
        this.rear = -1;
    }

    public boolean enQueue(int value) {
        // Check if full
        if (isFull()) {
            return false;
        }
        // If queue is empty (front == rear == -1), inserting 1st element
        if (isEmpty()) {
            front = 0;
            rear = 0;
            arr[rear] = value;
        } else {
            // If queue is not empty, then add at rear
            rear = (rear + 1) % size;
            arr[rear] = value;
        }
        return true;
    }

    public boolean deQueue() {
        // Check if empty
        if (isEmpty()) {
            return false;
        }
        // Check if there is only one element present
        if (front == rear) {
            arr[front] = 0; // Clear the element (optional)
            front = -1;
            rear = -1;
        } else {
            // Remove from front
            arr[front] = 0; // Clear the element (optional)
            front = (front + 1) % size;
        }
        return true;
    }

    public int Front() {
        // Check if empty
        if (isEmpty()) {
            return -1;
        }
        return arr[front];
    }

    public int Rear() {
        // Check if empty
        if (isEmpty()) {
            return -1;
        }
        return arr[rear];
    }

    public boolean isEmpty() {
        return front == -1;
    }

    public boolean isFull() {
        return front == (rear + 1) % size;
    }
}

"""