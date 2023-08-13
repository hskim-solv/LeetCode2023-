class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        cnt = 0
        for i in range(len(A)):
            if A[i]==B[i]:
                cnt += 1
            else:
                for l1,l2 in [[A,B],[B,A]]:
                    if l1[i] in l2[:i]:
                        cnt += 1
            res.append(cnt)
        return res