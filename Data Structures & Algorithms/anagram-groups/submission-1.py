from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # output = []
        # iteration i = 0 => "act"
        # output = [["act"]]
        
        # iteration i = 1 => "pots"
        # output = [["act"], ["pots"]]

        # iteration i = 2 => "tops"
        # output = [["act"], ["pots", "tops"]]

        output = []

        for str in strs:
            i = 0
            found = False
            while i < len(output):
                if Counter(output[i][0]) == Counter(str):
                    output[i].append(str)
                    found = True
                i += 1
            
            # if we didn't find any anagram of str, we append a list
            # of str to output
            if not found:
                output.append([str])

        return output





