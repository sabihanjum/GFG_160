"""Given a root of a binary tree with n nodes, the task is to find its level order traversal. Level order traversal of a tree is breadth-first traversal for the tree."""

class Solution:
    def levelOrder(self, root):
        # Your code here
        if root is None:
            return []
            
        res = []
        q = deque()
        currLevel = 0
        
        q.append(root)
        
        while q:
            len_q = len(q)
            res.append([])
            for i in range(len(q)):
                node = q.popleft()
                res[currLevel].append(node.data)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            currLevel += 1
        return res