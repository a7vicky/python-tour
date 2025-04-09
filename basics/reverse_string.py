"""
Given a string s, reverse the string without reversing its individual words. Words are separated by spaces.

Note: The string may contain leading or trailing spaces, or multiple spaces between two words. The returned string should only have a single space separating the words, and no extra spaces should be included.
"""

class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, s):
        #.split() splits the string into words, ignoring all whitespace (no matter how many spaces).
        # '.join(...) joins the words back together with a single space.
        ns = ' '.join(s.split())
        return ' '.join(ns.split()[::-1])

if __name__ == "__main__":
    print("Example 1:")
    print(Solution().reverseWords("Let's take a contest for a while! "))

