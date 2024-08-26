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
        if self.front == -1:  
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
        if self.front == self.rear:
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

# Using Linkedlist 
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class MyCircularQueue:
    def __init__(self, size: int):
        self.size = size
        self.current_size = 0  # To keep track of the current number of elements
        self.front = None  # Will point to the front node
        self.rear = None   # Will point to the rear node

    def enQueue(self, value: int) -> bool:
        # Check if the queue is full
        if self.isFull():
            return False
        
        # Create a new node
        new_node = Node(value)
        
        # If the queue is empty, initialize the front and rear to this new node
        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
            new_node.next = self.front  # Circular link
        else:
            # Otherwise, add the new node at the end and update the rear pointer
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  # Maintain the circular nature
        
        self.current_size += 1
        return True

    def deQueue(self) -> bool:
        # Check if the queue is empty
        if self.isEmpty():
            return False
        
        # If there is only one element in the queue
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            # Otherwise, remove the front element and update the front pointer
            self.front = self.front.next
            self.rear.next = self.front  # Maintain the circular nature
        
        self.current_size -= 1
        return True

    def Front(self) -> int:
        # Check if the queue is empty
        if self.isEmpty():
            return -1
        return self.front.value

    def Rear(self) -> int:
        # Check if the queue is empty
        if self.isEmpty():
            return -1
        return self.rear.value

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.current_size == self.size


# java
"""
class Node {
    int value;
    Node next;

    public Node(int value) {
        this.value = value;
        this.next = null;
    }
}

class MyCircularQueue {
    private int size;
    private int currentSize;
    private Node front;
    private Node rear;

    public MyCircularQueue(int size) {
        this.size = size;
        this.currentSize = 0;
        this.front = null;
        this.rear = null;
    }

    public boolean enQueue(int value) {
        // Check if the queue is full
        if (isFull()) {
            return false;
        }

        // Create a new node
        Node newNode = new Node(value);

        // If the queue is empty, initialize the front and rear to this new node
        if (isEmpty()) {
            front = newNode;
            rear = newNode;
            rear.next = front; // Circular link
        } else {
            // Otherwise, add the new node at the end and update the rear pointer
            rear.next = newNode;
            rear = newNode;
            rear.next = front; // Maintain the circular nature
        }

        currentSize++;
        return true;
    }

    public boolean deQueue() {
        // Check if the queue is empty
        if (isEmpty()) {
            return false;
        }

        // If there is only one element in the queue
        if (front == rear) {
            front = null;
            rear = null;
        } else {
            // Otherwise, remove the front element and update the front pointer
            front = front.next;
            rear.next = front; // Maintain the circular nature
        }

        currentSize--;
        return true;
    }

    public int Front() {
        // Check if the queue is empty
        if (isEmpty()) {
            return -1;
        }
        return front.value;
    }

    public int Rear() {
        // Check if the queue is empty
        if (isEmpty()) {
            return -1;
        }
        return rear.value;
    }

    public boolean isEmpty() {
        return currentSize == 0;
    }

    public boolean isFull() {
        return currentSize == size;
    }
}
"""