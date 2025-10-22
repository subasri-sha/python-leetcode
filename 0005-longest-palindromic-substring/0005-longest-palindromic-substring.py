class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        res_len = 0

        for i in range(len(s)):
            # Odd length
            l, r = i, i # Tuple unpacking
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    result = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    result = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        return result
        