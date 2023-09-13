class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        arr = []
        
        for mask in range(1, 1<<n):
            subseq = ''
            for i in range(n):
                # convert the bitmask to the actual subsequence
                if mask & (1 << i) > 0:
                    subseq += s[i]
            if subseq == subseq[::-1]:
                arr.append((len(subseq), mask))
        
        arr.sort(reverse=True)
        result = 1
        for i in range(len(arr)):
            len1, mask1 = arr[i]
            # break early
            if len1 ** 2 < result: break
            for j in range(i+1, len(arr)):
                len2, mask2 = arr[j]
                # disjoint
                if mask1 & mask2 == 0 and len1 * len2 > result:
                    result = len1 * len2
                    break
        
        return result