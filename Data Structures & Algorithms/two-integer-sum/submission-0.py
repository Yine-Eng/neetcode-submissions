class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            jig_saw = target - nums[i]

            if jig_saw in hash_map:
                return [hash_map[jig_saw], i]

            hash_map[nums[i]] = i