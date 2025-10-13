class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        duplicate_set = set()
        result = 0
        length = 0

        for i in range(0, len(s)):
            while s[i] in duplicate_set: # checks for every duplicates in the set
                    duplicate_set.remove(s[length])
                    length += 1 # length increases by 1 after traversing each element in set
            duplicate_set.add(s[i])
            result = max(result, i - length + 1)
        return result


