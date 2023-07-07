class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        for n, freq in Counter(nums).most_common():
            length = len(res)
            if length < freq:
                for i in range(length):
                    res[i].append(n)
                for _ in range(freq-length):
                    res.append([n])

            else:
                for i in range(freq):
                    res[i].append(n)
        return res