"""
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3465/
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
"""

import math

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq_nums = list()
        # finding max and min number of digits
        l_digits, h_digits = int(math.log10(low))+1, int(math.log10(high))+1
        
        for i in range(l_digits, h_digits+1): #placeholder for digits
            for j in range(1, 9-i+2):
                temp = j
                while int(math.log10(temp))+1< i:
                    temp = temp*10 + (temp%10+1)
                if temp <= high and temp >= low: seq_nums.append(temp)
        return seq_nums