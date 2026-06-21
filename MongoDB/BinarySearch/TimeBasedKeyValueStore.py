# Clarify: timestamps always increasing? return "" if not found? same key multiple times?
# Key insight: timestamps increasing → list is already sorted → binary search for floor
#
# Connection to Snapshot Array:
#   Snapshot Array: history[index] = [[snap_id, value], ...]
#   Time Based KV:  store[key]     = [[timestamp, value], ...]
#   Same pattern — store changes, binary search for floor value
#
# Volunteer before being asked:
#   - set is O(1) — just append, already sorted by timestamp
#   - get is O(log n) — binary search for largest timestamp ≤ requested
#   - If timestamps not guaranteed increasing → need to sort on set → O(log n) set
#   - Real world: MongoDB oplog, git history, bitemporal data models

class TimeMap:
    def __init__(self):
        self.store = {}                                    # key → [[timestamp, value], ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])         # append — already sorted

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])                   # [] if key never set

        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r - l) // 2
            if values[m][0] <= timestamp:                  # valid candidate
                res = values[m][1]                         # best answer so far
                l = m + 1                                  # try to find newer
            else:
                r = m - 1

        return res

# Edge cases:
#   key never set → store.get returns [] → binary search skipped → return ""
#   timestamp before first entry → no valid candidate → return ""
#   timestamp after last entry → returns last value
#   exact timestamp match → returns that value

# Complexity:
#   set → O(1) amortised
#   get → O(log n) where n = number of set calls for that key
#   space → O(n) where n = total set calls across all keys

# Follow-ups:
#   Timestamps not guaranteed increasing → sort on set → O(log n) set
#   Thread safe → wrap set/get with threading.Lock
#   Distributed → shard by key, consistent hashing, each shard owns its history
#   TTL → add expiry per entry, background cleaner (same as Snapshot Array)
#   Real world: MongoDB oplog timestamps, Redis XADD streams, bitemporal DBs