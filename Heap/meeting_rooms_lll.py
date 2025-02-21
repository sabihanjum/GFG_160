"""You are given an integer n representing the number of rooms numbered from 0 to n - 1. Additionally, you are given a 2D integer array meetings[][] where meetings[i] = [starti, endi] indicates that a meeting is scheduled during the half-closed time interval [starti, endi). All starti values are unique.

Meeting Allocation Rules:

When a meeting starts, assign it to the available room with the smallest number.
If no rooms are free, delay the meeting until the earliest room becomes available. The delayed meeting retains its original duration.
When a room becomes free, assign it to the delayed meeting with the earliest original start time.
Determine the room number that hosts the most meetings. If multiple rooms have the same highest number of meetings, return the smallest room number among them."""

import heapq
class Solution:

    # Function to calculate the room that hosts the maximum meetings.
    def mostBooked(n, meetings):
        # Count of meetings per room
        cnt = [0] * n 
    
        # Min-heap for occupied rooms: (end time, room number)
        occ = []

        # Min-heap for available rooms: room numbers
        avail = list(range(n))

        # Sort meetings by start time
        meetings.sort()

        for s, e in meetings:
            # Release rooms that have become available by time s
            while occ and occ[0][0] <= s:
                _, r = heapq.heappop(occ)
                heapq.heappush(avail, r)

            if avail:
                # Assign to the smallest available room
                r = heapq.heappop(avail)
                heapq.heappush(occ, (e, r))
                cnt[r] += 1
            else:
                # All rooms are occupied; assign to the room that becomes free earliest
                t, r = heapq.heappop(occ)
                heapq.heappush(occ, (t + (e - s), r))
                cnt[r] += 1

        # Find the room with the maximum number of meetings
        res = max(range(n), key=lambda i: cnt[i])
        return res