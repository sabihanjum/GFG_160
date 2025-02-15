"""Given a Binary Tree, your task is to return its In-Order Traversal.

An inorder traversal first visits the left child (including its entire subtree), then visits the node, and finally visits the right child (including its entire subtree).

Follow Up: Try solving this with O(1) auxiliary space."""

class Solution:
    # Morris Traversal
    def inOrder(root):
        res = []
        curr = root

        while curr is not None:
            if curr.left is None:

                # If no left child, visit this node and go right
                res.append(curr.data)
                curr = curr.right
            else:

                # Find the inorder predecessor of curr
                prev = curr.left
                while prev.right is not None \
                and prev.right != curr:
                    prev = prev.right

                # Make curr the right child of its inorder predecessor
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:

                    # Revert the changes made in the tree structure
                    prev.right = None
                    res.append(curr.data)
                    curr = curr.right

        return res