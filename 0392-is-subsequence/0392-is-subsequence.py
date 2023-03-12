class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        #even_numbers = (n for n in numbers if not n % 2)
        #print(list(takewhile(lambda x: x != i, (j for j in t for i in s if i==j ))))
        l = len(s)

        for i in s:
            while t := deque(t):
                if i == t.popleft():
                    l -= 1
                    break 
        return not l
       
