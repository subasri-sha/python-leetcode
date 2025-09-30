class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)): # Loops through every index i in the list.
            for j in range(i, len(nums)): # This compares each element nums[i] with every other element nums[j].
                if nums[i] + nums[j] == target and i != j:
                    return i, j

        #  dic = {}  # initialise an empty dictionary

        # for i, val in enumerate(nums):
        #     if target - val in dic:
        #         return [dic[target - val], i]
        #     else:
        #         dic[val] = i
    
        