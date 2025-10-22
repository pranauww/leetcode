from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        insert = 0
        i = 0
        while i < len(chars):
            grp = 1
            while (grp + i) < len(chars) and chars[i] == chars[grp+i]:
                grp += 1
            chars[insert] = chars[i]
            insert += 1
            if grp > 1:
                string = str(grp)
                chars[insert:insert+len(string)] = list(string)
                insert += len(string)
            i += grp
        return insert

def main():
    solution = Solution()
    
    # Test case 1: Example 1
    chars1 = ["a","a","b","b","c","c","c"]
    print("Test case 1:")
    print(f"Input: {chars1}")
    result1 = solution.compress(chars1)
    print(f"Output: {result1}, chars: {chars1[:result1]}")
    print(f"Expected: 6, ['a','2','b','2','c','3']")
    print()
    
    # Test case 2: Example 2
    chars2 = ["a"]
    print("Test case 2:")
    print(f"Input: {chars2}")
    result2 = solution.compress(chars2)
    print(f"Output: {result2}, chars: {chars2[:result2]}")
    print(f"Expected: 1, ['a']")
    print()
    
    # Test case 3: Example 3
    chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print("Test case 3:")
    print(f"Input: {chars3}")
    result3 = solution.compress(chars3)
    print(f"Output: {result3}, chars: {chars3[:result3]}")
    print(f"Expected: 4, ['a','b','1','2']")
    print()
    
    # Additional test cases
    # Test case 4: Single character repeated many times
    chars4 = ["a","a","a","a","a","a","a","a","a","a"]
    print("Test case 4:")
    print(f"Input: {chars4}")
    result4 = solution.compress(chars4)
    print(f"Output: {result4}, chars: {chars4[:result4]}")
    print(f"Expected: 3, ['a','1','0']")
    print()
    
    # Test case 5: All different characters
    chars5 = ["a","b","c","d","e"]
    print("Test case 5:")
    print(f"Input: {chars5}")
    result5 = solution.compress(chars5)
    print(f"Output: {result5}, chars: {chars5[:result5]}")
    print(f"Expected: 5, ['a','b','c','d','e']")
    print()
    
    # Test case 6: Mixed case with numbers
    chars6 = ["a","a","a","b","b","c","c","c","c","c"]
    print("Test case 6:")
    print(f"Input: {chars6}")
    result6 = solution.compress(chars6)
    print(f"Output: {result6}, chars: {chars6[:result6]}")
    print(f"Expected: 6, ['a','3','b','2','c','5']")
    print()
    
    # Test case 7: Edge case - very long sequence
    chars7 = ["x"] * 100
    print("Test case 7:")
    print(f"Input: {chars7[:10]}... (100 'x' characters)")
    result7 = solution.compress(chars7)
    print(f"Output: {result7}, chars: {chars7[:result7]}")
    print(f"Expected: 4, ['x','1','0','0']")
    print()

if __name__ == "__main__":
    main()
