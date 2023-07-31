class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        def s(p1,p2):
            if p2[1]==p1[1]:
                return inf, p2[1]
            if p2[0]==p1[0]:
                return p2[0],inf
            a = (p2[1]-p1[1])/(p2[0]-p1[0])
            b = p1[1]-a*p1[0]

            return a, b
        d = defaultdict(int)
        for i in range(len(points)-2):

            for j in range(i+1,len(points)-1):

                a, b = s(points[i],points[j])
                #print(a,b)
                if (a,b) in d:
                    continue
                
                for k in range(j+1,len(points)):
                    xxx,yyy = points[k]
                    if a == inf:
                        if b == yyy:
                            if (a,b) not in d:
                                d[(a,b)] = 3
                            else:
                                d[(a,b)] += 1
                    elif b == inf:
                        if a == xxx:
                            if (a,b) not in d:
                                d[(a,b)] = 3
                            else:
                                d[(a,b)] += 1
                    elif math.isclose(yyy, b+a*xxx):
                        if (a,b) not in d:
                            d[(a,b)] = 3
                        else:
                            d[(a,b)] += 1
        #print(d)
        if d:
            return max(d.values())
        return 2
        '''
        for i in range(0,len(points)-1):
            for j in range(i+1,len(points)):
                x,y = points[j]
                if y == 
                a, b = s(points[i],points[j])
                if points[i] not in d[(a,b)]:
                    d[(a,b)].append(points[i])
                if points[j] not in d[(a,b)]:
                    d[(a,b)].append(points[j])
                d[(a,b)] += 1
        #print(d.items())
        return max(d.values())
        '''
        '''
        def helper(points):
            if len(points) < 3:
                return len(points)
            x0, y0 = points[0]
            x1, y1 = points[1]
            a = (x1-x0) / (y1-y0)
            b = y1 - a*x1
            cnt = 2
            for j in range(2, len(points)):
                x1, y1 = points[j]
                if y1 == a*x1+b:
                    cnt += 1
                else:
                    return helper(points[j:])
            return cnt
                
        
        return helper(points)
        '''
       