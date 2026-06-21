from typing import List
import bisect

# Clarify: all values init to 0? snap_id starts at 0? get always called with valid snap_id?
# Key insight: store only changes per index, not full array per snap
# This is essentially MVCC — same pattern MongoDB uses internally for document versioning
#
# Volunteer before being asked:
#   - Naive: store full array per snap → O(n×v) space where v = number of snaps
#   - Optimal: store (snap_id, val) pairs per index → O(n + s) where s = total sets
#   - Binary search on get → find floor snap_id → O(log s)
#   - Real world: git commits, MongoDB oplog, database MVCC

class SnapshotArray:
    def __init__(self, length: int):
        # history[index] = [[snap_id, value], ...] — only stores changes
        self.history = [[[-1, 0]] for _ in range(length)]  # -1 ensures base value always found
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.history[index].append([self.snap_id, val])    # record change at current snap

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1                            # return before increment

    def get(self, index: int, snap_id: int) -> int:
        history = self.history[index]

        # binary search for largest snap_id <= requested snap_id
        l, r = 0, len(history) - 1
        pos = 0                                            # default to base value [-1, 0]

        while l <= r:
            mid = l + (r - l) // 2
            if history[mid][0] <= snap_id:
                pos = mid                                  # valid candidate, try newer
                l = mid + 1
            else:
                r = mid - 1

        return history[pos][1]

# Edge cases:
#   get before any set → returns 0 (base value from init)
#   get at exact snap_id → returns that value
#   get between snaps → returns most recent value before snap_id
#   multiple sets same index same snap → last set wins (latest in history)

# Complexity:
#   set → O(1) amortised
#   snap → O(1)
#   get → O(log s) where s = number of sets at that index
#   space → O(n + s) where n = length, s = total set calls

# Follow-ups:
#   Thread safe version → wrap set/snap/get with threading.Lock
#   Distributed → shard by index range, each shard keeps its own history
#   TTL snapshots → add expiry to snap, background thread to clean old versions
#   Real world: MongoDB change streams, git history, Postgres MVCC