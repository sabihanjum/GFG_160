"""Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

Left Boundary: This includes all the nodes on the path from the root to the leftmost leaf node. You must prefer the left child over the right child when traversing. Do not include leaf nodes in this section.

Leaf Nodes: All leaf nodes, in left-to-right order, that are not part of the left or right boundary.

Reverse Right Boundary: This includes all the nodes on the path from the rightmost leaf node to the root, traversed in reverse order. You must prefer the right child over the left child when traversing. Do not include the root in this section if it was already included in the left boundary.

Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. """

class Solution:
    def isLeaf(self, node):
        return node.left is None and node.right is None


    # Function to collect the left boundary nodes
    def collectBoundaryLeft(self, root, res):
        if root is None:
            return

        curr = root
        while not self.isLeaf(curr):
            res.append(curr.data)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    # Function to collect the leaf nodes using Morris Traversal
    def collectLeaves(self, root, res):
        current = root

        while current:
            if current.left is None:
                # To include Rightmost leaf node
                if current.right is None:
                    res.append(current.data)
            
                current = current.right
            
            else:
                # Find the inorder predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                    if predecessor.right is None:
                
                        predecessor.right = current
                        current = current.left
                    else:
                        # If it's predecessor is a leaf node
                        if (predecessor.left is None) :
                            res.append(predecessor.data)
                            predecessor.right = None
                            current = current.right
                
    # Function to collect the right boundary nodes
    def collectBoundaryRight(self, root, res):
        if root is None:
            return

        curr = root
        temp = []
        while not self.isLeaf(curr):
            temp.append(curr.data)

            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        res.extend(reversed(temp))

    # Function to perform boundary traversal
    def boundaryTraversal(self, root):
        res = []

        if not root:
            return res

        # Add root data if it's not a leaf
        if not self.isLeaf(root):
            res.append(root.data)

        # Collect left boundary
        self.collectBoundaryLeft(root.left, res)

        # Collect leaf nodes
        self.collectLeaves(root, res)

        # Collect right boundary
        self.collectBoundaryRight(root.right, res)

        return res