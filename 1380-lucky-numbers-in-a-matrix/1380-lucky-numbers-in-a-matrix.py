class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        return [max(col) for col in zip(*matrix) if min(matrix[col.index(max(col))]) == max(col)]