"""Given the root of a Binary search tree(BST), where exactly two nodes were swapped by mistake. Your task is to fix (or correct) the BST by swapping them back. Do not change the structure of the tree.
Note: It is guaranteed that the given input will form BST, except for 2 nodes that will be wrong. All changes must be reflected in the original Binary search tree(BST)."""

class Solution:
    def correctBSTUtil(self, root, first, middle, last, prev):
        if root is None:
            return

        # Recur for the left subtree
        self.correctBSTUtil(root.left, first, middle, last, prev)

        # If this node is smaller than the previous node, 
        # it's violating the BST rule.
        if prev[0] and root.data < prev[0].data:

            # If this is the first violation, mark these 
            # two nodes as 'first' and 'middle'
            if not first[0]:
                first[0] = prev[0]
                middle[0] = root

            # If this is the second violation, 
            # mark this node as last
            else:
                last[0] = root

        # Mark this node as previous
        prev[0] = root

        # Recur for the right subtree
        self.correctBSTUtil(root.right, first, middle, last, prev)

    # Function to fix the given BST, where two nodes are swapped.
    def correctBST(self, root):
        # Initialize pointers needed for correctBSTUtil()
        first, middle, last, prev = [None], [None], [None], [None]

        # Set the pointers to find out two nodes
        self.correctBSTUtil(root, first, middle, last, prev)

        # Fix (or correct) the tree
        if first[0] and last[0]:
            first[0].data, last[0].data = last[0].data, first[0].data
        elif first[0] and middle[0]:
            first[0].data, middle[0].data = middle[0].data, first[0].data


    #Driver Code Starts{
    # Print tree as level order
    def printLevelOrder(root):
        if not root:
            print("N", end=" ")
            return

        queue = [root]
        nonNull = 1

        while queue and nonNull > 0:
            curr = queue.pop(0)

            if curr is None:
                print("N", end=" ")
                continue
            nonNull -= 1

            print(curr.data, end=" ")
            queue.append(curr.left)
            queue.append(curr.right)
            if curr.left:
                nonNull += 1
            if curr.right:
                nonNull += 1