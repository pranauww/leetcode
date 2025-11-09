class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1

        while left <= right and top <= bottom:
            for i in range(left, right+1):
                output.append(matrix[top][i])
            top += 1            
            
            for i in range(top, bottom+1):
                output.append(matrix[i][right])
            right -= 1

            if top-1 != bottom:    
                for i in range(right, left-1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1
                

            if left != right+1:    
                for i in range(bottom, top-1, -1):
                    output.append(matrix[i][left])
                left += 1
            
        return output