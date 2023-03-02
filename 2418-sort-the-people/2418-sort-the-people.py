class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        return [ names[i] for i,n in sorted(enumerate(heights), key = lambda x:x[1], reverse=True) ]
        