class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        box = [0] * m * n
        for r,c in indices:
            for j in range(r*n,(r+1)*n):
                box[j] += 1
    
            for i in range(c, m*n, n):
                box[i] += 1

        return sum(x&1 for x in box)