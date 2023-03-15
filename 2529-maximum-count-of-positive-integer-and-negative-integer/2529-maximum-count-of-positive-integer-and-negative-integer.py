class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(  *map( sum, zip( *[(x > 0, x < 0) for x in nums] ) ) )
        