# Basic
"""
1) Visit
When you visit any url after current url then all it's forward history won't be available.
fresh forward history will start. 
2) Back & forwrd:
You need to keep track of what all url visited , back & forth from the current one.
"""

# Method 1:
"""
Using Doubly LinkList so that we can move backward and forward. 

Time Complexity:
  visit(url): O(1) — You just attach a new node.
  back(steps): O(steps) — In the worst case, you might traverse the entire list.
  forward(steps): O(steps) — Same as back, you travel node by node.
Space Complexity: O(N) where N is the total number of URLs visited. Every URL is stored in a node.
"""

class DoublyLinkedList:
    def __init__(self, value):
        self.val = value
        self.pre = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        # We only need to track where we are currently standing
        self.cur = DoublyLinkedList(homepage)
        
    def visit(self, url: str) -> None:
        newNode = DoublyLinkedList(url)
        # Connect the current node to the new node
        self.cur.next = newNode
        newNode.pre = self.cur
        # Move current to the new page
        self.cur = newNode
        # Forward history is cleared automatically because 
        # newNode.next is None by default
        
    def back(self, steps: int) -> str:
        # Move back until we run out of steps OR hit the very first page
        while steps > 0 and self.cur.pre:
            self.cur = self.cur.pre
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        # Move forward until we run out of steps OR hit the latest visited page
        while steps > 0 and self.cur.next:
            self.cur = self.cur.next
            steps -= 1 # Fixed the += mistake
        return self.cur.val

# Method 2:
"""
Most Optimised one: Dynamic Array

Logic:
Store history in a list.
Maintain a current_idx for where the user is.
Maintain a last_idx to mark the "end" of the valid forward history.
visit: Add the URL at current_idx + 1 and reset the last_idx to this new position.
back/forward: Simply update the current_idx using max and min bounds.

Time Complexity:
  visit(url): O(1) — You just attach a new node.
  back(steps): O(1) — Direct Jump
  forward(steps): O(1) — Direct Jump
Space Complexity: O(N) where N is the total number of URLs visited. Every URL is stored in a node.

"""

class BrowserHistory:
    def __init__(self, homepage: str):
        # We start with the homepage at index 0
        self.history = [homepage]
        self.current_idx = 0
        self.last_idx = 0  # This marks the boundary of 'forward' history

    def visit(self, url: str) -> None:
        self.current_idx += 1
        
        # If we are visiting a new page, we clear the forward history.
        # In an array, we just overwrite the next element.
        if self.current_idx < len(self.history):
            self.history[self.current_idx] = url
        else:
            self.history.append(url)
            
        # Any 'forward' history beyond this point is now invalid
        self.last_idx = self.current_idx

    def back(self, steps: int) -> str:
        # Jump back directly! O(1)
        self.current_idx = max(0, self.current_idx - steps)
        return self.history[self.current_idx]

    def forward(self, steps: int) -> str:
        # Jump forward directly! O(1)
        self.current_idx = min(self.last_idx, self.current_idx + steps)
        return self.history[self.current_idx]


# Method 3:
"""
Using Two Stack

1) curStack (The Past): This holds everything from your current page back to the homepage. The top of this stack is always your current page.
2) forwardHistoryStack (The Future): This holds the pages you've gone "back" from. When you visit a new page, this stack is thrown away.

Time Complexity:
  visit(url): O(1) — You just attach a new node.
  back(steps): O(steps) — In the worst case, you might traverse the entire list.
  forward(steps): O(steps) — Same as back, you travel node by node.
Space Complexity: O(N) where N is the total number of URLs visited. Every URL is stored in a node.
"""

class BrowserHistory:

    def __init__(self, homepage: str):
        # curStack: The bottom is the homepage, the top is the current page
        self.curStack = [homepage]
        # forwardHistoryStack: Stores pages we've retreated from via 'back'
        self.forwardHistoryStack = []

    def visit(self, url: str) -> None:
        # Step 1: Visiting a new page clears all 'forward' history
        # You can't go 'forward' after choosing a new path
        self.forwardHistoryStack = []
        
        # Step 2: Add the new page to our current history
        self.curStack.append(url)
        
    def back(self, steps: int) -> str:
        # Move pages from curStack to forwardHistoryStack
        # We must leave at least ONE node in curStack (the homepage)
        while steps > 0 and len(self.curStack) > 1:
            # Pop from history and push into the 'forward' stack
            last_page = self.curStack.pop()
            self.forwardHistoryStack.append(last_page)
            steps -= 1
            
        # The current page is always at the top of the curStack
        return self.curStack[-1]

    def forward(self, steps: int) -> str:
        # Move pages back from forwardHistoryStack to curStack
        while steps > 0 and self.forwardHistoryStack:
            # Pop from 'forward' and push back into 'current' history
            next_page = self.forwardHistoryStack.pop()
            self.curStack.append(next_page)
            steps -= 1
            
        return self.curStack[-1]
