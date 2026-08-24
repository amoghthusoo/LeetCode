class Solution:
    def isPalindromic(self, s: str) -> bool:

        bin_str = ""
        for ch in s:
            bin_str += bin(ord(ch))[2:].zfill(8)

        if(bin_str == bin_str[-1::-1]):
            return True

        return False

    