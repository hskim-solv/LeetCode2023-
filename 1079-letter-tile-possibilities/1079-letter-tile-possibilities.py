class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        
        return  sum([ len(set(permutations(tiles, i)))  for i in range(1,len(tiles)+1) ]) 