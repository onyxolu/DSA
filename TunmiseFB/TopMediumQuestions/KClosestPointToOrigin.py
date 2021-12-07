'''
Finding the k closest points to the origin will require us to first be able to calculate the distance of a given point to the origin before we can start to evaluate the relative closeness of any two points.

In this problem, with one of the two Euclidean coordinates being the origin 
this simplifies the Euclidean distance equation back to dist = x^2 + y^2
'''

'''
APPROACH 1 - USING HEAP DATA STRUCTURE

While we must iterate over all elements in the points array, we only need to keep track of the k closest points encountered so far. We could therefore choose to store them in a separate data structure. In order to keep this data structure capped at k elements, we will need to keep track of the point that is farthest away from the origin and thus the next point to be removed when a closer point is found.

The ideal data structure for this purpose is a max heap or max priority queue. These data structures allow access to the max value in constant time and perform replacements in logarithmic time.

At the start of our iteration through points, we will insert the first k elements into our heap. Once the heap is "full", we can then compare each new point to the farthest point stored in the heap. If the new point is closer, then we should remove the farthest point from the heap and insert the new point.

After the entire points array has been processed, we can create an array from the points stored in the heap and then return the answer.

Algorithm

1 - Use a max heap (or max priority queue) to store points by distance.
    Store the first k elements in the heap.
    Then only add new elements that are closer than the top point in the heap while removing the top point to keep the heap at k elements.
2 - Return an array of the k points stored in the heap.


Time complexity - O(N log k) - Adding to/removing from heap takes log k time, when the size is capped at k
Space complexity - O(k) - the heap will contain maximum of k elements
N - lenght of points array
'''
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Since heap is sorted in increasing order,
        # negate the distance to simulate max heap
        # and fill the heap with the first k elements of points
        heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            dist = -self.squared_distance(points[i])
            if dist > heap[0][0]:
                # If this point is closer than the kth farthest,
                # discard the farthest point and add this one
                heapq.heappushpop(heap, (dist, i))
        
        # Return all points stored in the max heap
        return [points[i] for (_, i) in heap]
    
    def squared_distance(self, point):
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2





'''

ALTERNATE APPROACH USING SORT


Time complexity: O(NlogN)
Sort the list according to the distance to origin. Apparently, we did more than the question asked. We sorted all the distance, the question only ask for top k. To improve time complexity, we need to think about how to get we ask without extra effort. This is where heap data structure comes in.

'''

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda P:P[0]**2+P[1]**2)
        return points[:K]