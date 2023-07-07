class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        for n, freq in Counter(nums).most_common():
            if len(res) < freq:
                for i in range(len(res)):
                    res[i].append(n)
                for _ in range(freq-len(res)):
                    res.append([n])

            else:
                for i in range(freq):
                    res[i].append(n)
        return res