# best method: in only one swap(submitted on geeksforgeeks)
# traverse the whole linklist till end and keep on incr first
# and when count become>= n then after that start incr 'second' aslo
# this will ensure first-second= n-1 and thus 'second' will point to the
# nth node from the last
def getNthFromLast(head,n):
    first, second= head,head
    count= 0
    while first.next:
        first= first.next
        count+= 1
        if count>=n:   # after count becomes equal to n
            second= second.next
    if count+1<n: # means n> no of elements in the link list
        return -1
    else:
        return second.data

# 2nd method: Brute force method
# this will take two traversal
# 1st to count no of elements and 2nd to get the nth element from the last

