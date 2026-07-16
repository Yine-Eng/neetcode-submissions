class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        right = 0
        longest = 0

        for left in range(len(s)):
            while right < len(s) and s[right] not in unique:
                unique.add(s[right])
                right += 1

            longest = max(longest, (right - left))
            unique.remove(s[left])

        return longest