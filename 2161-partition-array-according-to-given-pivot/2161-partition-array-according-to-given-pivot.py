class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, m , greater = [],[],[]
        for n in nums:
            if n < pivot:
                less.append(n)
            elif n > pivot:
                greater.append(n)
            else:
                m.append(n)
        return less +m+ greater
    