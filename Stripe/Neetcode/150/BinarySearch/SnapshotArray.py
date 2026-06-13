class SnapshotArray:

    def __init__(self, length):
        # Store only changes and not the entire snapshot
        # history[index] = [[snap_id, value], ...]
        # Start with [-1, 0] so every index defaults to 0
        self.history = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # Record value change at current snapshot
        self.history[index].append([self.snap_id, val])

    def snap(self) -> int:
        # Take snapshot and return its id
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Find latest value whose snap_id <= requested snap_id
        history = self.history[index]

        l, r = 0, len(history) - 1
        pos = -1

        while l <= r:
            mid = (l + r) // 2
            # mid = l + ((r-l) // 2)

            if history[mid][0] <= snap_id:
                pos = mid          # valid answer
                l = mid + 1        # try to find a newer one
            else:
                r = mid - 1

        return history[pos][1]