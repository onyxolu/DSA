
# merging overlapping won't work
# We need to keep track of mutual exclusiveness
# we need to keep track of the ending time of all the meetings currently happening so that when we try to schedule a new meeting


import heapq

def minMeetingRooms( intervals):
    # if len(intervals) < 2:
    #     return 1
    intervals.sort(key=lambda x: x[0])
    minRooms = 0
    minHeap = []
    for interval in intervals:
        print(intervals,minHeap, minRooms)
        cur_start, cur_end = interval
        # remove all the meetings that have ended
        while len(minHeap) > 0 and cur_start >= minHeap[0][0]:
            heapq.heappop(minHeap)
        # add the current meeting into MinHeap (added end first so heap can sort by end time)
        heapq.heappush(minHeap, [cur_end, cur_start])
        # all active meetings are in the minHeap so we need room for all of them
        minRooms = max(minRooms, len(minHeap))
    return minRooms


print(minMeetingRooms([[0,30],[5,10],[15,20]]))