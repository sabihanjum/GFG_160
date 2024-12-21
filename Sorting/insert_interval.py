"""Geek has an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith event and intervals is sorted in ascending order by starti. He wants to add a new interval newInterval= [newStart, newEnd] where newStart and newEnd represent the start and end of this interval.

Help Geek to insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary)."""

class Solution:
    def insertInterval(self, intervals, newInterval):
        res = []
        i = 0
        n = len(intervals)
        
        #Add all intervals that come before the new interval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        #merge all overlapping intervals with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        
        #add all the remianing intervals
        while i < n:
            res.append(intervals[i])
            i += 1
        return res