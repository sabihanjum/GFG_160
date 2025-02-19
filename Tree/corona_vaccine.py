"""Geek has successfully developed an effective vaccine for the Coronavirus and aims to ensure that every house in Geek Land has access to it. The houses in Geek Land are structured as a binary tree, where each node represents a house, and the edges denote direct connections between houses.

Each house that receives a vaccine kit can provide coverage to:

Itself
Its direct parent house (if it exists)
Its immediate child houses (if any exist)
Your task is to determine the minimum number of houses that must be supplied with a vaccine kit to ensure that every house is covered."""

class Solution:
    def minVaccine(self, root, res):
        if not root:
            return 1

        left = self.minVaccine(root.left, res)
        right = self.minVaccine(root.right, res)

        # If any child is not covered, place a 
        # vaccine at this node
        if left == 0 or right == 0:
            res[0] += 1
            return 2

        # If any child has a vaccine, this node is covered
        if left == 2 or right == 2:
            return 1

        # Otherwise, this node is not covered
        return 0

    def supplyVaccine(self, root):
        res = [0]

        # If the root itself is not covered, 
        # place a vaccine at root
        if self.minVaccine(root, res) == 0:
            res[0] += 1

        return res[0]