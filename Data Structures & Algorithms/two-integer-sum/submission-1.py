class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We can creat a hash map of this format:
        # {key = index: value will be complement}
        # We will start with an empty hash map

        # Next, we can go through nums in and if
        # nothing is in nums, we add


        hash_map = {}

        for i in range(len(nums)):
            jigsaw = target - nums[i]

            if jigsaw in hash_map:
                return [hash_map[jigsaw], i]
            else:
                hash_map[nums[i]] = i

        # Input = [4, 2, 7, 5, 6]

        # First iteration:
        # start hashmap = {}
        # after the for loop runs:
        # index = 0, value = 4, jigsaw = 6
        # hashmap = {4: 0}

        # Second iteration:
        # start hashmap = {4: 0}
        # after the for loop runs:
        # index = 1, value = 2, jigsaw = 8
        # hashmap = {4: 0, 2: 1}

        # Third iteration:
        # start hashmap = {4: 0, 2: 1}
        # after the for loop runs:
        # index = 2, value = 7, jigsaw = 3
        # hashmap = {4: 0, 2: 1, 7: 2}

        # Fourth iteration:
        # start hashmap = {4: 0, 2: 1, 7: 2}
        # after the for loop runs:
        # index = 3, value = 5, jigsaw = 5
        # hashmap = {4: 0, 2: 1, 7: 2, 5: 3}

        # Fifth iteration:
        # start hashmap = {4: 0, 2: 1, 7: 2, 5: 3}
        # after the for loop runs:
        # index = 4, value = 6, jigsaw = 4
        # hashmap = {4: 0, 2: 1, 7: 2, 5: 3}

