"""Given a data stream arr[] where integers are read sequentially, the task is to determine the median of the elements encountered so far after each new integer is read.

There are two cases for median on the basis of data set size.

1. If the data set has an odd number then the middle one will be consider as median.
2. If the data set has an even number then there is no distinct middle value and the median will be the arithmetic mean of the two middle values."""
import heapq
class Solution:

    # Function to find the median of a stream of data
    def getMedian(arr):
    
        # Max heap to store the smaller half of numbers
        leftMaxHeap = []
    
        # Min heap to store the greater half of numbers
        rightMinHeap = []
    
        res = []
        for num in arr:
            # Insert new element into max heap (negating for max behavior)
            heapq.heappush(leftMaxHeap, -num)
        
            # Move the top of max heap to min heap to maintain order
            temp = -heapq.heappop(leftMaxHeap)
            heapq.heappush(rightMinHeap, temp)
            # Balance heaps if min heap has more elements
            if len(rightMinHeap) > len(leftMaxHeap):
                temp = heapq.heappop(rightMinHeap)
                heapq.heappush(leftMaxHeap, -temp)
        
            # Compute median based on heap sizes
            if len(leftMaxHeap) != len(rightMinHeap):
                median = -leftMaxHeap[0]
            else:
                median = (-leftMaxHeap[0] + rightMinHeap[0]) / 2.0
        
            res.append(median)
    
        return res