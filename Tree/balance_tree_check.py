"""Given a binary tree, determine if it is height-balanced. A binary tree is considered height-balanced if the absolute difference in heights of the left and right subtrees is at most 1 for every node in the tree."""

class Solution:
    def isBalancedRec(self, root):
        # code here
        if root is None:
            return 0
            
        lHeight = self.isBalancedRec(root.left)
        rHeight = self.isBalancedRec(root.right)
        
        if lHeight == -1 or rHeight == -1 or abs(lHeight - rHeight) > 1:
            return -1
        return max(lHeight, rHeight) + 1
    def isBalanced(self, root):
        return self.isBalancedRec(root) > 0