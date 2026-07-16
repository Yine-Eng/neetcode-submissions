class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1 = [1, 6, 10, 13]
        # nums2 = [7, 9, 12]


        nums1 += nums2
        # here: nums1 = [1, 6, 10, 13, 7, 9, 12]

        nums1.sort()
        # here: nums1 = [1, 6, 7, 9, 10, 12, 13]

        # Mathematics for for finding median:
        # if len(nums) % 2 != return mid number as median

        # we return (sum of mid number and the number after mid) / 2
        # else:

        # odd case
        # odd input = [1, 6, 7, 9, 10, 12, 13]
        # 7 // 2 = 3
        # median = 9

        mid = len(nums1) // 2

        if len(nums1) % 2 != 0:
            return nums1[mid]
        
        # Even case
        # even input = [1, 6, 7, 9, 10, 12, 13, 14]
        # mid = 8 // 2 = 4
        # median = (10 + 9) / 2 = 9.5
        else:
            median = (nums1[mid] + nums1[mid - 1]) / 2
            return median