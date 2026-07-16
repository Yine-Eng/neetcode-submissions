class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dictionary with keys as elements in nums and values as their frequency
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        #create an empty integer array to store the keys with the values 
        arr = []

        #create a highest value, set the variable to zero, and store the value as you loop through
        

        #create a variable called highest key and set it to None

        #loop through the keys and values in the dictionary, decreatmenting k and continuing while k is not 0
        while k != 0:
            highest_value = 0
            highest_key = None
            for key, value in dic.items():
                if value > highest_value:
                    highest_value = value
                    highest_key = key
            arr.append(highest_key)
            dic.pop(highest_key, None)
            k -= 1
        return arr