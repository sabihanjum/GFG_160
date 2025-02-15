"""Given a binary tree, convert the binary tree to its Mirror tree.

Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged. """

from collections import deque

class Solution:
    def mirror(root):
        if root is None:
            return

        queue = deque([root])

        # Traverse the tree, level by level
        while queue:
            curr = queue.popleft()

            # Swap the left and right subtree
            curr.left, curr.right = curr.right, curr.left

            # Push the left and right node to the queue
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    # Print tree as level order
    def levelOrder(root):
        if root is None:
            print("N ", end="")
            return

        queue = deque([root])

        while queue:
            curr = queue.popleft()

            if curr is None:
                print("N ", end="")
                continue

            print(curr.data, end=" ")
            queue.append(curr.left)
            queue.append(curr.right)