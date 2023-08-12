class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        rnge = [-1, n]
        res = []
        
        while s:
            cnt = 0
            y,x = startPos
            for c in s:
                if c == "R":
                    x += 1
                elif c == "L":
                    x -= 1
                elif c == "U":
                    y -= 1
                else: # D
                    y += 1
                
                if x in rnge or y in rnge:
                    break
                cnt += 1  
            res.append(cnt)
            s = s[1:]
        return res