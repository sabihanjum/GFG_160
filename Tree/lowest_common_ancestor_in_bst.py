"""Given a Binary Search Tree (with all values unique) and two nodes n1 and n2 (n1 != n2). You may assume that both nodes exist in the tree. Find the Lowest Common Ancestor (LCA) of the given two nodes in the BST.

LCA between two nodes n1 and n2 is defined as the lowest node that has both n1 and n2 as descendants (where we allow a node to be a descendant of itself)."""

class Solution:
    def LCA(root, n1, n2):
        while root:
            # If both n1 and n2 are smaller than root,
            # then LCA lies in left
            if root.data > n1.data and root.data > n2.data:
                root = root.left
            
            # If both n1 and n2 are greater than root,
            # then LCA lies in right
            elif root.data < n1.data and root.data < n2.data:
                root = root.right
            
            # Else Ancestor is found
            else:
                break
            
        return root