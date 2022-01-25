# Hashmap

class OrderedStream:

    def __init__(self, n: int):
        self.seen = {}
        self.ptr = 1

    def insert(self, id: int, value: str):
        seen, ptr = self.seen, self.ptr

        seen[id] = value
        result = []
        while ptr in seen:  # check if next largest occurs
            result.append(seen[ptr])
            del seen[ptr]
            ptr += 1

        self.ptr = ptr
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
