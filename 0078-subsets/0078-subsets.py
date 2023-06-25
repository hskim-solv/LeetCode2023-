class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.dfs(nums,[],res)
        return res
    
    def dfs(self,nums,path,res):
        res.append(path)
        for i in range(len(nums)):
            if path:
                if path[-1] < nums[i]:
                    self.dfs(nums[:i]+nums[i+1:],path+nums[i:i+1],res)
                else:
                    continue
            else:
                self.dfs(nums[:i]+nums[i+1:],path+nums[i:i+1],res)