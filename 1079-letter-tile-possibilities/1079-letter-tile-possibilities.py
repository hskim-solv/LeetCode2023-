class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = 0
        for i in range(1,len(tiles)+1):
            box = []
            for j in permutations(tiles, i):
                box.append(j)
            res += len(set(box))
        return res