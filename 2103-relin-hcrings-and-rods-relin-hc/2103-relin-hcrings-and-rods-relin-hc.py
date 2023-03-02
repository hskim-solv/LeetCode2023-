class Solution:
    def countPoints(self, rings: str) -> int:
        rgb = { i:"" for i in set(rings[1::2]) }
        print(rgb)
        for i in range(0,len(rings),2):
            color, th = rings[i:i+2]
            rgb[th] += color
        return sum( len(set(x))==3 for x in rgb.values())
        