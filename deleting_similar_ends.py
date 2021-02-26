"""
Question is taken from leetcode (1750. Minimum Length of String After Deleting Similar Ends)
One can see the question using the link https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
Leetcode holds credit for this problem and this video is for educational purpose
"""

"""
Question is as below
====================
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).
"""


def minimum_length_String(s):

    N = len(s)
    l = 0
    r = N - 1
    """
    len(s) ==> (r - l) + 1
    because in the last we will return r and l combination
    r >= l we use equal sign because using that we can have
    minimum two characters returned which is true
    Since no use of any extra space is needed for this code
    hence space complexity is O(1), whereas the time complexity is
    O(n)
    """
    while (r - l) + 1 > 1 and s[l] == s[r]:
        current = s[l]
        while r >= l and s[l] == current:
            l += 1
        while r >= l and s[r] == current:
            r -= 1
    return (r -l) + 1

  
string = "cabaabac"
print(minimum_length_String(string))
