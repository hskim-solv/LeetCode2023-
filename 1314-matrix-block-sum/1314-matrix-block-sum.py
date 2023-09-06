class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
            
        h, w = len(mat), len(mat[0])
        integral_image = [ [ 0 for _ in range(w) ] for _ in range(h) ]
        # building integral image to speed up block sum computation
        for i in range(h):
            summation = 0
            for j in range(w):
                summation += mat[i][j]
                integral_image[i][j] = summation
                
                if i > 0:
                    integral_image[i][j] += integral_image[i-1][j]
        
        # compute block sum by looking-up integral image
        output_image = [ [ 0 for _ in range(w) ] for _ in range(h) ]
        for i in range(h):
            for j in range(w):
                #print(output_image)
                min_row, max_row = max(0, i-k), min(h-1, i+k)
                min_col, max_col = max(0, j-k), min(w-1, j+k)
               
                output_image[i][j] = integral_image[max_row][max_col]
                if min_row > 0:
                    output_image[i][j] -= integral_image[min_row-1][max_col]
                
                if min_col > 0:
                    output_image[i][j] -= integral_image[max_row][min_col-1]
                    
                if min_col > 0 and min_row > 0:
                    output_image[i][j] += integral_image[min_row-1][min_col-1]
                
        return output_image
        
        '''return [[sum(sum(mat[r][max(0,j-k):min(len(mat[0]),j+k+1)]) for r in range(max(0,i-k),min(len(mat),i+k+1))) for j in range(len(mat[0]))] for i in range(len(mat))]'''
            
