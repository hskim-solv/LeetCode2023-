class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        #print( list(Counter(list(Counter(nums).items())).items() ) )
        return all(x % 2 == 0 for x in Counter(nums).values())  
        #print( list(Counter(nums).values())  )
      