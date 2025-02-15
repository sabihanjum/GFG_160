"""Given a Binary Search Tree(BST) and a target. Check whether there's a pair of Nodes in the BST with value summing up to the target. """

class Solution:
    def inorderTraversal(self, root, inorder):
        if root is None:
            return
        
        self.inorderTraversal(root.left, inorder)
        inorder.append(root.data)
        self.inorderTraversal(root.right, inorder)
    def findTarget(self, root, target): 
        # your code here.
        inorder = []
        self.inorderTraversal(root, inorder)
        n = len(inorder)
        l = 0
        r = n-1
        
        while l<r:
            if inorder[l] + inorder[r] > target:
                r -= 1
            elif inorder[l] + inorder[r] < target:
                l += 1
            else:
                return True
        return False