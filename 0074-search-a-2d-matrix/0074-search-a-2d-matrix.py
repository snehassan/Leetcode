import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_list = [x for sublist in matrix for x in sublist]
        if target in matrix_list:
            return True
        else:
            return False
    


