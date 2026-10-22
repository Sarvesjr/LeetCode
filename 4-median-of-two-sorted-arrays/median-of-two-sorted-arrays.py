class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            l1 = float('-inf') if i == 0 else nums1[i - 1]
            r1 = float('inf') if i == m else nums1[i]

            l2 = float('-inf') if j == 0 else nums2[j - 1]
            r2 = float('inf') if j == n else nums2[j]

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return float(max(l1, l2))

            elif l1 > r2:
                right = i - 1
            else:
                left = i + 1

        return 0.0