class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for c in count:
            if count[c] > 1:
                return True
        
        return False
        