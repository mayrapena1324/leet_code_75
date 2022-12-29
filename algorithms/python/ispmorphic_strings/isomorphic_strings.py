# Source :https://leetcode.com/problems/isomorphic-strings/

# ********************************************************************************** #
"""Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself."""
# ********************************************************************************** #

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Checks matching length of strings
        if len(s) != len(t):
            return False
        else:
            word_dict = {}
            for i in range(len(s)):
                # checking if key already exists
                if s[i] in word_dict:
                    # checking to see if the saved value matches.
                    if word_dict[s[i]] != t[i]:
                        return False
                else:
                    # If the key does not exist. Checks to see if value exist.
                    if t[i] in word_dict.values():
                        return False
                    else:
                        # if key: value pair does not exist, create the key and value
                        word_dict[s[i]] = t[i]
            return True
