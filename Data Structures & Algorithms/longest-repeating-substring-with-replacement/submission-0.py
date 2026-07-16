from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        char_count = Counter()
        longest = 0

        for right in range(len(s)):
            # Add the current character to the frequency counter
            char_count[s[right]] += 1

            # Update the maximum frequency of any character in the current window
            max_freq = max(max_freq, char_count[s[right]])

            # Calculate the number of replacements needed
            window_size = right - left + 1
            replacements_needed = window_size - max_freq

            # If replacements exceed k, shrink the window
            if replacements_needed > k:
                char_count[s[left]] -= 1
                left += 1

            # Update the longest valid window size
            longest = max(longest, right - left + 1)

        return longest
