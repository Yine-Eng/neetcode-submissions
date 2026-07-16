class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        single_occurrences = {}

        for num in nums:
            if num not in single_occurrences:
                single_occurrences[num] = 1
            else:
                return True
        
        return False