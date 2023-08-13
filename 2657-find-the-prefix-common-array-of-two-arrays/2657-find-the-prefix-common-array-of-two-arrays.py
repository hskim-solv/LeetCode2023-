class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        cnt = 0
        for i in range(len(A)):
            if A[i]==B[i]:
                cnt += 1
            else:
                if A[i] in B[:i]:
                    cnt += 1
                if B[i] in A[:i]:
                    cnt += 1
            res.append(cnt)
        return res