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

# Java
"""
// Node class for doubly linked list
class Node {
    int data;      // Data stored in the node
    Node pre;      // Pointer to the previous node
    Node next;     // Pointer to the next node

    // Constructor to initialize Node object
    public Node(int data) {
        this.data = data;  // Assign the data
        this.pre = null;   // Initialize previous pointer as null
        this.next = null;  // Initialize next pointer as null
    }
}

// LinkedList class
class LinkedList {
    Node head;   // Head of the linked list (points to the first node)

    // Constructor to initialize LinkedList object
    public LinkedList() {
        this.head = null;  // Initially, the list is empty
    }

    // Check if the linked list is empty
    public boolean isEmpty() {
        return head == null;
    }

    // Insert a new node at the beginning of the list
    public void insertAtBeginning(int data) {
        Node node = new Node(data);  // Create a new node
        if (head == null) {
            head = node;             // If list is empty, set the head to the new node
        } else {
            node.next = head;        // New node's next points to the current head
            head.pre = node;         // Current head's previous points to the new node
            head = node;             // Update the head to the new node
        }
    }

    // Insert a new node at the end of the list
    public void insertAtLast(int data) {
        Node node = new Node(data);  // Create a new node
        if (head == null) {
            head = node;             // If list is empty, set the head to the new node
        } else {
            Node current = head;
            while (current.next != null) {  // Traverse to the end of the list
                current = current.next;
            }
            node.pre = current;      // New node's previous points to the last node
            current.next = node;     // Last node's next points to the new node
        }
    }

    // Delete a node by its key (data)
    public void deleteNode(int key) {
        if (head == null) {  // If the list is empty
            System.out.println("LinkedList is empty, you can't delete");
            return;
        }
        if (head.data == key) {  // If the node to be deleted is the head
            if (head.next == null) {
                head = null;  // If only one node is present, delete it
            } else {
                head = head.next;  // If multiple nodes, update the head
                head.pre = null;
            }
            return;
        }
        Node current = head;
        while (current != null && current.data != key) {  // Traverse to find the node
            current = current.next;
        }
        if (current == null) {  // If the key was not found
            System.out.println("Element not found");
            return;
        }
        if (current.next == null) {  // If the node to be deleted is the last node
            current.pre.next = null;
        } else {  // If the node to be deleted is in between
            current.pre.next = current.next;
            current.next.pre = current.pre;
        }
        current.pre = null;  // Clear the references of the current node
        current.next = null;
    }

    // Display the elements of the linked list
    public void show() {
        if (head == null) {
            System.out.println("LinkedList is empty");
            return;
        }
        Node current = head;
        StringBuilder result = new StringBuilder();
        while (current != null) {
            result.append("<-").append(current.data).append("->");
            current = current.next;
        }
        System.out.println(result.toString());
    }

    // Main method to test the functionality
    public static void main(String[] args) {
        LinkedList first = new LinkedList();

        // Test cases for inserting at the beginning
        first.insertAtBeginning(10);
        first.insertAtBeginning(15);
        first.insertAtBeginning(20);
        first.insertAtBeginning(25);

        // Test cases for inserting at the last
        first.insertAtLast(35);
        first.insertAtLast(40);
        first.insertAtLast(45);

        // Uncomment to test delete operations
        // first.deleteNode(45);  // Delete last node
        // first.deleteNode(25);  // Delete first node
        // first.deleteNode(40);  // Delete node from middle
        // first.deleteNode(20);  // Delete another node
        first.deleteNode(48);  // Trying to delete a non-existing node

        // Show the final state of the linked list
        first.show();
    }
}
"""