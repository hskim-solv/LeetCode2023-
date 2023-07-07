class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = 0
        for n, freq in Counter(nums).most_common():
            diff = freq-length
            if diff > 0:
                for i in range(length):
                    res[i].append(n)
                for _ in range(diff):
                    res.append([n])
                length = freq
            else:
                for i in range(freq):
                    res[i].append(n)
        return res