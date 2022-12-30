# Source: https://leetcode.com/problems/is-subsequence/
# ********************************************************************************** #
"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
of "abcde" while "aec" is not). """
# ********************************************************************************** #


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # keeping track if we make it through the string
                i += 1
            j += 1  # keep counter for t moving
        if i == len(s):  # check to see if all letters were found by comparing to len of string
            print(i)
            return True
        else:
            print(i)
            return False

