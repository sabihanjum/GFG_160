"""Given an array arr[] of n sorted linked lists of different sizes. The task is to merge them in such a way that after merging they will be a single sorted linked list, then return the head of the merged linked list."""

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
class Solution:
    # Function to merge two sorted lists.
    def mergeTwo(head1, head2):
    
        # Create a dummy node to simplify 
        # the merging process
        dummy = Node(-1)
        curr = dummy

        # Iterate through both linked lists
        while head1 is not None and head2 is not None:
            # Add the smaller node to the merged list
            if head1.data <= head2.data:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next

        # If any list is left, append it to
        # the merged list
        if head1 is not None:
            curr.next = head1
        else:
            curr.next = head2

        # Return the merged list starting
        # from the next of dummy node
        return dummy.next

    def mergeListsRecur(i, j, arr):
    
        # If single list is left
        if i == j:
            return arr[i]

        # Find the middle of lists
        mid = i + (j - i) // 2

        # Merge lists from i to mid 
        head1 = mergeListsRecur(i, mid, arr)

        # Merge lists from mid+1 to j 
        head2 = mergeListsRecur(mid + 1, j, arr)

        # Merge the above 2 lists 
        head = mergeTwo(head1, head2)

        return head

    # Function to merge K sorted linked lists
    def mergeKLists(arr):
    
        # Base case for 0 lists 
        if len(arr) == 0:
            return None

        return mergeListsRecur(0, len(arr) - 1, arr)

    def printList(node):
        while node is not None:
            print(node.data, end=" ")
            node = node.next