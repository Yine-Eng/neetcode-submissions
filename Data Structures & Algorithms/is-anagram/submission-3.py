class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        str_dict_s = {}
        for character in s:
            if character in str_dict_s:
                str_dict_s[character] += 1
            else:
                str_dict_s[character] = 1

        for character in t:
            if character in str_dict_s:
                str_dict_s[character] -= 1
            else:
                return False

        for value in str_dict_s.values():
            if value != 0:
                return False
        return True