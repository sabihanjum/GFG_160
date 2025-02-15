"""Given a binary tree and an integer k, determine the number of downward-only paths where the sum of the node values in the path equals k. A path can start and end at any node within the tree but must always move downward (from parent to child)."""

class Solution:
    # Function to find paths in the tree which have their sum equal to K
    def countPathsUtil(self, node, k, currSum, prefSums):
        if node is None:
            return 0

        pathCount = 0
        currSum += node.data

        # Pathsum from root to current node is equal to k
        if currSum == k:
            pathCount += 1

        # The count of curr_sum − k gives the number of paths 
        #with sum k up to the current node
        pathCount += prefSums.get(currSum - k, 0)

        # Add the current sum into the hashmap
        prefSums[currSum] = prefSums.get(currSum, 0) + 1

        pathCount += self.countPathsUtil(node.left, k, currSum, prefSums)
        pathCount += self.countPathsUtil(node.right, k, currSum, prefSums)

        # Remove the current sum from the hashmap
        prefSums[currSum] -= 1

        return pathCount

    # Function to find the paths in the tree which have their sum equal to K
    def countAllPaths(self, root, k):
        prefSums = {}
        return self.countPathsUtil(root, k, 0, prefSums)
