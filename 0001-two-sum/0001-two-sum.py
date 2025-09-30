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
        # Alternative code for better time complexity
        #  dic = {}  # initialise an empty dictionary

        # for i, val in enumerate(nums): # enumerate(nums) gives both index i and value val.
        #     if target - val in dic:    # checks target - val in dic, if target - value in dict
        #         return [dic[target - val], i]  # return the difference with its index i.e difference : i
        #     else: 
        #         dic[val] = i # if not it stores the value in dic
    
        