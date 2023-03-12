class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        #even_numbers = (n for n in numbers if not n % 2)
        #print(list(takewhile(lambda x: x != i, (j for j in t for i in s if i==j ))))
        x,l = 0 , len(s)
        t, s = deque(t), deque(s)
        while s:
            i = s.popleft() 
            while t:
                if i == t.popleft():
                    x+=1
                    break 
        return x == l
       
