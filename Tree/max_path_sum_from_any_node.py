"""Given a binary tree, the task is to find the maximum path sum. The path may start and end at any node in the tree."""
class Node:
    def __init__(self, val):
        self.left = (None)
        self.right = None
        self.data = val
class Slution:
    def maxPathSumUtil(self, root, res):
        # Base case: return 0 for a null node
        if root is None:
            return 0

        # Calculate maximum path sums for left and right subtrees
        l = max(0, self.maxPathSumUtil(root.left, res))
        r = max(0, self.maxPathSumUtil(root.right, res))

        # Update 'res' with the maximum path sum passing through the current node
        res[0] = max(res[0], l + r + root.data)

        # Return the maximum path sum rooted at this node
        return root.data + max(l, r)

    # Returns maximum path sum in tree with given root
    def maxPathSum(self, root):
        res = [root.data]

        # Compute maximum path sum and store it in 'res'
        self.maxPathSumUtil(root, res)

        return res[0]