class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Find the median of two sorted arrays in O(log(min(m, n))) time
        using binary search on partitions.
        """
        # Ensure nums1 is the smaller array for O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2  # Size of the left partition

        left, right = 0, m

        while left <= right:
            mid1 = (left + right) // 2
            mid2 = half - mid1

            # Get boundary elements; use ±infinity for out-of-bounds
            l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = nums1[mid1]     if mid1 < m  else float('inf')
            l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            r2 = nums2[mid2]     if mid2 < n  else float('inf')

            if l1 <= r2 and l2 <= r1:
                # Found the correct partition
                if (m + n) % 2 == 1:
                    return float(max(l1, l2))
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # Too many elements from nums1 on the left
                right = mid1 - 1
            else:
                # Too few elements from nums1 on the left
                left = mid1 + 1

        # Should never be reached if inputs are valid
        return float('nan')