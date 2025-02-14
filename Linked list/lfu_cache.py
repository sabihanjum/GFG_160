"""Design and implement an LFU (Least Frequently Used) cache. Here cap denotes the capacity of the cache and Q denotes the number of queries. Query can be of two types GET(x) and PUT(x, y). 

The LRU cache should support the following operations:

LFUCache(cap): initializes the cache with a given capacity.
get(key): returns the value associated with the key if it exists; otherwise, returns -1.
put(key, value): inserts or updates the key with value. If the cache has reached its capacity, the least frequently used (LFU) key should be removed. If there is a tie between keys with the same frequency, the least recently used (LRU) key among them should be removed."""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val

        # Initial frequency is 1
        self.cnt = 1
        self.next = None
        self.prev = None

class LFUCache:
    
    # Constructor to initialize the LFU cache
    def __init__(self, capacity):

        # Maps key to Node
        self.cacheMap = {}  
        
        # Maps frequency to doubly linked list
        # (head, tail) of Nodes
        self.freqMap = {}   
        
        # Tracks the minimum frequency
        self.minFreq = 0    
        
        # Capacity of the LFU cache
        self.capacity = capacity  

    # Function to get the value for a given key
    def get(self, key):

        # Return -1 if key is not found in the cache
        if key not in self.cacheMap:
            return -1

        # Retrieve the Node and update its frequency
        node = self.cacheMap[key]
        res = node.value
        self.updateFreq(node)
        return res

    # Function to put a key-value pair into the cache
    def put(self, key, value):

        # Do nothing if the cache has zero capacity
        if self.capacity == 0:
            return

        # Update value if key already exists in the cache
        if key in self.cacheMap:
            node = self.cacheMap[key]
            node.value = value
            self.updateFreq(node)

        # Add a new key-value pair to the cache
        else:

            # Remove the least frequently used node if cache is full
            if len(self.cacheMap) == self.capacity:
                node = self.freqMap[self.minFreq][1].prev
                del self.cacheMap[node.key]
                self.remove(node)

                # Remove the frequency list if it's empty
                if self.freqMap[self.minFreq][0].next == self.freqMap[self.minFreq][1]:
                    del self.freqMap[self.minFreq]

            # Create a new node for the key-value pair
            node = Node(key, value)
            self.cacheMap[key] = node

            # Reset minimum frequency to 1
            self.minFreq = 1
            self.add(node, 1)

    # Add a node right after the head
    def add(self, node, freq):

        # Initialize the frequency list if it doesn't exist
        if freq not in self.freqMap:

            # Dummy head node
            head = Node(-1, -1)

            # Dummy tail node
            tail = Node(-1, -1)
            head.next = tail
            tail.prev = head
            self.freqMap[freq] = (head, tail)

        # Insert the node right after the head
        head = self.freqMap[freq][0]
        temp = head.next
        node.next = temp
        node.prev = head
        head.next = node
        temp.prev = node

    # Remove a node from the list
    def remove(self, node):

        # Update pointers to exclude the node
        delprev = node.prev
        delnext = node.next
        delprev.next = delnext
        delnext.prev = delprev

    # Update the frequency of a node
    def updateFreq(self, node):

        # Get the current frequency
        oldFreq = node.cnt

        # Increment the frequency
        node.cnt += 1

        # Remove the node from the current frequency list
        self.remove(node)
        if self.freqMap[oldFreq][0].next == self.freqMap[oldFreq][1]:
            del self.freqMap[oldFreq]

            # Update minimum frequency if needed
            if self.minFreq == oldFreq:
                self.minFreq += 1

        # Add the node to the updated frequency list
        self.add(node, node.cnt)