"""Given a matrix mat[][]. Find the size of the largest sub-matrix whose sum is equal to zero. The size of a matrix is the product of rows and columns. A sub-matrix is a matrix obtained from the given matrix by deletion of several (possibly, zero or all) rows/columns from the beginning and several (possibly, zero or all) rows/columns from the end."""

class Solution:
    def maxZeroSumSubarray(self, arr):
        prefSum = 0
        maxLength = 0

        # Hash map to store the first index of each prefix sum
        mp = {}

        # Iterate through the array to find subarrays with zero sum
        for i in range(len(arr)):
            prefSum += arr[i]

            if prefSum == 0:
                maxLength = i + 1

            if prefSum in mp:
                # If this prefSum repeats, find subarray length.
                maxLength = max(maxLength, i - mp[prefSum])
            else:
                # Only store the index of the first occurrence of prefSum
                mp[prefSum] = i

        return maxLength

    def zeroSumSubmat(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        maxArea = 0

        for i in range(rows):

            # Temporary array to store the column-wise cumulative sum
            temp = [0] * cols

            # Iterate over each row from i to j
            for j in range(i, rows):

                # Accumulate the column-wise sum for rows between i and j
                for k in range(cols):
                    temp[k] += mat[j][k]

                # Find the longest zero-sum subarray in column sums
                lenSubarray = maxZeroSumSubarray(temp)

                # Update the maximum area 
                maxArea = max(maxArea, (j - i + 1) * lenSubarray)

        return maxArea