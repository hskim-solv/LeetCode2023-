class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = 0
        for n, freq in Counter(nums).most_common():
            if freq > length:
                for i in range(length):
                    res[i].append(n)
                for _ in range(freq-length):
                    res.append([n])
                length = freq
            else:
                for i in range(freq):
                    res[i].append(n)
        return res