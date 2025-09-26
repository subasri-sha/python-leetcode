class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
         # Start from the end of the merged array
        write_index = m + n - 1
      
        # Pointers to the last valid elements in each array
        nums1_index = m - 1
        nums2_index = n - 1
      
        # Continue until all elements from nums2 are processed
        while nums2_index >= 0:
            # If nums1 still has elements and current element is larger than nums2's
            if nums1_index >= 0 and nums1[nums1_index] > nums2[nums2_index]:
                # Place the larger element from nums1 at the current position
                nums1[write_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                # Place the element from nums2 (either it's larger or nums1 is exhausted)
                nums1[write_index] = nums2[nums2_index]
                nums2_index -= 1
          
            # Move the write position one step back
            write_index -= 1