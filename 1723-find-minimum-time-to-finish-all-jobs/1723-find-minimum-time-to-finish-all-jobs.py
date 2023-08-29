class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True)

        def dfs(i):
            if i == n: 
                return True
            
            for j in range(k):
                if cap[j] >= jobs[i]:
                    cap[j] -= jobs[i]
                    if dfs(i + 1): 
                        return True
                    cap[j] += jobs[i]
                if cap[j] == x: 
                    break
            return False

        # binary search
        left, right = max(jobs), sum(jobs)
        while left < right:
            x = (left + right) // 2
            cap = [x] * k
            if dfs(0):
                right = x
            else:
                left = x + 1
        return left