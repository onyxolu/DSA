from typing import Optional

# Clarify: return new list or modify in place? both empty? one empty?
# Both lists sorted → two pointer single pass → O(n+m) time
#
# Volunteer before being asked:
#   - Dummy node → clean head reference, no null edge cases
#   - node.next = list1 or list2 → handles remaining tail in O(1)
#   - One list empty → returns the other immediately
#   - Large input on disk → stream both sorted lists, same two pointer logic
#   - Real world: merge phase of merge sort, merging DB index pages

# ─── Approach 1: New Nodes — O(n+m) time | O(n+m) space ─────────────
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()                  # dummy head for clean reference

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:                                  # equal or greater → take list2
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2                 # append remaining tail
        return dummy.next


# ─── Approach 2: In-Place (reuse existing nodes) — O(n+m) time | O(1) space ──
# Same logic, but we reuse existing nodes instead of creating new ones
# Volunteer: use this when memory is constrained
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        if not list1: return list2
        if not list2: return list1

        # ensure list1 starts with smaller value
        if list1.val > list2.val:
            list1, list2 = list2, list1

        head = list1                               # head is always list1 now

        while list1.next and list2:
            if list1.next.val <= list2.val:
                list1 = list1.next                 # advance list1
            else:
                next = list1.next                  # save list1.next
                list1.next = list2                 # insert list2 node
                list2 = list2.next                 # advance list2
                list1.next.next = next             # reconnect saved next
                list1 = list1.next                 # advance list1

        if not list1.next:
            list1.next = list2                     # append remaining list2

        return head

# ─── Decision guide ──────────────────────────────────────────────────
# Memory fine       → Approach 1 (simpler, less error prone)
# Memory constrained → Approach 2 (in-place, O(1) space)
# Large on disk     → stream both sorted, Approach 1 logic

# Edge cases (both approaches):
#   both empty → return None
#   one empty → return the other
#   all equal → stable, list2 values appended after list1 values

# Follow-ups:
#   Merge k sorted lists → min heap → O(n log k) — on your tagged list!
#   In-place merge → Approach 2 above
#   Large lists on disk → stream both, same two pointer logic