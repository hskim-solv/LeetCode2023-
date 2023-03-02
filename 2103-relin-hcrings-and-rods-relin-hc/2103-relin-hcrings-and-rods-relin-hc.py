class Solution:
    def countPoints(self, rings: str) -> int:
        rgb = { i : "" for i in set(rings[1::2]) }
        for i in range(0, len(rings), 2):
            rgb[rings[i+1]] += rings[i]
        return sum( len(set(x))==3 for x in rgb.values())
        