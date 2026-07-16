class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         status = False
         dic_n = {}
         for num in nums:
             if num in dic_n:
                 dic_n[num] += 1
             else:
                 dic_n[num] = 1

         for value in dic_n.values():
             if value > 1:
                 return True
         return status