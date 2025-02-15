"""Given two arrays representing the inorder and preorder traversals of a binary tree, construct the tree and return the root node of the constructed tree.

Note: The output is written in postorder traversal."""

from collections import deque

class Solution:
    def printLevelOrder(self, root):
        if root is None:
            print("N ", end="")
            return

        qq = deque([root])
        nonNull = 1

        while qq and nonNull > 0:
            curr = qq.popleft()

            if curr is None:
                print("N ", end="")
                continue
            nonNull -= 1

            print(curr.data, end=" ")
            qq.append(curr.left)
            qq.append(curr.right)
            if curr.left:
                nonNull += 1
            if curr.right:
                nonNull += 1
        #Driver Code Ends }


    # Recursive function to build the binary tree.
    def buildTreeRecur(self, mp, preorder, preIndex, left, right):
        # For empty inorder array, return None
        if left > right:
            return None

        rootVal = preorder[preIndex[0]]
        preIndex[0] += 1

        # create the root Node
        root = Node(rootVal)

        # find the index of Root element in the in-order array.
        index = mp[rootVal]

        # Recursively create the left and right subtree.
        root.left = self.buildTreeRecur(mp, preorder, preIndex, left, index - 1)
        root.right = self.buildTreeRecur(mp, preorder, preIndex, index + 1, right)

        return root

    # Function to construct tree from its inorder and preorder traversals
    def buildTree(self, inorder, preorder):
        # Hash map that stores index of a root element in inorder array
        mp = {value: idx for idx, value in enumerate(inorder)}
        preIndex = [0]
    
        return self.buildTreeRecur(mp, preorder, preIndex, 0, len(inorder) - 1)