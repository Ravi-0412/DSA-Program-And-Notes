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
        self.successor= None   # global variable for reversing first n node
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



# method 2(best one):
# swapping kth and (k+1)th node from end of the linklist list by changing the links not by changing the data
# logic: create a dummy node to handle the corner cases like above one
    def swap_two_node_last_links(self,k):
        dummy= Node(0)
        dummy.next= self.head
        first,second,pre_sec= dummy, dummy,None
        count= 0
        # second will point to (k+1)th ele from last and pre_sec will point to one node before second 
        for i in range(k):
            first= first.next
            count+= 1
        print(first.data,second.data)
        while first.next:
            pre_sec= second
            second= second.next
            first= first.next
            count+= 1
        print(first.data,second.data)
        
        if count<= k:
            print("can't possible ")
            return
        temp= second.next
        second.next= second.next.next
        temp.next= second
        pre_sec.next= temp

        
        llstr = ''
        current= dummy.next
        while current:
            llstr+= str(current.data) + "-->"
            current= current.next
        print(llstr)

    def ReverseN(self, head, n):
        if n==1:
            self.successor= head.next   # storing the first node after 'n' into successor
            return head
        reverseHead= self.ReverseN(head.next, n-1)
        head.next.next= head
        head.next= self.successor   # at last first node(head) will point to the first node after 'n'
        return reverseHead


if __name__ == "__main__":
    l1= LinkedList()
    # l1.insert_at_begining(5)
    # l1.insert_at_begining(85)
    # l1.insert_last(67)
    # l1.insert_last(23)
    # test cases for swapping function
    # arr= ['mango','apple','banana','grapes','orange','pineapple','potato','onion']
    arr= [1,2,3,4,5,6,7]
    # arr= [1,2]
    # arr= [1,2,3]
    l1.insert_values(arr)
    l1.show()
    # l1.swap_two_node_last_values(2)
    # l1.show()
    # l1.swap_two_node_last_links(1)
    # l1.show()
    # l1.swap_two_node_last_links1(7)
    # l1.remove_at(2)
    # l1.show()
    # l1.get_length()
    l1.ReverseN(l1.head,5)
    l1.show()

# java
"""
// Node class for LinkedList
class Node {
    int data;       // Data stored in the node
    Node next;      // Pointer to the next node in the list

    // Constructor to initialize Node object
    public Node(int data) {
        this.data = data;  // Assign the data
        this.next = null;  // Initialize next as null
    }
}

// LinkedList class
class LinkedList {
    Node head;      // Head of the LinkedList (points to the first node)

    // Constructor to initialize LinkedList object
    public LinkedList() {
        this.head = null;  // Initially the list is empty
    }

    // Check if the LinkedList is empty
    public boolean isEmpty() {
        return head == null;
    }

    // Insert a new node at the beginning of the LinkedList
    public void insertAtBeginning(int data) {
        Node node = new Node(data);   // Create a new node
        node.next = head;             // The new node's next will point to the current head
        head = node;                  // Now, the head points to the newly inserted node
    }

    // Insert a new node at the end of the LinkedList
    public void insertLast(int data) {
        Node node = new Node(data);  // Create a new node
        if (head == null) {
            head = node;             // If the list is empty, set the head to the new node
        } else {
            Node current = head;     // Start from the head and traverse to the end of the list
            while (current.next != null) {
                current = current.next;
            }
            current.next = node;     // At the end, point the last node to the new node
        }
    }

    // Insert values from an array into the LinkedList, wiping out current values
    public void insertValues(int[] data_list) {
        head = null;                 // Clear the existing list by setting head to null
        for (int num : data_list) {
            insertLast(num);         // Insert each element of the array at the end of the list
        }
    }

    // Display the elements of the LinkedList
    public void show() {
        if (head == null) {
            System.out.println("Linked list is empty");
            return;
        }
        Node current = head;
        StringBuilder llstr = new StringBuilder();
        while (current != null) {
            llstr.append(current.data).append("-->");
            current = current.next;
        }
        llstr.append("null");  // Append "null" at the end to indicate the end of the list
        System.out.println(llstr.toString());
    }

    // Get the length of the LinkedList
    public int getLength() {
        Node current = head;
        int count = 0;
        while (current != null) {
            count++;
            current = current.next;
        }
        System.out.println("Number of elements in linked list is: " + count);
        return count;
    }

    // Remove the node at the given index
    public void removeAt(int index) {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }
        if (index == 0) {
            head = head.next;  // If index is 0, just move the head to the next node
            return;
        }
        Node current = head;
        Node prev = null;
        for (int i = 0; i < index; i++) {
            prev = current;            // Track the node before the node to be removed
            current = current.next;    // Move to the next node
            if (current == null) {     // If the index is out of range
                System.out.println("Index out of bounds");
                return;
            }
        }
        prev.next = current.next;  // Link the previous node to the node after the current node
    }

    // Main function to test LinkedList functionality
    public static void main(String[] args) {
        LinkedList l1 = new LinkedList();

        // Test case: insert at beginning
        l1.insertAtBeginning(5);
        l1.insertAtBeginning(85);
        l1.show(); // Expected output: 85-->5-->null

        // Test case: insert at last
        l1.insertLast(67);
        l1.insertLast(23);
        l1.show(); // Expected output: 85-->5-->67-->23-->null

        // Test case: insert values from an array
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        l1.insertValues(arr);
        l1.show(); // Expected output: 1-->2-->3-->4-->5-->6-->7-->null

        // Additional test case: insert values from a smaller array
        int[] arr2 = {1, 2};
        l1.insertValues(arr2);
        l1.show(); // Expected output: 1-->2-->null

        // Additional test case: insert values from another array
        int[] arr3 = {1, 2, 3};
        l1.insertValues(arr3);
        l1.show(); // Expected output: 1-->2-->3-->null
    }
}
"""







    

