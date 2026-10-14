class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return None

        for i in range(len(nums) - 1):
            v = target - nums[i]
            n = nums[i+1:]
            if v in n :
                return [i,n.index(v)+len(nums[:i+1])]


        
