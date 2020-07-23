"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3395/
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""

class Solution:
    def findNum(self, num):
        bin_sum = 0
        counter = 1
        while (num):
            if (num % 10) == 1:
                bin_sum += counter
            num = num // 10
            counter *= 2
        return bin_sum
    

    def addBinary(self, a: str, b: str) -> str:
        a = int(a)
        b = int(b)
        a = self.findNum(a)
        b = self.findNum(b)
        return bin(a+b)[2:]