class Solution:
    def pivotInteger(self, n: int) -> int:
        x = i = 1
        y = j = n

        while i != j:
            if x < y:
                i += 1
                x += i
            else:
                j -= 1
                y += j
        if x == y:
            return i
        return -1
        