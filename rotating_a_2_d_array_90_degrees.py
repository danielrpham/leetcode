"""
Problem: Rotating a 2-d array by 90 degrees clockwise:
https://leetcode.com/problems/rotate-image/ Description: You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        oned = list()
        pos = 1
        for i in range(n):
            for j in range(n):
                oned.append((pos, matrix[i][j]))
                pos += 1
        temp = [None] * (n ** 2)
        for x in oned:
            #print(((x * n) % (n**2 + 1)), x)
            temp[((x[0] * n) % (n**2 + 1)) - 1] = x[1]
        counter = 0
        


        for x in range(n):
            for y in range(n):
                matrix[x][y] = temp[counter]
                counter += 1