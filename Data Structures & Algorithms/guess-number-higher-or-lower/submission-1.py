# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s, e = 0, n
        answer = n // 2
        response = guess(answer)
        while response != 0:
            if response == 1:
                s = answer + 1
            else:
                e = answer - 1
            answer = (e + s) // 2
            response = guess(answer)
        
        return answer
        