class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last = { c : i for i, MPG in enumerate(garbage) for c in MPG}
        dis = list( accumulate(travel, initial = 0) )
        return sum( map( len, garbage ) ) + sum(dis[last.get(c, 0)] for c in 'PGM')
            