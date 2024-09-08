# brute force , time: O(n* k) may go to O(n^2)
# logic: 1st take two linked list and merge them now take the list one by one and merge with ans of already merged list

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if len(lists)== 0 or len(lists)==1:
            # return lists   # here i was making mistake since we have to return as linked list but here it will return in form of array
        if lists== [[]] or lists== []:
            return None   
        if len(lists)==1:
            return lists[0]  # every 1D array is a linked list in itself so we can return this
        head1, head2= lists[0], lists[1]
        newHead= self.mergeTwoLists(head1,head2)
        for i in range(2,len(lists)):
            head1= newHead
            head2= lists[i]
            newHead= self.mergeTwoLists(head1,head2)
        return newHead
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val> list2.val:                       
                list1, list2= list2, list1                                                                                  
            list1.next= self.mergeTwoLists(list1.next,list2) 
        return list1 or list2


# method 2:
# time: O(n*logk), k= no of given lists and n is the no of nodes inside each list
# logic: it is just like given 'k'  elements and merge them into one.
# Take two list consecutively and merge them till  end
# after that you will left with k/2 lists , now repeat the same step just like we do for merge sort
# finally you will get the one sorted lists 

# in this case you will have to move logK level and each level workdone will be 0(n)
# so time complexity is O(n*logK), space: O(logk)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        while len(lists) > 1:
            MergedLists = []
            for i in range(0, len(lists),2):
                l1= lists[i]
                l2= lists[i+1] if (i+1) < len(lists) else None   # this can be None also for odd no of lists
                MergedLists.append(self.mergeTwoLists(l1,l2))
            lists= MergedLists.copy()
        return lists[0]  
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val> list2.val:                       
                list1, list2= list2, list1                                                                                  
            list1.next= self.mergeTwoLists(list1.next,list2) 
        return list1 or list2


# method 3: very simpler and cleaner
# time and space is just same as above
# logic: just use the concept of merge sort (divide and conquer technique)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists== [[]] or lists== []:
            return None
        if len(lists)==1:
            return lists[0]
        mid= len(lists)//2
        l,r= self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        # l,r= self.mergeKLists(lists[:mid+1]), self.mergeKLists(lists[mid+1:])   # this is giving error 'max recursion depth exceeded' don't getting why
        return self.merge(l,r)
    
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val> list2.val:                       
                list1, list2= list2, list1                                                                                  
            list1.next= self.merge(list1.next,list2) 
        return list1 or list2


# Java
"""
// method 1:
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }
        if (lists.length == 1) {
            return lists[0];
        }

        ListNode head1 = lists[0];
        ListNode head2 = lists[1];
        ListNode newHead = mergeTwoLists(head1, head2);

        for (int i = 2; i < lists.length; i++) {
            head1 = newHead;
            head2 = lists[i];
            newHead = mergeTwoLists(head1, head2);
        }

        return newHead;
    }

    private ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        if (list1.val > list2.val) {
            ListNode temp = list1;
            list1 = list2;
            list2 = temp;
        }
        list1.next = mergeTwoLists(list1.next, list2);
        return list1;
    }

    
// method 2:
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }
        if (lists.length == 1) {
            return lists[0];
        }
        while (lists.length > 1) {
            int newSize = (lists.length + 1) / 2; // Calculate new size for the next iteration
            ListNode[] mergedLists = new ListNode[newSize];
            for (int i = 0; i < lists.length; i += 2) {
                ListNode l1 = lists[i];
                ListNode l2 = (i + 1 < lists.length) ? lists[i + 1] : null;
                mergedLists[i / 2] = mergeTwoLists(l1, l2);
            }
            lists = mergedLists; // Update lists to be the merged lists for the next iteration
        }
        return lists[0];
    }

    private ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        if (list1.val > list2.val) {
            ListNode temp = list1;
            list1 = list2;
            list2 = temp;
        }
        list1.next = mergeTwoLists(list1.next, list2);
        return list1;
    }

    
// method 3:
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0 || (lists.length == 1 && lists[0] == null)) {
            return null;
        }
        if (lists.length == 1) {
            return lists[0];
        }
        return mergeKListsHelper(lists, 0, lists.length - 1);
    }

    private ListNode mergeKListsHelper(ListNode[] lists, int start, int end) {
        if (start == end) {
            return lists[start];
        }
        int mid = start + (end - start) / 2;
        ListNode left = mergeKListsHelper(lists, start, mid);
        ListNode right = mergeKListsHelper(lists, mid + 1, end);
        return merge(left, right);
    }

    private ListNode merge(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        if (list1.val > list2.val) {
            ListNode temp = list1;
            list1 = list2;
            list2 = temp;
        }
        list1.next = merge(list1.next, list2);
        return list1;
    }
}

"""