class Solution:
    def maxProduct(self, s: str) -> int:
        arr = []
        result = 1
        for mask in range(1, 1<<len(s)):
            subseq = [s[i] for i in range(len(s)) if mask & (1<<i)]
            if subseq == subseq[::-1]:
                arr.append((len(subseq), mask))
        arr.sort(reverse=True)

        
        for i in range(len(arr)):
            if arr[i][0] ** 2 <= result: 
                break
            for j in range(i+1, len(arr)):
                if not arr[i][1] & arr[j][1]:
                    if arr[i][0] * arr[j][0] > result:
                        result = arr[i][0] * arr[j][0]
                        break
        
        return result