class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums = Counter(nums).most_common()
        res = []
        for n, freq in nums:
            if len(res) < freq:
                diff = freq-len(res)
                for _ in range(diff):
                    res.append([n])
                for i in range(freq-diff):
                    res[i].append(n)
            else:
                for i in range(freq):
                    res[i].append(n)
        return res