class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        return list(chain(*[ [n]*cnt for n, cnt in sorted(Counter(nums).most_common(),key=lambda x: (x[1], -x[0])) ]))