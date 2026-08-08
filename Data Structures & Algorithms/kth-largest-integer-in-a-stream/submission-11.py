class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.targ = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.targ:
            heapq.heappop(self.heap)

        return self.heap[0]
