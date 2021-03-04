class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s:str):
        if s == "":
            return True
        s = s.lower()
        z = ""
        for i in s:
            if ord("a") <= ord(i) <= ord("z"):
                z += i
        return z == z[::-1]