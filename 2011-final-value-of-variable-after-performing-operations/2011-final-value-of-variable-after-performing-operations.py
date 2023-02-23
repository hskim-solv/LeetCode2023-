class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n = 0
        while operations:
            if "+" in operations.pop():
                n += 1
            else:
                n -= 1
        return n