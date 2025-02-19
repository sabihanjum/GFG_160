"""Given a root of a Binary Search Tree, modify and return the given BST such that it is balanced and has minimum possible height. If there is more than one answer, return any of them.

Note: The height of balanced BST returned by you will be compared with the expected height of the balanced tree."""

class Solution:
    def constructBalancedBST(self, nodes, l, h):
        if l>h:
            return
        m = (l+h)//2
        root = Node(nodes[m])
        
        root.left = self.constructBalancedBST(nodes, l, m-1)
        root.right = self.constructBalancedBST(nodes, m+1, h)
        
        return root
    def inorder(self, root, nodes):
        if root is None:
            return
        self.inorder(root.left, nodes)
        nodes.append(root.data)
        self.inorder(root.right, nodes)
    def balanceBST(self,root):
        #code here
        nodes = []
        self.inorder(root, nodes)
        
        return self.constructBalancedBST(nodes, 0, len(nodes)-1)

