"""Given a BST and an integer k, the task is to find the kth smallest element in the BST. If there is no kth smallest element present then return -1."""
class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallestRecur(self, root,cnt, k): 
        #code here.
        if root is None:
            return -1
        left = self.kthSmallestRecur(root.left, cnt, k)
        if left != -1:
            return left
        cnt[0] += 1
        
        if cnt[0] == k:
            return root.data
        right = self.kthSmallestRecur(root.right, cnt, k)
        return right
    def kthSmallest(self, root, k):
        cnt = [0]
        return self.kthSmallestRecur(root, cnt, k)