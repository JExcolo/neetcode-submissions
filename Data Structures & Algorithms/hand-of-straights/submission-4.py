class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        rounds = len(hand) // groupSize
        
        hash = {}

        for num in hand:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        
        for _ in range(rounds):
            cur = min(hash)
            for i in range(cur, groupSize + cur):
                if i not in hash or hash[i] == 0:
                    return False
                else:
                    hash[i] -= 1
                    if hash[i] == 0:
                        del(hash[i])
        return True


