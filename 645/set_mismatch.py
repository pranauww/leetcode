class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        for i in range(1, len(nums)+1):
            count[i] = 0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for c in count:
            if count[c] > 1:
                res.append(c)
        
        for c in count:
            if count[c] < 1:
                res.append(c)
        
        return res
        