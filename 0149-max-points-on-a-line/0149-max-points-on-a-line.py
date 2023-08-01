class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        def s(p1,p2):
            if p2[1]==p1[1]:
                return inf, p2[1]
            elif p2[0]==p1[0]:
                return p2[0],inf
            a = (p2[1]-p1[1])/(p2[0]-p1[0])
            return a, p1[1]-a*p1[0]
        
        d = defaultdict(int)
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                a, b = s(points[i],points[j])
                if (a,b) in d:
                    continue
                init = False
                for k in range(j+1,len(points)):
                    xxx,yyy = points[k]
                    if (a == inf and b==yyy) or (a == xxx and b == inf) or math.isclose(yyy, b+a*xxx):
                        if init:
                            d[(a,b)] += 1
                        else:
                            d[(a,b)] = 3
                            init = True
        if d:
            return max(d.values())
        return 2
     