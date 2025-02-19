"""You are given a binary tree with n nodes, where each node contains a certain number of candies, and the total number of candies across all nodes is n. In one move, we can select two adjacent nodes and transfer one candy from one node to the other. The transfer can occur between a parent and child in either direction.

The task is to determine the minimum number of moves required to ensure that every node in the tree has exactly one candy.

Note: The testcases are framed such that it is always possible to achieve a configuration in which every node has exactly one candy, after some moves."""

class Solution:
    def distribute_candy_util(self, root, ans):
    
        # Base Case
        if root is None:
            return 0

        
        # Traverse left subtree
        l = self.distribute_candy_util(root.left, ans)

        # Traverse right subtree
        r = self.distribute_candy_util(root.right, ans)

        # Update number of moves
        ans[0] += abs(l) + abs(r)

        # Return number of moves to balance
        # current node
        return root.data + l + r - 1

    # Function to find the number of moves to
    # distribute all of the candies
    def distribute_candy(self, root):
        ans = [0]
    
        self.distribute_candy_util(root, ans)
    
        return ans[0]