class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for flight in flights:
            depart, dest, price = flight
            if depart not in adj:
                adj[depart] = []
            adj[depart].append( (dest, price) )

        q = deque()
        q.append((0, src, 0))
        
        dist = [float("inf")] * n

        minCost = float("inf")
        while q:
            curStop, airp, price = q.popleft()
            if curStop > k:
                continue

            if airp not in adj: continue
            for flt, cost in adj[airp]:
                new_price = price + cost
                if new_price < dist[flt]:
                    dist[flt] = new_price
                    if flt == dst:
                        minCost = min(minCost, new_price)
                    elif curStop < k:
                        q.append((curStop + 1, flt, new_price))
        
        return minCost if minCost < float("inf") else -1