class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count("U") != moves.count("D"):
            return False
        elif moves.count("L") != moves.count("R"):
            return False
        else:
            return True
        
        