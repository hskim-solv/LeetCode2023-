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
        res = 0
        for i in range(len(points)-2):
            #d = defaultdict(int)
            for j in range(i+1,len(points)-1):
                d = defaultdict(int)
                a, b = s(points[i],points[j])

                for k in range(j+1,len(points)):
                    xxx,yyy = points[k]
                    if (a == inf and b==yyy) or (a == xxx and b == inf) or math.isclose(yyy, b+a*xxx):
                        d[(a,b)] += 1
            
                if d:
                    res = max(res,*d.values())
        return res + 2
     