from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = {}
        for flight in flights:
            depart, dest, price = flight
            if depart not in adj:
                adj[depart] = []
            if dest not in adj:
                adj[dest] = []
            adj[depart].append( (dest, price) )
        
        prices = [float("inf")] * n
        prices[src] = 0

        q = deque()
        q.append((0, src, 0))

        while q:
            ks, d, p = q.popleft()
            if ks > k:
                break
            for nD, nP in adj[d]:
                if prices[nD] > p + nP:
                    prices[nD] = p + nP
                    q.append( (ks + 1, nD, p + nP) )
                
        return -1 if prices[dst] == float("inf") else prices[dst]
 