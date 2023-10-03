class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        for q in queries:
            sm = 0
            cnt = 0
            for n in nums:
                sm += n
                if q < sm:
                    break
                cnt += 1
            res.append(cnt)
        return res