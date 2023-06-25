class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length-1,-1,-1):
            for j in range(length):
                matrix[j].append(matrix[i].pop(0))