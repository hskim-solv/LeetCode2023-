class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums = Counter(nums).most_common()
        res = []
        for n, freq in nums:
            if len(res) < freq:
                for _ in range(freq-len(res)):
                    res.append([])
            for i in range(freq):
                res[i].append(n)
        return res