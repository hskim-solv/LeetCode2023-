class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        return [names[heights.index(s)] for s in sorted(heights,reverse=True)]
        