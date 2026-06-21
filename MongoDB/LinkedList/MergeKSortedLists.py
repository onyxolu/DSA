import heapq
from typing import List, Optional

# Clarify: duplicates preserved? empty list valid? empty lists within list?
# k = number of lists, n = total nodes across all lists
#
# Approach: Min Heap — O(n log k) time | O(k) space
# Volunteer before being asked:
#   - NodeWrapper needed → Python heapq can't compare ListNode directly
#   - Only push head of each list initially → heap stays size k
#   - As each node is popped, push its next → always k elements in heap
#   - Divide and conquer alternative → O(n log k) time, O(log k) space (recursion stack)
#   - Real world: merge phase of external merge sort, merging DB index pages

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):                       # needed for heapq comparison
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        res = cur = ListNode(0)                    # dummy head
        minHeap = []

        for lst in lists:
            if lst:                                # skip empty lists
                heapq.heappush(minHeap, NodeWrapper(lst))

        while minHeap:
            wrapper = heapq.heappop(minHeap)       # pop smallest
            cur.next = wrapper.node
            cur = cur.next

            if wrapper.node.next:                  # push next node from same list
                heapq.heappush(minHeap, NodeWrapper(wrapper.node.next))

        return res.next

# Edge cases:
#   [] → None
#   [[]] → None
#   single list → returns it as is
#   all equal values → all preserved in order

# Complexity:
#   time → O(n log k) — n pops each costing O(log k)
#   space → O(k) — heap never exceeds k elements

# vs Divide and Conquer:
#   heap → O(k) space, simpler to implement
#   divide and conquer → O(log k) space, better for memory-constrained environments

# Connection:
#   merge two sorted lists → building block of this problem
#   this problem → building block of external merge sort


# ─── Approach 2: Divide and Conquer — O(n log k) time | O(log k) space
# Key insight: pair up lists and merge two at a time, halving the problem each round
# log k rounds × O(n) per round = O(n log k)
# Volunteer: better space than heap — O(log k) recursion stack vs O(k) heap
# Real world: same as merge sort — natural fit for distributed merging
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])       # recurse left half
        right = self.mergeKLists(lists[mid:])      # recurse right half
        return self.mergeTwoLists(left, right)     # merge the two halves

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next