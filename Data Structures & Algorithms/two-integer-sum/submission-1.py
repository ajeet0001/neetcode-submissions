class Solution:
    def twoSum(self, nums: List[int], tar: int) -> List[int]:
        total = {}
        for i in range(len(nums)):
            if tar - nums[i] in total:
                return [total[tar-nums[i]],i]
            total[nums[i]] = i
        return [-1,-1]