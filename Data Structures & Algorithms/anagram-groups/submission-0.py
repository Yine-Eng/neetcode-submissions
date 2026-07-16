class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        start = {}
        index = 0

        while index < len(strs):
            key = tuple(sorted(strs[index]))
            if key not in start:
                start[key] = [strs[index]]
            else:
                start[key].append(strs[index])
            
            index += 1

        print(start)
        return (list(start.values()))