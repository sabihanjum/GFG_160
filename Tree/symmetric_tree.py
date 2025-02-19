"""Given a root of a Binary Tree. Your task is to check whether it is Symmetric or not, i.e. whether the binary tree is a Mirror image of itself."""

class Solution:
    def isSymmetric(root):
        if root is None:
            return True

        # Two stacks to store nodes for comparison
        s1 = []
        s2 = []

        # Initialize the stacks with the 
        # left and right subtrees
        s1.append(root.left)
        s2.append(root.right)

        while s1 and s2:
            # Get the current pair of nodes
            node1 = s1.pop()
            node2 = s2.pop()

            # If both nodes are null, continue to the next pair
            if node1 is None and node2 is None:
                continue

            # If one node is null and the other is not, 
            # or the nodes' data do not match
            # then the tree is not symmetric
            if node1 is None or node2 is None or node1.data != node2.data:
                return False

            # Push children of node1 and node2 in opposite order
            # Push left child of node1 and right child of node2
            s1.append(node1.left)
            s2.append(node2.right)

            # Push right child of node1 and left child of node2
            s1.append(node1.right)
            s2.append(node2.left)

        # If both stacks are empty, the tree is symmetric
        return len(s1) == 0 and len(s2) == 0