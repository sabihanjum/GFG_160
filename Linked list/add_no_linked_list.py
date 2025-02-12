"""Given the head of two singly linked lists num1 and num2 representing two non-negative integers. The task is to return the head of the linked list representing the sum of these two numbers.

For example, num1 represented by the linked list : 1 -> 9 -> 0, similarly num2 represented by the linked list: 2 -> 5. Sum of these two numbers is represented by 2 -> 1 -> 5.

Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list."""


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
#Driver Code Ends }

class Solution:
# function to reverse the linked list
    def reverse(self, head):
        prev = None
        curr = head

        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

    # function to trim leading zeros in linked list
    def trimLeadingZeros(self, head):
        while head and head.data == 0:
            head = head.next
        return head
    # Function to find the length of linked list
    def countNodes(self, head):
        length = 0
        curr = head

        while curr is not None:
            length += 1
            curr = curr.next

        return length

    # Function to add two numbers represented by linked list
    def addTwoLists(self, num1, num2):
        num1 = self.trimLeadingZeros(num1)
        num2 = self.trimLeadingZeros(num2)
    
        # Find the length of both the linked lists
        len1 = self.countNodes(num1)
        len2 = self.countNodes(num2)
    
        # If num1 is smaller, swap the two linked lists by 
        # calling the function with reversed parameters
        if len1 < len2:
            return self.addTwoLists(num2, num1)

        carry = 0
        num1 = self.reverse(num1)
        num2 = self.reverse(num2)

        res = num1

        # Iterate till either num2 is not empty or carry is greater than 0
        while num2 is not None or carry != 0:
            # Add carry to num1
            num1.data += carry

            # If num2 linked list is not empty, add it to num1
            if num2 is not None:
                num1.data += num2.data
                num2 = num2.next

            # Store the carry for the next nodes
            carry = num1.data // 10

            # Store the remainder in num1
            num1.data = num1.data % 10

            # If we are at the last node of num1 but carry is
            # still left, then append a new node to num1
            if num1.next is None and carry != 0:
                num1.next = Node(0)

            num1 = num1.next

        # Reverse the resultant linked list to get 
        # the required linked list
        return self.reverse(res)


    #Driver Code Starts{
    def printList(head):
        curr = head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()