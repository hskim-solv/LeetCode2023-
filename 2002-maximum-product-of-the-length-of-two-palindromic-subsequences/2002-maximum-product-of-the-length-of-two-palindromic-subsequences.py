class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        arr = []
        
        for mask in range(1, 1<<n):
            subseq = ''
            for i in range(n):         
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                arr.append((len(subseq), mask))
        
        arr.sort(reverse=True)
        result = 1
        for i in range(len(arr)):
            if arr[i][0] ** 2 <= result: 
                break
            mask1 = arr[i][1]
            for j in range(i+1, len(arr)):
                #len2, mask2 = arr[j]
                # disjoint
                if mask1 & arr[j][1]:
                    continue
                if arr[i][0] * arr[j][0] > result:
                    result = arr[i][0] * arr[j][0]
                    break
        
        return result