import heapq
from heapq import heappush, heappop

# Clarify: timestamps can be corrected? current() always valid (at least one update)?
# Key insight: hashmap for O(1) lookup, two heaps for O(log n) min/max
# Lazy deletion — only clean stale heap entries when queried
#
# Volunteer before being asked:
#   - Naive: sort on every update → O(n log n) per update, too slow
#   - Two heaps + lazy deletion → O(log n) update, O(log n) amortised min/max
#   - SortedList alternative → O(1) min/max but requires external library
#   - latest_time tracks current() in O(1) — don't iterate to find max timestamp
#   - Real world: stock tickers, sensor data streams, live leaderboards

class StockPrice:
    def __init__(self):
        self.latest_time = 0
        self.timestamp_price_map = {}                      # timestamp → price
        self.max_heap = []                                 # (-price, timestamp)
        self.min_heap = []                                 # (price, timestamp)

    def update(self, timestamp: int, price: int) -> None:
        self.timestamp_price_map[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)
        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))       # negate for max heap

    def current(self) -> int:
        return self.timestamp_price_map[self.latest_time]  # O(1)

    def maximum(self) -> int:
        # lazy delete stale entries
        price, timestamp = self.max_heap[0]
        while -price != self.timestamp_price_map[timestamp]:
            heappop(self.max_heap)
            price, timestamp = self.max_heap[0]
        return -price

    def minimum(self) -> int:
        # lazy delete stale entries
        price, timestamp = self.min_heap[0]
        while price != self.timestamp_price_map[timestamp]:
            heappop(self.min_heap)
            price, timestamp = self.min_heap[0]
        return price

# Edge cases:
#   same timestamp updated multiple times → hashmap always has latest, heaps lazily cleaned
#   current() after correction → latest_time unchanged if same timestamp, correct price returned
#   maximum/minimum after all corrections → lazy deletion handles all stale entries

# Complexity:
#   update  → O(log n)
#   current → O(1)
#   maximum → O(log n) amortised
#   minimum → O(log n) amortised
#   space   → O(n) where n = total updates

# Follow-ups:
#   Single structure → SortedList from sortedcontainers → O(1) min/max, O(log n) update
#   Thread safe → threading.Lock around all operations
#   Distributed → shard by timestamp range, global min/max needs cross-shard query
#   Real world: stock tickers, IoT sensor streams, live leaderboards