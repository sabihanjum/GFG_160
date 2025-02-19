"""Given a root of a Binary Tree, find the vertical traversal of it starting from the leftmost level to the rightmost level.
If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree."""

class Solution:
    def DFS(self, root, mp, mn, hd):
        if root is None:
            return 
        if hd not in mp:
            mp[hd] = []
            
        mp[hd].append(root.data)
        mn[0] = min(mn[0], hd)
        
        self.DFS(root.left, mp, mn, hd-1)
        self.DFS(root.right, mp, mn, hd+1)
    def verticalOrder(self, root): 
        #Your code here
        mp = {}
        mn = [0]
        
        self.DFS(root, mp, mn, 0)
        
        res = []
        hd = mn[0]
        while hd in mp:
            res.append(mp[hd])
            hd += 1
        return res