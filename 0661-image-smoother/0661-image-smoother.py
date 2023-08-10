class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0]) if m else 0
        res = deepcopy(img)
        for x in range(m):
            for y in range(n):
                neighbors = [
                    img[_x][_y]
                    for _x in (x-1, x, x+1)
                    for _y in (y-1, y, y+1)
                    if 0 <= _x < m and 0 <= _y < n
                ]
                res[x][y] = sum(neighbors) // len(neighbors)
        return res
        
        