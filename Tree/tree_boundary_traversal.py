"""Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

Left Boundary: This includes all the nodes on the path from the root to the leftmost leaf node. You must prefer the left child over the right child when traversing. Do not include leaf nodes in this section.

Leaf Nodes: All leaf nodes, in left-to-right order, that are not part of the left or right boundary.

Reverse Right Boundary: This includes all the nodes on the path from the rightmost leaf node to the root, traversed in reverse order. You must prefer the right child over the left child when traversing. Do not include the root in this section if it was already included in the left boundary.

Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. """

class Solution:
    def collectBoundaryLeft(self, root, res):
        if root is None:
            return
        if self.isLeaf(root) is False:
            res.append(root.data)
        if root.left:
            self.collectBoundaryLeft(root.left, res)
        else:
            self.collectBoundaryLeft(root.right, res)
            
    def collectBoundaryRight(self, root, res):
        if root is None:
            return
        if root.right:
            self.collectBoundaryRight(root.right, res)
        else:
            self.collectBoundaryRight(root.left, res)
            
        if self.isLeaf(root) is False:
            res.append(root.data)
    def collectLeaves(self, root, res):
        if root is None:
            return
        
        if self.isLeaf(root):
            res.append(root.data)
        else:
            self.collectLeaves(root.left, res)
            self.collectLeaves(root.right, res)
    
    def isLeaf(self, root):
        if root.left is None and root.right is None:
            return True
        else:
            return False
    def boundaryTraversal(self, root):
        # Code here
        res = []
        if root is None:
            return res
        if self.isLeaf(root) is False:
            res.append(root.data)
            
        self.collectBoundaryLeft(root.left, res)
        self.collectLeaves(root, res)
        self.collectBoundaryRight(root.right, res)
        return res