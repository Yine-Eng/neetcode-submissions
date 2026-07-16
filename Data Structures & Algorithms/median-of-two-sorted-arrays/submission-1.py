class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2
        left, right = 0, len(nums1) - 1

        while True:
            i = (left + right) // 2  # Partition index for nums1
            j = half - i - 2  # Partition index for nums2

            nums1_left = nums1[i] if i >= 0 else float("-inf")
            nums1_right = nums1[i + 1] if (i + 1) < len(nums1) else float("inf")

            nums2_left = nums2[j] if j >= 0 else float("-inf")
            nums2_right = nums2[j + 1] if (j + 1) < len(nums2) else float("inf")

            # Check if partition is correct
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Odd case
                if total % 2 != 0:
                    return min(nums1_right, nums2_right)

                # Even case
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2

            # Adjust partition
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1

