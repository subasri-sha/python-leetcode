class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # by brute force method with worst TC
        # nums1 = nums1 + nums2
        # nums1.sort()
        # if len(nums1) % 2 != 0:
        #     return nums1[len(nums1)// 2]
        # return (nums1[(len(nums1) // 2) - 1] + nums1[len(nums1) // 2]) / 2

        # Optimal approach
        # combine and sort array using merging sort array to get optimized TC

        ans = []
        nums1_pt, nums2_pt = 0, 0

        while nums1_pt < len(nums1) and nums2_pt < len(nums2):
            if nums1[nums1_pt] < nums2[nums2_pt]:
                ans.append(nums1[nums1_pt])
                nums1_pt += 1
            else:
                ans.append(nums2[nums2_pt])
                nums2_pt += 1
        while nums1_pt < len(nums1):
            ans.append(nums1[nums1_pt])
            nums1_pt +=1

        while nums2_pt < len(nums2):
            ans.append(nums2[nums2_pt])
            nums2_pt +=1
        

        n = len(ans)
        if n % 2 != 0:
            return float(ans[n // 2])
        else:
            return (ans[(n // 2) - 1] + ans[n // 2]) / 2.0


    