"""Given two arrays start[] and end[] such that start[i] is the starting time of ith meeting and end[i] is the ending time of ith meeting. Return the minimum number of rooms required to attend all meetings."""

class Solution:
    def minMeetingRooms(start, end):
        n = len(start)
    
        # no. of rooms at any point of time
        room = 0
        res = 0
    
        # sorting the start and end time of meetings
        start.sort()
        end.sort()
    
        # pointing to the current index of the start and end array
        i, j = 0, 0
    
        while i < len(start):
        
            # encountered start time of meeting
            if start[i] < end[j]:
                # increase no. of rooms
                room += 1
                i += 1
        
            # encountered end time of meeting
            else:
                # decrease no. of rooms
                room -= 1
                j += 1
        
            # updating final result
            res = max(res, room)
    
        return res