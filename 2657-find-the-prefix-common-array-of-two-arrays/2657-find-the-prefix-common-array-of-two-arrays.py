class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        cnt = 0
        for i in range(len(A)):
            if A[i]==B[i]:
                cnt += 1
            else:
                for _ in range(2):
                    if A[i] in B[:i]:
                        cnt += 1
                    A, B = B, A
            res.append(cnt)
        return res