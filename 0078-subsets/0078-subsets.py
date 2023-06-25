class Solution:
   def __init__(self):
       self.res = []
       
   def subsets(self, nums, path=[]):
       self.res.append(path)
       for i in range(len(nums)):
           self.subsets(nums[i+1:], path+nums[i:i+1])
       return self.res