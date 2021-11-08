def meetingRoomii(meetings):
    startTimes = [i[0] for i in meetings]
    endTimes = [i[1] for i in meetings]
    startTimes.sort(reverse=True)
    endTimes.sort(reverse=True)

    rooms = 0
    while len(startTimes)>0:
        startTime = startTimes.pop()

        endTime = endTimes[-1]
        if endTime <= startTime:
            endTime.pop()
        else:
            rooms += 1
    return rooms

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        size = len(intervals)
        if size<=1: return size

        #sort by start times
        intervals.sort(key = lambda x: x[0])
        heap = [interval[0][1]]
        heapq.heapify(heap)

        #iterate through the intervals
        for interval in intervals[1:]:
            if heap and interval[0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,interval[1])

        return len(heap)

