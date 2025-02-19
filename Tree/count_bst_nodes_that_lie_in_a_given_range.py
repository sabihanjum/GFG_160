"""Given a Binary Search Tree (BST) and a range l-h (inclusive), your task is to return the number of nodes in the BST whose value lie in the given range."""

class Solution:
    def getCount(self, root, l, h):
        # Your code here
        if root is None:
            return 0
            
        if root.data >= l and root.data <= h:
            return 1+self.getCount(root.left, l, h) + self.getCount(root.right, l, h)
        elif root.data<l:
            return self.getCount(root.right, l, h)
        else:
            return self.getCount(root.left, l, h)