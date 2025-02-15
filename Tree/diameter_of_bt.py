"""Given a binary tree, the diameter (also known as the width) is defined as the number of edges on the longest path between two leaf nodes in the tree. This path may or may not pass through the root. Your task is to find the diameter of the tree."""

class Solution:
    def diameterRecur(self, root, res):

        # Base case: tree is empty
        if root is None:
            return 0

        # find the height of left and right subtree
        # (it will also find of diameter for left 
        # and right subtree).
        lHeight = self.diameterRecur(root.left, res)
        rHeight = self.diameterRecur(root.right, res)

        # Check if diameter of root is greater
        # than res.
        res[0] = max(res[0], lHeight + rHeight+1)

        # return the height of current subtree.
        return 1 + max(lHeight, rHeight)

    # Function to get diameter of a binary tree
    def diameter(self, root):
        res = [0]
        self.diameterRecur(root, res)
        return res[0] - 1