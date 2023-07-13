class Solution:

    def __init__(self, nums: List[int]):
        self.ori = nums
        self.nums = deepcopy(nums)
        

    def reset(self) -> List[int]:
        return self.ori


    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()