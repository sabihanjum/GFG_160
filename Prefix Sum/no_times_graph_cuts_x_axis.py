"""Given an integer array arr[], where each arr[i] denotes the trajectory of the graph over the plane; i.e. arr[i]>0 means graph going above its current position by arr[i] value and arr[i]<0 means graph going down by arr[i] value. If initial position of the graph is at origin, determines the number of times graph crosses or touches the X-axis."""

class Solution:
    def touchedXaxis(self, arr):
        # code here
        curPos = 0
        times = 0
        for i in range(len(arr)):
            if curPos < 0 and curPos + arr[i] >= 0:
                times += 1
            elif curPos > 0 and curPos + arr[i] <= 0:
                times += 1
            curPos += arr[i]
        return times