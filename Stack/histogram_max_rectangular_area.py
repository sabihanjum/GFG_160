"""You are given a histogram represented by an array arr, where each element of the array denotes the height of the bars in the histogram. All bars have the same width of 1 unit.

Your task is to find the largest rectangular area possible in the given histogram, where the rectangle can be formed using a number of contiguous bars."""

class Solution:
    def nextSmaller(self, arr):
        n = len(arr)
        nextS = [n] * n
        st = []
        for i in range(n):
            while st and arr[i] < arr[st[-1]]:
                nextS[st.pop()] = i
            st.append(i)
        return nextS
    def prevSmaller(self, arr):
        n = len(arr)
        prevS = [-1] * n
        st = []
        for i in range(n):
            while st and arr[i] < arr[st[-1]]:
                st.pop()
            if st:
                prevS[i] = st[-1]
            st.append(i)
        return prevS
    def getMaxArea(self, arr):
        prevS = self.prevSmaller(arr)
        nextS = self.nextSmaller(arr)
        maxArea = 0
        for i in range(len(arr)):
            width = nextS[i] - prevS[i] - 1
            area = arr[i] * width
            maxArea = max(maxArea, area)
        return maxArea