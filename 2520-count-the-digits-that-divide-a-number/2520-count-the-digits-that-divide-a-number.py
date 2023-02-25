class Solution:
    def countDigits(self, num: int) -> int:
        return sum( num % val == 0 for val in map(int, str(num) ) ) 
        