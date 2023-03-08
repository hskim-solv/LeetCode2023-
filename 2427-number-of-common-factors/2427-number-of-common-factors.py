class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        answer = 0
        N = gcd(a,b)
        if N == 1:
            return 1
        for i in range(2, int(N ** 0.5) + 1):
            if N % i == 0:
                answer += 1
                if N // i != i:
                    answer += 1
        answer += 1
        return answer + 1
        