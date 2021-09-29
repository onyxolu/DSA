# import heapq

# def minMeetingRooms(intervals):
#     if not intervals:
#         return 0
#     intervals.sort(key=lambda interval: interval.start)
#     min_heap = [intervals[0].end] # stores only end_time
    
#     for i in range(1, len(intervals)):
#         interval = intervals[i]
#         if interval.start < min_heap[0]:
#             heapq.heappush(min_heap, interval.end)
#         else:
#             heapq.heappushpop(min_heap, interval.end)
#     return len(min_heap)


# print(minMeetingRooms([(0,30),(5,10),(15,20)]))


def meetingRooms(intervals):
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    res, count = 0,0
    s, e = 0,0

    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else: 
            e += 1
            count -= 1
        res = max(res,count)
    return res

print(meetingRooms([(0,30),(5,10),(15,20)]))
