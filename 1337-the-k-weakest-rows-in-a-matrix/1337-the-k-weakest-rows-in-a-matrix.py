class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return list( 
                list(
                    zip(
                *sorted( 
                    [ 
                        (sum( takewhile(lambda x: x, row) ) , i)                          for i, row in enumerate(mat) 
                    ] 
                )[:k]  
                    ) 
            
            )[1]
    ) 
        
             