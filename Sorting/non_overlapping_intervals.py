"""Given a 2D array intervals[][] of representing intervals where intervals [i] = [starti, endi ]. Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping."""

class Solution:
    def minRemoval(self, intervals):
        """
        Find the minimum number of intervals to remove to make the rest non-overlapping.
        
        :param intervals: List[List[int]] - list of intervals
        :return: int - minimum number of intervals to remove
        """
        cnt = 0

        # Sort intervals by their ending point
        intervals.sort(key=lambda x: x[1])
        
        # Initialize the end of the first interval
        end = float('-inf')  # Start with a very small value to handle edge cases
        
        for interval in intervals:
            # If there is an overlap, increment the removal count
            if interval[0] < end:
                cnt += 1
            else:
                # Update the end point to the current interval's end
                end = interval[1]
                
        return cnt
