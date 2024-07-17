class MyCircularDeque:
    
    def __init__(self, size: int):
        self.front = -1  # will point to the index of 1st element
        self.rear = -1   # will point to the index of the last element
        self.size = size
        self.arr = [None for _ in range(size)]

    def insertFront(self, value: int) -> bool:
        # check if full
        if self.isFull():
            return False
        # if deque is empty
        elif self.isEmpty():
            self.front, self.rear = 0, 0
            self.arr[self.front] = value
        else:
            # move front backward
            self.front = (self.front - 1 + self.size) % self.size
            self.arr[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        # check if full
        if self.isFull():
            return False
        # if deque is empty
        elif self.isEmpty():
            self.front, self.rear = 0, 0
            self.arr[self.rear] = value
        else:
            # move rear forward
            self.rear = (self.rear + 1) % self.size
            self.arr[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        # check if empty
        if self.isEmpty():
            return False
        # if there is only one element present
        elif self.front == self.rear:
            self.arr[self.front] = None
            self.front, self.rear = -1, -1
        else:
            self.arr[self.front] = None
            # Move front ahead
            self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        # check if empty
        if self.isEmpty():
            return False
        # if there is only one element present
        elif self.front == self.rear:
            self.arr[self.rear] = None
            self.front, self.rear = -1, -1
        else:
            self.arr[self.rear] = None
            # move 'rear' backward
            self.rear = (self.rear - 1 + self.size) % self.size
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return self.front == (self.rear + 1) % self.size

# Java
"""
public class MyCircularDeque {

    private int[] arr;
    private int front, rear, size;

    public MyCircularDeque(int size) {
        this.size = size;
        this.arr = new int[size];
        this.front = -1;
        this.rear = -1;
    }

    public boolean insertFront(int value) {
        // Check if full
        if (isFull()) {
            return false;
        }
        // If deque is empty
        if (isEmpty()) {
            front = 0;
            rear = 0;
            arr[front] = value;
        } else {
            // Move front backward
            front = (front - 1 + size) % size;
            arr[front] = value;
        }
        return true;
    }

    public boolean insertLast(int value) {
        // Check if full
        if (isFull()) {
            return false;
        }
        // If deque is empty
        if (isEmpty()) {
            front = 0;
            rear = 0;
            arr[rear] = value;
        } else {
            // Move rear forward
            rear = (rear + 1) % size;
            arr[rear] = value;
        }
        return true;
    }

    public boolean deleteFront() {
        // Check if empty
        if (isEmpty()) {
            return false;
        }
        // If there is only one element present
        if (front == rear) {
            arr[front] = 0; // Clear the element (optional)
            front = -1;
            rear = -1;
        } else {
            arr[front] = 0; // Clear the element (optional)
            // Move front ahead
            front = (front + 1) % size;
        }
        return true;
    }

    public boolean deleteLast() {
        // Check if empty
        if (isEmpty()) {
            return false;
        }
        // If there is only one element present
        if (front == rear) {
            arr[rear] = 0; // Clear the element (optional)
            front = -1;
            rear = -1;
        } else {
            arr[rear] = 0; // Clear the element (optional)
            // Move rear backward
            rear = (rear - 1 + size) % size;
        }
        return true;
    }

    public int getFront() {
        if (isEmpty()) {
            return -1;
        }
        return arr[front];
    }

    public int getRear() {
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