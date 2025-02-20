"""Given an array of points where each point is represented as points[i] = [xi, yi] on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance, defined as: 

sqrt( (x2 - x1)2 + (y2 - y1)2 )

Note: You can return the k closest points in any order, driver code will sort them before printing."""
import heapq
class Solution:
    # Function to calculate squared
    # distance from the origin
    def squaredDis(self, point):
        return point[0] * point[0] + point[1] * point[1]

    # Function to find k closest points to the origin
    def kClosest(self, points, k):
        # Max heap to store points with their 
        # squared distances
        maxHeap = []

        # Iterate through each point
        for point in points:
            dist = self.squaredDis(point)
        
            if len(maxHeap) < k:
                # If the heap size is less than k, 
                # insert the point
                heapq.heappush(maxHeap, (-dist, point))
            else:
                # If the heap size is k, compare with
                #the top element
                if -dist > maxHeap[0][0]:
                    # Replace the top element if the current
                    #point is closer
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-dist, point))

        # Take the k closest points from the heap
        return [pair[1] for pair in maxHeap]