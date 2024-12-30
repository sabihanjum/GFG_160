"""You are given a 2D matrix mat[][] of size n×m. The task is to modify the matrix such that if mat[i][j] is 0, all the elements in the i-th row and j-th column are set to 0 and do it in constant space complexity."""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Result list to store the merged intervals
        res = []

        # Iterate through each interval in the given list
        for i in range(len(intervals)):
            # Case 1: The new interval is completely before the current interval
            if newInterval[1] < intervals[i][0]:
                # Add the new interval to the result and append the remaining intervals
                res.append(newInterval)
                return res + intervals[i:]

            # Case 2: The new interval is completely after the current interval
            elif newInterval[0] > intervals[i][1]:
                # Add the current interval to the result
                res.append(intervals[i])

            # Case 3: The new interval overlaps with the current interval
            else:
                # Merge the intervals by taking the minimum start and maximum end
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # Add the merged interval to the result after processing all intervals
        res.append(newInterval)
        return res
