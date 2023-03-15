class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        return list( map( sum, zip(*map(lambda x: divmod(x,2),Counter(nums).values() ) ) ) )