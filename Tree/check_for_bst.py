"""Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.
A BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees."""

class Solution:
    def isBST(root):
        curr = root
        prevValue = float('-inf') 
        while curr:
            if curr.left is None:
                # Process curr node
                if curr.data <= prevValue:
                    # Not in ascending order
                    return False
                prevValue = curr.data
                curr = curr.right
            else:
                # Find the inorder predecessor of curr
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                if pre.right is None:
                    # Create a temporary thread to the curr node
                    pre.right = curr
                    curr = curr.left
                else:
                    # Remove the temporary thread
                    pre.right = None
                    # Process the curr node
                    if curr.data <= prevValue:
                        # Not in ascending order
                        return False
                    prevValue = curr.data
                    curr = curr.right

        return True