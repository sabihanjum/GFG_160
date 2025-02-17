"""Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree back from the array. Complete the functions

serialize() : stores the tree into an array a and returns the array.
deSerialize() : deserializes the array to the tree and returns the root of the tree.
Note: Multiple nodes can have the same data and the node values are always positive integers. Your code will be correct if the tree returned by deSerialize(serialize(input_tree)) is same as the input tree. Driver code will print the in-order traversal of the tree returned by deSerialize(serialize(input_tree))."""

from collections import deque
class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        #code here
        arr = []
        q = deque([root])
        
        while q:
            curr = q.popleft()
            if not curr:
                arr.append(-1)
                continue
            arr.append(curr.data)
            q.append(curr.left)
            q.append(curr.right)
        return arr
    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, arr):
        #code here
        if arr[0] == -1:
            return None9left
        root = Node(arr[0])
        q = deque([root])
        
        i = 1
        while q:
            curr = q.popleft()
            if arr[i] != -1:
                left = Node(arr[i])
                curr.left = left
                q.append(left)
            i += 1
            
            if arr[i] != -1:
                right = Node(arr[i])
                curr.right = right
                q.append(right)
            i += 1
        return root
        
    def printLevelOrder(root):
        if root is None:
            print("N ", end = "")
            return
        queue = dequeue([root])
        non_null = 1
        while queue and non_null > 0:
            curr = queue.popleft()
            
            if curr is None:
                print("N ", end="")
                continue
            non_null -= 1
            
            print(curr.data, end = " ")
            queue.append(curr.left)
            queue.append(curr.right)
            if curr.left:
                non_null += 1
            if curr.right:
                non_null += 1