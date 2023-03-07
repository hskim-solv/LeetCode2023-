class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        #return ''.join( [k for k, v in Counter(arr).items() if v == 1][k-1:k] )
        return ''.join( [i for i in arr if arr.count(i) == 1][k-1:k])

