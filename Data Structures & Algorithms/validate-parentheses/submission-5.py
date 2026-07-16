class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "{":"}", "[":"]"}
        arr = []
        for i in s:
            if i in dic:
                arr.append(i)
            else:
                if not arr or i != dic[arr.pop()]:
                    return False
        return not arr
